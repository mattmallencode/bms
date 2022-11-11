from time import time
import config

time_since_last_soc_calculation: time
battery_percentage: float
functional_capacity: float
functional_capacity = config.CAPACITY * config.lifespan

def time_till_full(charger, battery_percentage, functional_capacity) -> float:
    """
    time_till_full returns the time (in hours) until the battery is fully charged from its current battery discharged
    """
    ttf_from_empty = functional_capacity / charger.report_current()
    ttf = ttf_from_empty * ((100 - battery_percentage)/100)
    return ttf 
  

def time_till_empty(charger, phone, battery_percentage, functional_capacity) -> float:
    """
    time_till_empty returns the time (in hours) until the battery is fully discharged from its current battery percentage
    """
    tte_from_full = functional_capacity / phone.power_draw
    tte = tte_from_full * (battery_percentage/100)
    return tte


def state_of_charge(charger, phone, battery_percentage, time_since_last_soc_calculation, functional_capacity) -> float:
    """
    state_of_charge returns the current battery percentage 

    Reference for SoC calculation: https://www.batterydesign.net/soc-estimation-by-coulomb-counting/
    """

    if phone.is_charging:
        i = charger.report_current()
    else:
        i = -phone.power_draw

    # gets current time t
    time_now = time()
    #time_step is the time interval between the last SoC calculation at t-1 and the current SoC calculation at time t
    time_step = time_now - time_since_last_soc_calculation
    # updates the time since the last soc calculation to the current time
    time_since_last_soc_calculation = time_now
    # calculates the state of charge
    soc = battery_percentage + ((i/functional_capacity) * time_step)
    # sets the battery percentage equal to the newly calculated battery percentage
    config.battery_percentage = soc

    return soc