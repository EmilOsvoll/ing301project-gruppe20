<<<<<<< Updated upstream
import json 
f = open('dev.json')
devs = json.load(f)


class Device:
=======
from typing import List, Optional
from datetime import time, date
import database



class Device:

    def __init__(self, Nr: int, Type: str, Producer: str, Name: str, Serial_no: str):
        self.Nr = Nr
        self.Type = Type
        self.Produer = Producer
        self.Name = Name
        self.serial_no = Serial_no
        self.state = False    
>>>>>>> Stashed changes

    def __init__(self): 
        self.devices = devs



class Sensor(Device): 
    def __init__(self):
        self.sensors = [] 

    def add_sensors(self, devices):
        for i in devices['dev_type']: 
            if i == "sensor" or "aktuator & sensor": 
                print(i)
                self.sensors.append(i)



class Actuator(Device): 

    def __init__(self): 
        self.actuators = []

    def add_actuators(self, devices):
        for i in devices['dev_type']: 
            if i == "actuator" or "aktuator & sensor": 
                self.actuators.append(i)





# TODO! Her skal du utvikle din egen design av en klassestruktur med enheter og deres funkjsoner!