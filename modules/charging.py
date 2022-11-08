# Importing Type so that we can type hint custom classes.
from typing import Type
# Importing the Charger class
from classes.charger import Charger
# Need the datetime module to appropriately discharge the battery.
from datetime import datetime
# Importing the Battery class from the battery.py folder
from classes.battery import Battery
# Importing the Phone class
from classes.phone import Phone
# Import the time class, we'll need it for the discharge function.
from time import time
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
# The original capacity of the battery.
CAPACITY = 4352
# The threshold of the current when battery is fully charged
THRESHOLD: float


def decide_charge_mode(charger: Type[Charger]) -> None:
    '''
    Function to set the charging mode of the Charger based on various parameters e.g. voltage_max, voltage_min.

    charger -- the charger we want to update the charge mode of.
    '''
    setting: str
    battery: Type[Battery]
    battery = charger.battery

    if battery.voltage < VOLTAGE_MIN:
        setting = "trickle"
    else:
        if battery.voltage < VOLTAGE_MAX:
            setting = "constant_current"
        elif battery.voltage >= VOLTAGE_MAX:
            setting = "constant_voltage"
            if battery.current <= THRESHOLD:
                setting = "trickle"

    charger.charge_setting = setting
    print(CAPACITY)


def discharge(battery: Type[Battery], phone: Type[Phone], last_time_discharged: float) -> float:
    '''
    Function to draw charge from the battery based on the power draw of the phone (GUI).

    battery -- the battery the BMS is managing.
    phone -- the phone the BMS is managing the battery of.
    last_time_discharged -- the last time this function was called.

    Returns the new time stanp to be passed as "last_time_discharged" the next time discharge is called.
    '''
    # Discharge the battery by the power draw times the time_passed.
    new_last_time = time.time()
    battery.voltage -= phone.power_draw * \
        (last_time_discharged - new_last_time())
    return new_last_time
