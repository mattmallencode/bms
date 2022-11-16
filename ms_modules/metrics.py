from time import time
import config

time_since_last_soc_calculation: time = time()
battery_percentage: float
functional_capacity: float
functional_capacity = config.CAPACITY * config.lifespan

def time_till_full(charger) -> float:
    """
    time_till_full returns the time (in hours) until the battery is fully charged from its current battery discharged
    """
    functional_capacity = config.CAPACITY * config.lifespan
    ttf_from_empty = (functional_capacity/1000) / charger.report_current()
    ttf = ttf_from_empty * ((100 - config.chargepercent)/100)
    config.ttf = ttf
    return ttf 
  

def time_till_empty(phone) -> float:
    """
    time_till_empty returns the time (in hours) until the battery is fully discharged from its current battery percentage
    """
    functional_capacity = config.CAPACITY * config.lifespan
    tte_from_full = (functional_capacity/1000) / phone.power_draw
    tte = tte_from_full * (config.chargepercent/100)
    config.tte = tte
    return tte


def state_of_charge(charger, phone) -> float:
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
    time_step = time_now - config.time_since_last_soc_calculation
    # updates the time since the last soc calculation to the current time
    config.time_since_last_soc_calculation = time_now
    # calculates the state of charge
    functional_capacity = config.CAPACITY * config.lifespan
    soc = config.chargepercent + ((i/(functional_capacity / 1000)) * time_step)
    # sets the battery percentage equal to the newly calculated battery percentage
    config.chargepercent = soc
    
    return soc