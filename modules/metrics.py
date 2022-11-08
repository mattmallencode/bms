from time import time
from typing import Type
from classes.charger import Charger
from classes.phone import Phone

battery_percentage: float
time_since_last_soc_calculation: time

# calculates ttf from the present battery charge status
def time_till_full(charger: Type[Charger], phone: Type[Phone]) -> float:
    # ttf_from_empty is how long it would take to charge battery from 0% - 100% assuming the current stays the same 
    # example: 5000 mAh/1000 mA = 5 hours till full from 0% 
    ttf_from_empty = charger.report_charge_left() / charger.report_current()
    ttf = ttf_from_empty * (100 - battery_percentage)
    return ttf 
   
# calculates tte from the present battery charge status
def time_till_empty(charger: Type[Charger], phone: Type[Phone]) -> float:
    tte_from_full = charger.report_charge_left() / phone.power_draw
    tte = tte_from_full * battery_percentage
    return tte

# SoC aka State of Charge calculates the battery percentage at time t
# variable i is dependent on if battery is charging or discharging
# time_step is the time interval between the last SoC calculation at t-1 and the current SoC calculation at time t
# Reference for SoC calculation: https://www.batterydesign.net/soc-estimation-by-coulomb-counting/
def state_of_charge(charger: Type[Charger], phone:Type[Phone]) -> float:
    if phone.is_charging:
        i = charger.report_current()
    else:
        i = phone.power_draw

    time_now = time.time()
    time_step = time_now - time_since_last_soc_calculation
    time_since_last_soc_calculation = time_now

    soc = battery_percentage + ((i/charger.report_charge_left()) * time_step)
    battery_percentage = soc
    return soc

