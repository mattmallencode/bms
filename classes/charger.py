from typing import Type
from classes.battery import Battery
from classes.powerbrick import PowerBrick

class Charger:
    def __init__(self, battery: Type[Battery], powerbrick:Type[PowerBrick]):
        self._battery = battery
        self._powerbrick = powerbrick
        self._charge_setting = None
        self._c_rate = None
        
    def _get_charge_setting(self) -> str:
        return self._charge_setting

    def _set_charge_setting(self, setting) -> None:
        self._charge_setting = setting

    def report_temperature(self) -> float:
        return self._battery.temperature
    
    def report_voltage(self) -> float:
        return self._battery.voltage

    def report_current(self) -> float:
        return self._battery.current
    
    def report_resistance(self) -> float:
        return self._battery.resistance

    def report_charge_left(self) -> float:
        return self._battery.charge_left

    def _get_c_rate(self) -> float:
        return self._c_rate
    
    def _set_c_rate(self, rate) -> None:
        self._c_rate = rate
        
        
    charge_setting = property(_get_charge_setting, _set_charge_setting)
    c_rate = property(_get_c_rate, _set_c_rate)