# Importing Type so that we can type hint custom classes.
from typing import Type
# Importing the Charger class
from classes.charger import Charger
# Importing the Battery class from the battery.py folder
from classes.battery import Battery
# Importing the Phone class
from classes.phone import Phone
# Import the time class, we'll need it for the discharge function.
from time import time


def decide_charge_mode(charger: Type[Charger]) -> None:
    '''
    Function to set the charging mode of the Charger based on various parameters e.g. voltage_max, voltage_min.

    Satisfies requirement 2: Determine Charge Setting

    charger -- the charger we want to update the charge mode of.

    alters the charge mode in the charger
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


def discharge(battery: Type[Battery], phone: Type[Phone], last_time_discharged: float) -> float:
    '''
    Function to draw charge from the battery based on the power draw of the phone (GUI).

    Satisfies requirement 6: Discharge

    battery -- the battery the BMS is managing.
    phone -- the phone the BMS is managing the battery of.
    last_time_discharged -- the last time this function was called.

    Returns the new time stanp to be passed as "last_time_discharged" the next time discharge is called.
    '''
    # Discharge the battery by the power draw times the time_passed.
    new_last_time = time.time()
    battery.voltage -= phone.power_draw * (last_time_discharged - new_last_time())
    return new_last_time

    # WE NEED A PHONE DEAD FUNCTION/MODE