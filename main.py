from smarthouse import SmartHouse
from devices import *
from persistence import SmartHousePersistence
from datetime import datetime

def load_demo_house(persistence: SmartHousePersistence) -> SmartHouse:
    result = SmartHouse(persistence)
    cur = result.persistence.cursor

    #Temporary sensor identifiers
    sensor_id = [3, 8, 11, 12, 14, 17, 21, 28]
    units = ['%', '°C', 'kWh', '°C', 'kWh', 'g/m^2', '%', '°C']

    #Read number of floors
    floors = "SELECT r.floor FROM  rooms r group by r.floor;"
    cur.execute(floors)
    #Add floors
    for floor in cur.fetchall():
        f = result.create_floor()
        rooms = f"SELECT * FROM  rooms r WHERE r.floor = {floor[0]};"
        cur.execute(rooms)
        #Add rooms to corresponding floors
        for room in cur.fetchall():
            r = result.create_room( floor_no = room[1], area = room[2], name = room[3])
            devices = f"SELECT * FROM devices d WHERE d.room = {room[0]};"
            cur.execute(devices)
            #Add devices to rooms
            for device in cur.fetchall():
                d: Device
                #Determine if device is sensor or actuator
                if device[0] in sensor_id:
                    d = Sensor(device[0], device[2], device[3], device[4], device[5], units[sensor_id.index(device[0])])
                    #Fetch most recent measurment
                    measurement = f"SELECT m.time_stamp, m.value FROM measurements m WHERE m.device = {device[0]} ORDER by DATETIME(m.time_stamp) DESC LIMIT 1;"
                    cur.execute(measurement)
                    m = cur.fetchone()
                    if m is not None:
                        dt = datetime.fromisoformat(m[0])
                        temp = Measurement(date=dt.date(), time=dt.time(), value=m[1])
                        d.measurements.append(temp)

                else:
                    actuator = f"SELECT Value FROM Actuator a WHERE a.Device = {device[0]} order by Id DESC;"
                    cur.execute(actuator)
                    a = cur.fetchone()
                    d = Actuator(device[0], device[2], device[3], device[4], device[5])
                    if a is not None:
                        d.value = a[0]

                if device[6] == "On":
                    d.On()
                else:
                    d.Off()

                result.register_device(d, r)

    # TODO read rooms, devices and their locations from the database
    return result


def do_device_list(smart_house: SmartHouse):
    print("Listing Devices...")
    idx = 0
    for d in smart_house.get_all_devices():
        print(f"{idx}: {d}")
        idx += 1


def do_room_list(smart_house: SmartHouse):
    print("Listing Rooms...")
    idx = 0
    for r in smart_house.get_all_rooms():
        print(f"{idx}: {r}")
        idx += 1


def do_find(smart_house: SmartHouse):
    print("Please enter serial no: ")
    serial_no = input()
    device = smart_house.find_device_by_serial_no(serial_no)
    if device:
        devices = smart_house.get_all_devices()
        rooms = smart_house.get_all_rooms()
        room = smart_house.get_room_with_device(device)
        device_idx = devices.index(device)
        room_idx = rooms.index(room)
        print(f"Device No {device_idx}:")
        print(device)
        print(f"is located in room No {room_idx}:")
        print(room)
    else:
        print(f"Could not locate device with serial no {serial_no}")


def do_move(smart_house):
    devices = smart_house.get_all_devices()
    rooms = smart_house.get_all_rooms()
    print("Please choose device:")
    device_id = input()
    device = None
    if device_id.isdigit():
        device = devices[int(device_id)]
    else:
        device = smart_house.find_device_by_serial_no(device_id)
    if device:
        print("Please choose target room")
        room_id = input()
        if room_id.isdigit() and rooms[int(room_id)]:
            to_room = rooms[int(room_id)]
            from_room = smart_house.get_room_with_device(device)
            smart_house.move_device(device, from_room, to_room)
        else:
            print(f"Room with no {room_id} does not exist!")
    else:
        print(f"Device wit id '{device_id}' does not exist")


def main(smart_house: SmartHouse):
    print("************ Smart House Control *****************")
    print(f"No of Rooms:       {smart_house.get_no_of_rooms()}")
    print(f"Total Area:        {smart_house.get_total_area()}")
    print(f"Connected Devices: {smart_house.get_no_of_devices()} ({smart_house.get_no_of_sensors()} Sensors | {smart_house.get_no_of_actuators()} Actuators)")
    print("**************************************************")
    print()
    print("Management Interface v.0.1")
    while (True):
        print()
        print("Please select one of the following options:")
        print("- List all devices in the house (l)")
        print("- List all rooms in the house (r) ")
        print("- Find a device via its serial number (f)")
        print("- Move a device from one room to another (m)")
        print("- Quit (q)")
        char = input()
        if char == "l":
            do_device_list(smart_house)
        elif char == "r":
            do_room_list(smart_house)
        elif char == "f":
            do_find(smart_house)
        elif char == "m":
            do_move(smart_house)
        elif char == "q":
            break
        else:
            print(f"Error! Could not interpret input '{char}'!")


if __name__ == '__main__':
    #house = build_demo_house()
    from pathlib import Path
    file_path = str(Path(__file__).parent.absolute()) + "/db.sqlite"
    p = SmartHousePersistence(file_path)
    house = load_demo_house(p)
    main(house)
