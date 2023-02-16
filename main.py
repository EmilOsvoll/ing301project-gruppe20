from smarthouse import SmartHouse
from devices import *


def build_demo_house() -> SmartHouse:
    house = SmartHouse()
    # TODO! her skal du legge inn etasjer, rom og enheter som at resultatet tilsvarer demo huset!
    #Make both floors
    first_floor =           house.create_floor()
    second_floor =          house.create_floor()
    #Add rooms to floor 1
    garage =                house.create_room(1, 19,    'Garage')
    entrance =              house.create_room(1, 13.5,  'Entrance')
    guest_room_1 =          house.create_room(1, 8,     'Guest Room 1')
    bathroom_1 =            house.create_room(1, 6.3,   'Bathroom 1')
    livingroom_kitchen =    house.create_room(1, 39.75, 'Livingroom/Kitchen')
    #Add rooms to floor 2
    hallway =               house.create_room(2, 10,    'Hallway')
    guest_room_2 =          house.create_room(2, 8,     'Guest Room 2')
    bathroom_2 =            house.create_room(2, 9.25,  'Bathroom 2')
    office =                house.create_room(2, 11.75, 'Office')
    guest_room_3 =          house.create_room(2, 10,    'Guest Room 3')
    dressing_room =         house.create_room(2, 4,     'Dressing Room')
    master_bedroom =        house.create_room(2, 17,    'Master Bedroom')
    #Create all devices
    devices = [
        Actuator    (1,	    "Smart Lys"	            ,"Fritsch Group"	            ,"Tresom Bright 1.0"	,"f11bb4fc-ba74-49cd"),
        Actuator    (2,	    "Smart Lys"	            ,"Fritsch Group"	            ,"Alphazap 2"	        ,"480dbae8-cce7-46d7"),
        Sensor      (3,	    "Fuktighetssensor"	    ,"Bernhard-Roberts"	            ,"Andalax"	            ,"4cb686fe-6448-4cf6"),
        Actuator    (4,	    "Smart Lys"	            ,"Fritsch Group"	            ,"Alphazap 2"	        ,"6a36c71d-4f48-4eb4"),
        Actuator    (5,	    "Smart Lys"	            ,"Larkin-Nitzsche"	            ,"Quo Lux"	            ,"d01130c9-a368-42c6"),
        Actuator    (6,	    "Billader"	            ,"Jast, Hansen and Halvorson"	,"Charge It 9000"	    ,"0cae4f01-4ad9-47aa"),
        Actuator    (7,	    "Paneloven"	            ,"Hauck-DuBuque"	            ,"Voyatouch 42"	        ,"d16d84de-79f1-4f9a"),
        Sensor      (8,	    "Temperatursensor"	    ,"Moen Inc"	                    ,"Prodder Ute 1.2"	    ,"e237beec-2675-4cb0"),
        Actuator    (9,	    "Smart Lys"	            ,"Fritsch Group"	            ,"Alphazap 2"	        ,"f4db4e54-cebe-428d"),
        Actuator    (10,	"Smart Lys"	            ,"Larkin-Nitzsche"	            ,"Quo Vadis Lux"	    ,"8d09aa92-fc58-4c6)"),
        Sensor      (11,	"Strømmåler"	        ,"Kilback LLC"	                ,"Transcof Current"	    ,"c8bb5601-e850-4a80"),
        Sensor      (12,	"Temperatursensor"	    ,"Moen Inc"	                    ,"Prodder Inne 2.3"	    ,"d16d84de-79f1-4f9a"),
        Actuator    (13,	"Smart Lys"	            ,"Fritsch Group"	            ,"Alphazap 2"	        ,"390ae474-21fb-4e06"),
        Sensor      (14,	"Strømmåler"	        ,"Ward-Schaefer"	            ,"Zaam-Dox NetConnect"	,"3b06cf0f-8494-458b"),
        Actuator    (15,	"Smart Stikkontakt"	    ,"Kilback LLC"	                ,"Konklab 3"	        ,"c28b6e75-d565-4678"),
        Actuator    (16,	"Varmepumpe"	        ,"Osinski Inc"	                ,"Fintone XCX4AB"	    ,"4eca6387-0767-4e4e"),
        Sensor      (17,	"Luftkvalitetssensor"	,"Hauck-DuBuque"	            ,"Sonair Pro"	        ,"c76688cc-3692-4aa3"),
        Actuator    (18,	"Smart Stikkontakt"	    ,"Kilback LLC"	                ,"Konklab 3"	        ,"4b9050f3-0ef0-4914"),
        Actuator    (19,	"Paneloven"	            ,"Hauck-DuBuque"	            ,"Voyatouch 42"	        ,"66373954-2ddd-4807"),
        Actuator    (20,	"Smart Stikkontakt"	    ,"Kilback LLC"	                ,"Konklab 3"	        ,"1b34f6ce-94cb-4f7b"),
        Sensor      (21,	"Fuktighetssensor"	    ,"Bernhard-Roberts"	            ,"Namfix Y"	            ,"8ceb53b2-e88f-4e8c"),
        Actuator    (22,	"Luftavfukter"	        ,"Steuber-Gerlach"	            ,"Aerified 42"	        ,"ae902f8f-10b4-4738"),
        Actuator    (23,	"Gulvvarmepanel"	    ,"Steuber-Gerlach"	            ,"Temp Opp Pro 13"	    ,"42f204bf-9944-47a1"),
        Actuator    (24,	"Paneloven"	            ,"Hauck-DuBuque"	            ,"Otcom 2"	            ,"73902f8f-10b4-4738"),
        Actuator    (25,	"Smart Lys"	            ,"Fritsch Group"	            ,"Alphazap 2"	        ,"627ff5f3-f4f5-47bd"),
        Actuator    (26,	"Smart Lys"	            ,"Fritsch Group"	            ,"Alphazap 2"	        ,"ebaaadce-2d6b-4623"),
        Actuator    (27,	"Varmepumpe"	        ,"Osinski Inc"	                ,"Fintone XCX2FF"	    ,"eed2cba8-eb13-4023"),
        Sensor      (28,	"Temperatursensor"	    ,"Moen Inc"	                    ,"Prodder Inne 2.3"	    ,"481e94bd-ff50-40ea"),
        Actuator    (29,	"Smart Lys"	            ,"Fritsch Group"	            ,"Tresom Bright 1.0"	,"233064d7-028a-407f"),
        Actuator    (30,	"Smart Lys"	            ,"Fritsch Group"	            ,"Alphazap 2"	        ,"89393440-43cb-4cb5"),
        Actuator    (31,	"Paneloven"	            ,"Hauck-DuBuque"	            ,"Otcom 2"	            ,"be490f21-b9cf-4413"),
    ]
    #Assign devices to rooms.
    house.register_device(devices[4], garage)
    house.register_device(devices[5], garage)     
    
    house.register_device(devices[7], entrance)
    house.register_device(devices[8], entrance)
    house.register_device(devices[9], entrance)
    house.register_device(devices[12], entrance)
    house.register_device(devices[13], entrance)

    house.register_device(devices[3], guest_room_1)
    house.register_device(devices[6], guest_room_1)

    house.register_device(devices[2], bathroom_1)

    house.register_device(devices[0], livingroom_kitchen)
    house.register_device(devices[1], livingroom_kitchen)
    house.register_device(devices[10], livingroom_kitchen)
    house.register_device(devices[11], livingroom_kitchen)
    house.register_device(devices[14], livingroom_kitchen)
    house.register_device(devices[15], livingroom_kitchen)
    house.register_device(devices[16], livingroom_kitchen)
    house.register_device(devices[17], livingroom_kitchen)

    house.register_device(devices[18], office)
    house.register_device(devices[19], office)

    house.register_device(devices[20], bathroom_2)
    house.register_device(devices[21], bathroom_2)
    house.register_device(devices[22], bathroom_2)

    house.register_device(devices[23], guest_room_2)

    house.register_device(devices[24], master_bedroom)
    house.register_device(devices[25], master_bedroom)
    house.register_device(devices[26], master_bedroom)
    house.register_device(devices[27], master_bedroom)
    house.register_device(devices[28], master_bedroom)

    house.register_device(devices[29], dressing_room)

    house.register_device(devices[30], guest_room_3)

    #Set refrence values
    devices[2].measurements.append(Measurement(date.today, time.second, 68, '%'))
    devices[7].measurements.append(Measurement(date.today, time.second, 1.3, '°C'))
    devices[10].measurements.append(Measurement(date.today, time.second, 0, 'kWh'))
    devices[11].measurements.append(Measurement(date.today, time.second, 18.1, '°C'))
    devices[13].measurements.append(Measurement(date.today, time.second, 1.5, 'kWh'))
    devices[16].measurements.append(Measurement(date.today, time.second, 0.08, 'g/m^2'))
    devices[20].measurements.append(Measurement(date.today, time.second, 52, '%'))
    devices[27].measurements.append(Measurement(date.today, time.second, 16.1, '°C'))
    #Set values
    return house



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
    house = build_demo_house()
    main(house)
