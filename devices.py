import json 
f = open('dev.json')



class Device:

    def __init__(self): 
        self.devices = json.load(f)



    class Sensor: 
        
        def __init__(self):
            self.sensors = [] 

        def add_sensors(self, devices):
            for i in devices['dev_type']: 
                if i == "sensor" or "aktuator & sensor": 
                    print(i)
                    self.sensors.append(i)



    class Actuator: 

        def __init__(self): 
            self.actuators = []

        def add_actuators(self, devices):
            for i in devices['dev_type']: 
                if i == "actuator" or "aktuator & sensor": 
                    self.actuators.append(i)





# TODO! Her skal du utvikle din egen design av en klassestruktur med enheter og deres funkjsoner!