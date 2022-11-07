# Importing the charger function to access the charger setting.
from classes.charger import Charger
# import math module 
import math
# import the charging file
from modules import charging

#import the time 
from time import time

# Class representing the state of a battery of a phone.
class Battery:
    def __init__(self, current: float, voltage: float, temperature: float,  resistance: float, charger: type[Charger]) -> None:
        """
        Initializes an instance of the Battery class based on the arguments you pass to this constructor.

        Keyword arguments:
        current -- the current of the battery.
        voltage -- the voltage of the battery.
        temperature -- the temperature of the battery.
        resistance -- the resistance of the battery.
        """
        # Initialize instance variables based on arguments passed to the constructor.
        self._current = current
        self._voltage = voltage
        self._temperature = temperature
        self._resistance = resistance
        self._charger = charger
        # Time 
        self._time = None
        self._time_last_changed = None

    def _get_current(self) -> float:
        """Returns the current of the battery."""
        return self._current

    def _set_current(self, current) -> None:
        """Updates the current of the battery."""
        self._current = current

    def _get_voltage(self) -> float:
        """Returns the voltage of the battery."""
        return self._voltage

    def _set_voltage(self, voltage) -> None:
        """Updates the voltage of the battery."""
        self._voltage = voltage

    def _get_temperature(self) -> float:
        """Returns the temperature of the battery."""
        return self._temperature

    def _set_temperature(self, temperature) -> None:
        """Updates the temperature of the battery."""
        self._temperature = temperature
    
    def _get_resistance(self) -> float:
        return self._resistance

    def _set_resistance(self, resistance) -> None:
        """Updates the resistance of the battery."""
        self._resistance = resistance
   
    def _get_charger(self) -> None:
        return self._charger
    
    def _get_time(self) -> float:
        return self._time

    def _set_time(self, time) -> float:
        self._time = time

    def _get_time_last_changed(self) -> float:
        return self._time_last_changed
    
    def _set_time_last_changed(self, time_last_changed) -> float:
        self._time_last_changed = time_last_changed
    
    # Assign all of the getters of setters to class properties.
    # This means private instance variables can be accessed "directly" by using the getters and setters as an interface.
    # E.g. my_battery.is_charging = False calls _set_is_charging(False) under the hood.
    current = property(_get_current, _set_current)
    voltage = property(_get_voltage, _set_voltage)
    temperature = property(_get_temperature, _set_temperature)
    resistance = property(_get_resistance, _set_resistance)
    charger = property(_get_charger)
    time = property(_get_time, _set_time)
    time_last_changed = property(_get_time_last_changed, _set_time_last_changed)

    # The function reponsible for simulating the affects of charging the battery.
    def affect_of_charging_the_battery(self) -> None:
        # create a time stamp
        # If the time is None it means this is the first time it has beeen called.
        if self._time == None:
            current_time = time.time()
            self.time = current_time
            self.time_last_changed = current_time
        
        # If the charge setting is "trickle" alter the variables based on the trickle charge.
        if self._charger.charge_setting == "trickle":
            # Taking the amount of time has passed since the last charge state.
            # Assume it has been charging in trickle charge for that length of time.
            # Modify the variables accordingly 
            time_in_trickle_charge = self.time - self.time_last_changed
            # apply the formulas to the varibles for the duration that they were affected

            # the voltage
            voltage_max = charging.VOLTAGE_MAX
            # Apply the voltage formula for trickle charge
            new_voltage = (voltage_max / 1000) * time_in_trickle_charge
            self.voltage = new_voltage
            # The current is 0 in trickle charge
            self.current = 0.0 
            # Temperture

        # If the charge setting is "constant_current" alter the variables based on the constant current.
        elif self._charger.charge_setting == "constant_current":
            # Taking the amount of time has passed since the last charge state.
            # Assume it has been charging with constant current for that length of time.
            # Modify the variables accordingly 
            time_in_constant_current = self.time - self.time_last_changed
            # Apply the voltage formula for constant current
            new_voltage = (1.0 / charging.CHARGE_C) * time_in_constant_current ** 2
            self.voltage = new_voltage
            # Current
            self.current = charging.CHARGE_C
            # Temperture


        # If it is neither of those that means it is "constant_voltage" hence we alter the variable accordingly.
        else:
            # Taking the amount of time has passed since the last charge state.
            # Assume it has been charging with constant voltage for that length of time.
            # Modify the variables accordingly 
            time_in_constant_voltage = self.time() - self.time_last_changed()
            # Apply the voltage formula for constant voltage
            # Voltage
            self.voltage = charging.VOLTAGE_MAX
            # Current
            current = charging.CHARGE_C(math.cos(time_in_constant_voltage / charging.CHARGE_C) + charging.CHARGE_C)
            self.current = current
            # Temperture

        #Once the varibales have beeen changed 
        self._time_last_changed = self._time
    