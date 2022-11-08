from typing import Type
from classes.battery import Battery
from classes.powerbrick import PowerBrick
#import the time 
import time

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

    def report_functional_capacity(self) -> float:
        return self._battery.functional_capacity

    def _get_c_rate(self) -> float:
        return self._c_rate
    
    def _set_c_rate(self, rate) -> None:
        self._c_rate = rate
        
        
    charge_setting = property(_get_charge_setting, _set_charge_setting)
    c_rate = property(_get_c_rate, _set_c_rate)

    def affect_of_charging_the_battery(self) -> None:
        # Time for the first time.
        if self._battery._time == None:
            current_time = time.time()
            self.time = current_time
            self.time_last_changed = current_time
        
        # If the charge setting is "trickle" alter the variables based on the trickle charge.
        if self._charge_setting == "trickle":
            # Taking the amount of time has passed since the last charge state.
            # Assume it has been charging in trickle charge for that length of time.
            # Modify the variables accordingly 
            time_in_trickle_charge = self.time - self.time_last_changed
            # apply the formulas to the varibles for the duration that they were affected

            # the voltage
            voltage_max = VOLTAGE_MAX
            # Apply the voltage formula for trickle charge
            new_voltage = (voltage_max / 1000) * time_in_trickle_charge
            self.voltage = new_voltage
            # The current is 0 in trickle charge
            self.current = 0.0 