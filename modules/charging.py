# Importing Type so that we can type hint custom classes.
from typing import Type
# Importing the Charger class from the charger.py folder
from classes.charger import Charger
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
# How much the battery is currently charged.
CHARGE_STATUS: float
# The capacity of the battery.
CAPACITY: float


def decide_charge_mode(charger: Type[Charger], charge_status: float, charge_c: float, voltage_max: float, voltage_min: float) -> float:
    ''' 
    A battery can charge under specific conditions: these being curren voltage, current in  and temperture.
    The function will take into account the current volatage and current
    The maximum / min range of the voltage 
    The voltage norm
    Temperture 
    And the current charge status of the battery ie. how full or empty the battery is.
    We pass the current charge rate in as it may change depending on our systems state and demands. 
    '''
    pass


def discharge(drain: float, discharge_c: float, thermal_runaway: float, charge_status: float) -> float:
    '''
    We need to have the drain on the system so that we can estimate what our discharge rate will be 
    our current discharge rate is needed as we may alter it 
    the rate of discharge may increase the affects of thermal_runaway so we need this variable 
    And our current charge status is needed as it will affect our rate of discharge (ie low power mode at low charge levels)


    We may need more variables to account for current and volatage out of the battery but we can add them in as we develop the functions.

    I also said that we are returning float in this case as it is the rate of discharge , This may change

    The discharge function is in the charging file as they both affect each other.
    '''
    pass
