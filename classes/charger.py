from typing import Type
from classes.battery import Battery
from classes.powerbrick import PowerBrick
# import the time
from time import time
# Import all from config.py
import config
# Import math
import math


class Charger:
    def __init__(self, battery: Type[Battery], powerbrick: Type[PowerBrick]) -> None:
        """
        Charger object for a battery that charges the battery in a safe manner.

        battery -- the battery we are charging.
        powerbrick -- the power supply that provides the electricity that is passed onto the battery in a safe manner.
        """
        self._battery = battery
        self._powerbrick = powerbrick
        self._time_of_last_charge = time()

        self._charge_setting = None
        # c rate should be assigned from the config.py
        self._c_rate = None

    def _get_charge_setting(self) -> str:
        """Returns the current charge setting."""
        return self._charge_setting

    def _set_charge_setting(self, setting) -> None:
        """Updates the current charge setting."""
        self._charge_setting = setting

    def report_voltage(self) -> float:
        """Returns the voltage of the battery."""
        return self._battery._voltage

    def report_current(self) -> float:
        """Returns the current of the battery."""
        return self._battery._current
    charge_setting = property(_get_charge_setting, _set_charge_setting)

    def trickle_charge(self) -> None:
        """Charges the battery in trickle charge mode."""
        # Time spent in trickle charge = our batteries current time - the last time the function was called.
        time_in_trickle_charge = time() - self._time_of_last_charge
        self._time_of_last_charge = time()
        # Apply the formula for calculating voltage and current.
        # the maximum voltage possible.
        voltage_max = self._powerbrick.voltage
        # Apply the voltage formula for trickle charge
        voltage_in = (voltage_max / 1000) * time_in_trickle_charge
        # Accumulating the voltage over time in the battery
        self._battery.voltage = voltage_in + self._battery.voltage
        # The current is 1/100 of the normal current in trickle charge
        self._battery.current = self._powerbrick.current / 100
        # set the last time the function was called to the curretn time for when the charge_battery() function is called next

    def constant_current(self) -> None:
        """Charges the battery in constant current mode."""
        time_in_constant_current = time() - self._time_of_last_charge
        self._time_of_last_charge = time()
        # print(time_in_constant_current)
        '''# Apply the voltage formula for constant current
        voltage_in = (1.0 / config.CHARGE_C) * time_in_constant_current ** 2
        # Accumulating the voltage over time in the battery
        self._battery.voltage = voltage_in + self._battery.voltage'''
        # print(time_in_constant_current)
        capacityPercentage = (config.CAPACITY/100) * \
            (config.THRESHHOLDPRECENTAGE)
        m = (capacityPercentage/(config.CHARGE_C*config.CAPACITY))
        # print(m)
        self._battery.voltage += (m*time_in_constant_current)
        # Current
        self._battery.current = (config.CHARGE_C*time_in_constant_current)

    def constant_voltage(self) -> None:
        """Charges the battery in constant voltage mode."""
        time_in_constant_voltage = time() - self._time_of_last_charge
        self._time_of_last_charge = time()
        # print(time_in_constant_voltage)
        # Apply the current formula for constant voltage
        capacityPercentage = (config.CAPACITY/100) * \
            (100-config.THRESHHOLDPRECENTAGE)
        m = (((capacityPercentage)/(config.CHARGE_C*1000))/4000)
        # print(m)
        self._battery.current -= (m*time_in_constant_voltage)

    def charge_battery(self) -> None:
        """Calls the relevant charge function depending on the current charge setting."""
        # If the charge setting is "trickle" alter the variables based on the trickle charge.
        if self._charge_setting == "trickle":
            self.trickle_charge()
        # If the charge setting is "constant_current" alter the variables based on the constant current.
        elif self._charge_setting == "constant_current":
            self.constant_current()
        # If the charge setting is "constant_voltage" alter the variables based on the constant voltage.
        else:
            self.constant_voltage()
