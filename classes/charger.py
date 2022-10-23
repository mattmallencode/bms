from typing import Type
from classes.battery import Battery

class Charger:
    def __init__():
        pass

    def _get_battery(battery: Type[Battery]):
        return battery

    battery = property(_get_battery)