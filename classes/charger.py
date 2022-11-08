from typing import Type

from battery import Battery
from powerbrick import PowerBrick

class Charger:
    def __init__(self, battery: Type[Battery], powerbrick:Type[PowerBrick]):
        """
        Charger object for a battery that charges the battery in a safe manor

        Satisfies requirement 1: Monitor Battery State

        battery -- the battery whoes 'sensors' we want to read
        powerbrick -- the power supply that provides the charge that is passed into the battery in a controlled manor
        """
        self._battery = battery
        self._powerbrick = powerbrick
        

        self._charge_setting = None
        # c rate should be assigned from the config.py
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

    def report_functional_capacity(self) -> float:
        return self._battery.functional_capacity

    def _get_c_rate(self) -> float:
        return self._c_rate
    
    def _set_c_rate(self, rate) -> None:
        self._c_rate = rate
        
        
    charge_setting = property(_get_charge_setting, _set_charge_setting)
    c_rate = property(_get_c_rate, _set_c_rate)