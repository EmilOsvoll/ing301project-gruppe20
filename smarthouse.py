from devices import Device
from typing import List, Optional
import json


class SmartHouse():
    """Den sentrale klasse i et smart hus system.
        Den forvalter etasjer, rom og enheter.
        Også styres alle enheter sentralt herifra."""

    h = open('house.json')
    house = json.load(h)


    def __init__(self):
        self.floors = []

    def create_floor(self) -> Floor:
        """Legger til en etasje og gi den tilbake som objekt.
            Denne metoden ble kalt i initialiseringsfasen når
            strukturen av huset bygges opp-."""

        return NotImplemented



    def create_room(self, floor_no: int, area: float, name: str = None) -> Room:
        self.floor = floor_no
        self.area = area
        self.name = name
        return Room(floor_no, area, name)


    def get_no_of_rooms(self) -> int:
        return len(Room.get_all_rooms())




    def get_all_devices(self) -> List[Device]:
        """Gir tilbake en liste med alle enheter som er registrert i huset."""
        super(Device).
        return NotImplemented

    def get_all_rooms(self) -> List[Room]:
        """Gir tilbake en liste med alle rom i huset."""
        return rooms

    def get_total_area(self) -> float:
        """Regner ut det totale arealet av huset."""
        return NotImplemented

    def register_device(self, device: Device, room: Room):
        """Registrerer en enhet i et gitt rom."""
        


        return NotImplemented

    def get_no_of_devices(self):
        """Gir tilbake antall registrerte enheter i huset."""


        return len()

    def get_no_of_sensors(self):
        """Git tilbake antall av registrerte sensorer i huset."""
        return len()

    def get_no_of_actuators(self):
        """Git tilbake antall av registrerte aktuatorer i huset."""
        return NotImplemented

    def move_device(self, device: Device, from_room: Room, to_room: Room):
        """Flytter en enhet fra et gitt romm til et annet."""
        return NotImplemented

    def find_device_by_serial_no(self, serial_no: str) -> Optional[Device]:
        """Prøver å finne en enhet blant de registrerte enhetene ved å
        søke opp dens serienummer."""
        return NotImplemented

    def get_room_with_device(self, device: Device):
        """Gir tilbake rommet der en gitt enhet er resitrert."""
        return NotImplemented

    def get_all_devices_in_room(self, room: Room) -> List[Device]:
        """Gir tilbake en liste med alle enheter som er registrert på rommet."""
        return NotImplemented

    def turn_on_lights_in_room(self, room: Room):
        """Slår på alle enheter av type 'Smart Lys' i et gitt rom."""
        return NotImplemented

    def turn_off_lights_in_room(self, room: Room):
        """Slår av alle enheter av type 'Smart Lys' i et gitt rom."""
        return NotImplemented

    def get_temperature_in_room(self, room: Room) -> Optional[float]:
        """Prøver å finne ut temperaturen i et gitt rom ved å finne
        enheter av type 'Temperatursensor' der og gi tilake verdien som kommatall."""
        return NotImplemented

    def set_temperature_in_room(self, room: Room, temperature: float):
        """Prøver å sette temperaturen i et gitt rom ved å sette alle aktuatorer
        som kan påvirke temperatur ('Paneloven', 'Varmepumpe', ...) til ønsket
        temperatur."""
        return NotImplemented
    
class Floor(SmartHouse):
    """Representerer en etasje i ett hus.
        En etasje har et entydig nummer og består av flere rom."""

    def __init__(self, floor_no: int):
        super().create_floor()
        self.floor_no = floor_no
        self.rooms = []

class Room(Floor):
    """Representerer et rom i en etasje i ett hus.
        Et rom har et areal og det kan gis et kort navn.
        På et romm kan også registreres smarte enheter."""

    def __init__(self, area: float, name: str = None):
        super().create_room()
        self.area = area
        self.name = name

    def __repr__(self):
        return f"{self.name} ({self.area} m^2)"
    
class Component:
    def __init__(self, id: int, type: str, manufacturer: str = None, component_name: str = None):
        self.id = id
        self.type = type
        self.manufacturer = manufacturer
        self.component_name = component_name
    
class Actuator(Component):
    def __init__(self, id: int, type: str, modulating: bool):
        super().__init__(id, type)
        self.modulating = modulating    # Modulating actuator means that it can be set
                                        # to a more precise state than on or off.
        self.state = None               # This must be a boolean if the actuator is
                                        # modulating. It should be set throuh a function,
                                        # not directly upon initialization.

class Sensor(Component):
    def __init__(self, id: int, type: str):
        super().__init__(id, type)
        
class Measurement(Sensor):
    def __init__(self, id: int, type: str, date, time, value: float, unit: str):
        super().__init__(id, type)
        self.date = date
        self.time = time
        self.value = value
        self.unit = unit