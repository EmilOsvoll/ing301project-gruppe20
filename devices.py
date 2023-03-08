from typing import List, Optional
from datetime import time, date

class Device:
    def __init__(self, Nr: int, Type: str, Producer: str, Name: str, Serial_no: str):
        self.Nr = Nr
        self.Type = Type
        self.Produer = Producer
        self.Name = Name
        self.serial_no = Serial_no
        self.state = False    

    def On(self):
        self.state = True
        return
    
    def Off(self):
        self.state = False
        return

class Sensor(Device):
    def __init__(self, Nr: int, Type: str, Producer: str, Name: str, Serial_no: str, unit: str):
        self.measurements: list[Measurement] = []
        self.unit = unit
        super().__init__(Nr, Type, Producer, Name, Serial_no)
    
    def __repr__(self) -> str:
        last = self.measurements[-1] if len(self.measurements) > 0 else 0
        s = f"{last.value} {self.unit}"
        return f"Sensor({self.serial_no}) TYPE: {self.Type} STATUS: {s} PRODUCT DETAILS: {self.Produer} {self.Name}"

    def getLast(self) -> float:
        return self.measurements[-1].value if len(self.measurements) > 0 else 0
        

class Actuator(Device):
    def __init__(self, Nr: int, Type: str, Producer: str, Name: str, Serial_no: str):
        self.value: float = 0
        super().__init__(Nr, Type, Producer, Name, Serial_no)

    def __repr__(self) -> str:
        heater = self.Type == "Paneloven" or self.Type == "Varmepumpe" or self.Type == "Gulvvarmepanel"
        s = ''
        if self.state:
            s = f"{self.value} °C" if heater else "ON"
        else:
            s = "OFF"
        return f"Aktuator({self.serial_no}) TYPE: {self.Type} STATUS: {s} PRODUCT DETAILS: {self.Produer} {self.Name}"

class Measurement:
    def __init__(self, date: date, time: time, value: float):
        self.date = date
        self.time = time
        self.value = value
        