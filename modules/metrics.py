from time import time
from typing import Type
from classes.charger import Charger
from classes.phone import Phone

# calculates ttf from the present battery charge status
def time_till_full(charger: Type[Charger], phone: Type[Phone]) -> float:
    # ttf_from_empty is how long it would take to charge battery from 0% - 100% assuming the current stays the same 
    # example: 5000 mAh/1000 mA = 5 hours till full from 0% 
    ttf_from_empty = charger.report_functional_capacity() / charger.report_current()
    ttf = ttf_from_empty * (100 - phone.battery_percentage)
    return ttf 
   
# calculates tte from the present battery charge status
def time_till_empty(charger: Type[Charger], phone: Type[Phone]) -> float:
    tte_from_full = charger.report_functional_capacity() / phone.power_draw
    tte = tte_from_full * phone.battery_percentage
    return tte

# SoC aka State of Charge calculates the battery percentage at time t
# variable i is dependent on if battery is charging or discharging
# time_step is the time interval between the last SoC calculation at t-1 and the current SoC calculation at time t
# Reference for SoC calculation: https://www.batterydesign.net/soc-estimation-by-coulomb-counting/
def state_of_charge(charger: Type[Charger], phone: Type[Phone]) -> float:
    if phone.is_charging:
        i = charger.report_current()
    else:
        i = phone.power_draw

    time_now = time.time()
    time_step = time_now - phone.time_since_last_percentage_calculation
    phone.time_since_last_percentage_calculation = time_now

    soc = phone.battery_percentage + ((i/charger.report_functional_capacity()) * time_step)
    phone.battery_percentage = soc
    return soc

