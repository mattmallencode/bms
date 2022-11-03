# Importing Type so that we can type hint custom classes.
from typing import Type
# Importing the Charger class
from classes.charger import Charger
# Importing the Phone class
from classes.phone import Phone

from classes.battery import Battery
# The optimum voltage for this battery, should be trended towards to minimize battery degradation.
VOLTAGE_NORM: float
# At this voltage the battery is dead, trending towards this voltage indicates a lower capacity.
VOLTAGE_MIN: float
# If voltage trends towards this value, it leads to degradation.
VOLTAGE_MAX: float
# Max rate of charge.
CHARGE_C: float
# Max rate of discharge.
DISCHARGE_C: float
# The temperature at which the battery will keep increasing in temperature and go on fire.
THERMAL_RUNAWAY: float
# The battery's status, either dead or alive.
BATTERY_ALIVE: bool
# The capacity of the battery.
CAPACITY: float



def decide_charge_mode(charger: Type[Charger]) -> None:
    '''
    Function to set the charging mode of the Charger based on various parameters e.g. voltage_max, voltage_min.

    charger -- the charger we want to update the charge mode of.
    '''
    # Variable to keep track of the Charger's setting.
    charging_mode: str
    # Variable to keep track of the reported voltage of the battery.
    battery_voltage: float
    # Variable to keep track of the reported current of the battery.
    battery_current: float
    # Set charging_mode to the Charger's current setting.
    charging_mode = charger.charging_mode
    # Ask the charger to report the battery's voltage.
    battery_voltage = charger.report_voltage()
    # Ask the charger to report the battery's current.
    battery_current = charger.report_current()
    # If the charger is in CC mode, then we should check if it needs to change to CV.
    if charging_mode == "constant_current":
        # If the voltage has gone over the rated max, we should switch to CV.
        if battery_voltage >= VOLTAGE_MAX:
            charging_mode = "constant_voltage"
        # If the voltage hasn't gone over the rated max, stay in CV mode and return.
        return
    # If the charger is in CV mode, then we should check if it needs to change to trickle.
    if charging_mode == "constant_voltage":
        # If the battery has reached its capacity we should switch to trickle charge. We don't return regardless here because if its trickle we should enter the "start" flow i.e. check if the voltage has reahced min,
        if battery_current >= CAPACITY:
            charging_mode = "trickle charge"
        # If the battery hasn't reached capacity we should stay in CV mode and return.
        else:
            return
    # If the voltage has reached is lower than its rated minimum than we should enter trickle charfge mode.
    if battery_voltage < VOLTAGE_MIN:
        charger.charging_mode = "trickle"
    # If the battery has reached its rated minimum then we should leave chickle charge mode.
    else: 
        # If the battery is less than its maximum rated voltage, then enter CC mode.
        if battery_voltage < VOLTAGE_MAX:
            charger.charging_mode = "constant_current"
        # If the battery has reached its maximum rated voltage then we should enter CV mode.
        else:
            charger.charging_mode = "constant_voltage"


def discharge(battery: Type[Battery], phone: Type[Phone], time_passed: float) -> float:
    '''
    Function to draw charge from the battery based on the power draw of the phone (GUI).

    phone -- the phone the BMS is managing the battery of.
    '''
    # Discharge the battery by the power draw times the time_passed.
    battery.voltage -= phone.power_draw * time_passed