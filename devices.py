import json 
f = open('dev.json')



class Device:

    def __init__(self): 
        self.devices = json.load(f)



    class Sensor: 
        
        def __init__(self):
            self.sensors = [] 


        def add_sensors(self, sensors): 




    class Actuator: 

        def __init__(self): 
            self.actuators = []





# TODO! Her skal du utvikle din egen design av en klassestruktur med enheter og deres funkjsoner!