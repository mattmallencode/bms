from typing import Type
from classes.battery import Battery

class Charger:
    def __init__(self, battery: Type[Battery], charging_mode: str) -> None:
        self._battery = battery
        self._charging_mode = charging_mode

    def _get_battery(self) -> Type[Battery]:
        return self._battery
    
    def _get_charging_mode(self) -> str:
        return self._charging_mode
    
    def _set_charging_mode(self, charging_mode: str) -> None:
        self._charging_mode = charging_mode
    
    battery = property(_get_battery)

    charging_mode = property(_get_charging_mode, _set_charging_mode)
    
    def report_temperature(self) -> float:
        return self.battery.temperature
    
    def report_voltage(self) -> float:
        return self.battery.voltage

    def report_current(self) -> float:
        return self.battery.current
    
    def report_resistance(self) -> float:
        return self.battery.resistance