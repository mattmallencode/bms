from typing import Type
from classes.battery import Battery
from classes.powerbrick import PowerBrick
#import the time 
from time import time
# Import all from config.py
import config 
# Import math
import math

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

        self._current_time = time.time()


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

    def _get_c_rate(self) -> float:
        return self._c_rate
    
    def _set_c_rate(self, rate) -> None:
        self._c_rate = rate
        
        
    charge_setting = property(_get_charge_setting, _set_charge_setting)
    c_rate = property(_get_c_rate, _set_c_rate)

    def trickle_charge(self):
        ''' This is the function that calculates the voltage and current of the battery 
            For the duration of time the battery spent in trickle charge.'''
        # Time spent in trickle charge = our batteries current time - the last time the function was called.
        time_in_trickle_charge = self._battery.time - self._battery.time_last_changed
        # Apply the formula for calculating voltage and current.
        # the maximum voltage possible.
        voltage_max = self._powerbrick.voltage
        # Apply the voltage formula for trickle charge
        new_voltage = (voltage_max / 1000) * time_in_trickle_charge
        self._battery.voltage = new_voltage
        # The current is 1/100 of the normal current in trickle charge
        self._battery.current = self._powerbrick.current/100 
        # set the last time the function was called to the curretn time for when the charge_battery() function is called next
        self._battery.time_last_changed = self._battery.time

    def constant_current(self):
        ''' This is the function that calculates the voltage and current of the battery 
            For the duration of time the battery spent in the constant current charge method.''' 
        time_in_constant_current = self._battery.time - self._battery.time_last_changed
        print(time_in_constant_current)
        # Apply the voltage formula for constant current
        new_voltage = (1.0 / config.CHARGE_C) * time_in_constant_current ** 2
        self._battery.voltage = new_voltage
        # Current
        self._battery.current = config.CHARGE_C
        self._battery.time_last_changed = self._battery.time
    
    def constant_voltage(self):
        ''' This is the function that calculates the voltage and current of the battery 
            For the duration of time the battery spent in the constant voltage charge method.'''
        time_in_constant_voltage = self._battery.time - self._battery.time_last_changed
        # Apply the voltage formula for constant voltage
        self._battery.voltage = self._powerbrick.voltage
        # Apply the current formula for constant voltage
        self._battery.current = config.CHARGE_C * (math.cos(time_in_constant_voltage / config.CHARGE_C) + config.CHARGE_C)
        self._battery.time_last_changed = self._battery.time
        

    def charge_battery(self) -> None:
        ''' Charging the battery will affect the variables within the battery. 
        In this case it is current and voltage. The varibales are altered differently based on the charge state.
        '''
        # Time for the first time.
        if self._battery._time == None:
            self._current_time = time()
            self._battery.time = self._current_time
            self._battery.time_last_changed = self._current_time
        else:
            # A previous time exists
            self._current_time = time()
            self._battery.time = self._current_time
        # If the charge setting is "trickle" alter the variables based on the trickle charge.
        if self._charge_setting == "trickle":
            self.trickle_charge()
        # If the charge setting is "constant_current" alter the variables based on the constant current.
        elif self._charge_setting == "constant_current":
            self.constant_current()
        # If the charge setting is "constant_voltage" alter the variables based on the constant voltage.
        else:
            self.constant_voltage()
        
        
