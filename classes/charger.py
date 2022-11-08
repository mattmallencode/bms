from typing import Type
from classes.battery import Battery
from classes.powerbrick import PowerBrick

class Charger:
    def __init__(self, battery: Type[Battery], powerbrick:Type[PowerBrick]):
        self._battery = battery
        self._powerbrick = powerbrick
        self._charge_setting = None
        
    def _get_charge_setting(self):
        return self._charge_setting

    def _set_charge_setting(self, setting):
        self._charge_setting = setting

    def report_temperature(self) -> float:
        return self.battery.temperature
    
    def report_voltage(self) -> float:
        return self.battery.voltage

    def report_current(self) -> float:
        return self.battery.current
    
    def report_resistance(self) -> float:
        return self.battery.resistance
        
    charge_setting = property(_get_charge_setting, _set_charge_setting)