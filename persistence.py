from sqlite3 import Connection
from devices import Device
#from smarthouse import Room
from typing import Optional, List, Dict, Tuple
from datetime import date, datetime


class SmartHousePersistence:

    def __init__(self, db_file: str):
        self.db_file = db_file
        self.connection = Connection(db_file)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.rollback()
        self.connection.close()

    def save(self):
        self.connection.commit()

    def reconnect(self):
        self.connection.close()
        self.connection = Connection(self.db_file)
        self.cursor = self.connection.cursor()

    def check_tables(self) -> bool:
        self.cursor.execute("SELECT name FROM sqlite_schema WHERE type = 'table';")
        result = set()
        for row in self.cursor.fetchall():
            result.add(row[0])
        return 'rooms' in result and 'devices' in result and 'measurements' in result


class SmartHouseAnalytics:

    def __init__(self, persistence: SmartHousePersistence):
        self.persistence = persistence

    def get_most_recent_sensor_reading(self, sensor: Device) -> Optional[float]:
        """
        Retrieves the most recent (i.e. current) value reading for the given
        sensor device.
        Function may return None if the given device is an actuator or
        if there are no sensor values for the given device recorded in the database.
        """

        cmd = f"""SELECT value FROM measurements m
                inner join devices d 
                on m.device = d.id 
                where d.id = {sensor.Nr}
                ORDER BY DATETIME(m.time_stamp) DESC  
                LIMIT 1;"""
        
        self.persistence.cursor.execute(cmd)
        ans = self.persistence.cursor.fetchone()
        if ans is not None:
            return ans[0]

    def get_coldest_room(self) -> str:
        """
        Finds the room, which has the lowest temperature on average.
        """
        cmd = """SELECT r.name from rooms r 
                inner join devices d on d.room = r.id 
                inner join measurements m on m.device = d.id 
                WHERE d."type" = "Temperatursensor"
                GROUP BY r.id
                ORDER BY AVG(m.value) ASC
                LIMIT 1;"""
        
        self.persistence.cursor.execute(cmd)
        ans = self.persistence.cursor.fetchone()
        return ans[0] 


    def get_sensor_readings_in_timespan(self, sensor: Device, from_ts: datetime, to_ts: datetime) -> List[float]:
        """
        Returns a list of sensor measurements (float values) for the given device in the given timespan.
        """
        cmd = f"""SELECT m.value FROM devices d
                inner join measurements m 
                on d.id = m.device 
                WHERE d.id = {sensor.Nr} AND DATETIME(m.time_stamp) > DATETIME("{from_ts.isoformat()}")  AND DATETIME(m.time_stamp) < DATETIME("{to_ts.isoformat()}")
                ORDER BY m.time_stamp ASC;"""
        
        self.persistence.cursor.execute(cmd)
        tuple = self.persistence.cursor.fetchall()
        return [item for t in tuple for item in t]

    def describe_temperature_in_rooms(self) -> Dict[str, Tuple[float, float, float]]:
        """
        Returns a dictionary where the key are room names and the values are triples
        containing three floating point numbers:
        - The first component [index=0] being the _minimum_ temperature of the room.
        - The second component [index=1] being the _maximum_ temperature of the room.
        - The third component [index=2] being the _average_ temperature of the room.

        This function can be seen as a simplified version of the DataFrame.describe()
        function that exists in Pandas:
        https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html?highlight=describe
        """
        cmd = """SELECT r.name, MIN(m.value), MAX(m.value), AVG(m.value)  from rooms r 
                INNER JOIN devices d ON r.id = d.room
                INNER JOIN measurements m ON d.id = m.device
                WHERE d."type" ="Temperatursensor" 
                GROUP BY r.id;
                """
        ans: dict[str, Tuple[float, float, float]] = dict()
        self.persistence.cursor.execute(cmd)
        for row in self.persistence.cursor.fetchall():
            ans[row[0]] = (float(row[1]), float(row[2]), float(row[3]))
        
        return ans

    #def get_hours_when_humidity_above_average(self, room: Room, day: date) -> List[int]:
    #    """
    #    This function determines during which hours of the given day
    #    there were more than three measurements in that hour having a humidity measurement that is above
    #    the average recorded humidity in that room at that particular time.
    #    The result is a (possibly empty) list of number respresenting hours [0-23].
    #    """
    #    return NotImplemented()