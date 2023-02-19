from devices import *
from typing import List, Optional


class Room:
    """Representerer et rom i en etasje i ett hus.
        Et rom har et areal og det kan gis et kort navn.
        På et romm kan også registreres smarte enheter."""

    def __init__(self, area: float, name: str = None):
        self.area = area
        self.name = name
        self.devices: list[Device] = []

    def __repr__(self):
        return f"{self.name} ({self.area} m^2)"


class Floor:
    """Representerer en etasje i ett hus.
        En etasje har et entydig nummer og består av flere rom."""

    def __init__(self, floor_no: int):
        self.floor_no = floor_no
        self.rooms: list[Room] = []


class SmartHouse:
    """Den sentrale klasse i et smart hus system.
        Den forvalter etasjer, rom og enheter.
        Også styres alle enheter sentralt herifra."""

    def __init__(self):
        self.floors: list[Floor] = []

    def create_floor(self) -> Floor:
        """Legger til en etasje og gi den tilbake som objekt.
            Denne metoden ble kalt i initialiseringsfasen når
            strukturen av huset bygges opp-."""
        floor = Floor(len(self.floors))
        self.floors.append(floor)
        return floor

    def create_room(self, floor_no: int, area: float, name: str = None) -> Room:
        """Legger til et rom i en etasje og gi den tilbake som objekt.
            Denne metoden ble kalt i initialiseringsfasen når
            strukturen av huset bygges opp-."""
        room = Room(area, name)
        self.floors[floor_no - 1].rooms.append(room)
        return room

    def get_no_of_rooms(self) -> int:
        """Gir tilbake antall rom i huset som heltall"""
        return len(self.get_all_rooms())

    def get_all_devices(self) -> List[Device]:
        """Gir tilbake en liste med alle enheter som er registrert i huset."""

        devices: list[Device] = []
        for room in self.get_all_rooms():
            devices += room.devices

        return devices

    def get_all_rooms(self) -> List[Room]:
        """Gir tilbake en liste med alle rom i huset."""
        rooms: list[rooms] = []
        for floor in self.floors:
            rooms += floor.rooms
        return rooms

    def get_total_area(self) -> float:
        """Regner ut det totale arealet av huset."""
        area: float = 0
        for room in self.get_all_rooms():
            area += room.area

        return area

    def register_device(self, device: Device, room: Room):
        """Registrerer en enhet i et gitt rom."""
        room.devices.append(device)
        return 

    def get_no_of_devices(self) -> int:
        """Gir tilbake antall registrerte enheter i huset."""
        return len(self.get_all_devices())

    def get_no_of_sensors(self) -> int:
        """Git tilbake antall av registrerte sensorer i huset."""
        count = 0
        for device in self.get_all_devices():
            if isinstance(device, Sensor):
                        count += 1
        return count

    def get_no_of_actuators(self) -> int:
        """Git tilbake antall av registrerte aktuatorer i huset."""

        count = 0
        for device in self.get_all_devices():
            if isinstance(device, Actuator):
                        count += 1
        return count

    def move_device(self, device: Device, from_room: Room, to_room: Room):
        """Flytter en enhet fra et gitt romm til et annet."""
        if device not in from_room.devices:
            return
        
        to_room.devices.append(device)
        from_room.devices.remove(device)

        return

    def find_device_by_serial_no(self, serial_no: str) -> Optional[Device]:
        """Prøver å finne en enhet blant de registrerte enhetene ved å
        søke opp dens serienummer."""

        for device in self.get_all_devices():
            if device.serial_no == serial_no:
                return device
        return 

    def get_room_with_device(self, device: Device) -> Optional[Room]:
        """Gir tilbake rommet der en gitt enhet er regitrert."""
        for room in self.get_all_rooms():
            if device in room.devices:
                return room
        return

    def get_all_devices_in_room(self, room: Room) -> List[Device]:
        """Gir tilbake en liste med alle enheter som er registrert på rommet."""
        return room.devices

    def turn_on_lights_in_room(self, room: Room):
        """Slår på alle enheter av type 'Smart Lys' i et gitt rom."""
        for device in room.devices:
            if device.Type == "Smart Lys":
                device.On()
        return

    def turn_off_lights_in_room(self, room: Room):
        """Slår av alle enheter av type 'Smart Lys' i et gitt rom."""
        for device in room.devices:
            if device.Type == "Smart Lys":
                device.Off()
        return 

    def get_temperature_in_room(self, room: Room) -> Optional[float]:
        """Prøver å finne ut temperaturen i et gitt rom ved å finne
        enheter av type 'Temperatursensor' der og gi tilake verdien som kommatall."""
        for device in room.devices:
            if device.Type == "Temperatursensor":
                return device.getLast()
        return

    def set_temperature_in_room(self, room: Room, temperature: float):
        """Prøver å sette temperaturen i et gitt rom ved å sette alle aktuatorer
        som kan påvirke temperatur ('Paneloven', 'Varmepumpe', ...) til ønsket
        temperatur."""
        for device in room.devices:
            if device.Type == "Paneloven" or device.Type == "Varmepumpe" or device.Type == "Gulvvarmepanel":
                device.value = temperature
                device.On()

        return 