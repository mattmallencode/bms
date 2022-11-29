from time import time
import config

time_since_last_soc_calculation: time = time()
battery_percentage: float
functional_capacity: float
functional_capacity = config.CAPACITY * config.lifespan

def time_till_full(charger) -> float:
    """
    Returns the time (in hours) until the battery is fully charged from its current battery discharged
    """
    curr_time = time()
    ttf_from_empty = 100 / ((config.chargepercent - config.last_soc_ttf) / (curr_time - config.time_of_last_ttf))
    config.time_of_last_ttf = curr_time
    ttf = ttf_from_empty * ((100 - config.chargepercent)/100)
    config.ttf = ttf / 3600
    config.last_soc_ttf = config.chargepercent
    return ttf 
  

def time_till_empty(phone) -> float:
    """
    Returns the time (in hours) until the battery is fully discharged from its current battery percentage
    """
    functional_capacity = config.CAPACITY * config.lifespan
    tte_from_full = (functional_capacity/1000) / phone.power_draw
    tte = tte_from_full * (config.chargepercent/100)
    config.tte = tte
    return tte


def state_of_charge(charger, phone) -> float:
    """
    Returns the current battery percentage 

    Reference for SoC calculation: https://www.batterydesign.net/soc-estimation-by-coulomb-counting/
    """

    if phone.is_charging:
        i = charger.report_current()
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
    if phone._powered_on:
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
    else:
        soc = config.chargepercent
    return soc

def adjust_lifespan(dif_in_soc: float) -> float:
    ''' 
    Adjusts the lifespan of the battery according to how many full charge cycles it has gone through.

    A lithium ion battery retains 80% of its original capacity after 500 charge cycles.
    So, this means that per charge cycle the capacity should reduce by 0.04 percent per charge cycle or 0.0004% for every 1% of discharge.
    The above is taken from Apple (will reference properly later).

    dif_in_soc -- the difference in SoC before discharge was called, and after discharge was called.

    Returns: the adjusted lifespan of the battery.
    '''
    config.lifespan -= ((0.0004 * dif_in_soc) / 100)