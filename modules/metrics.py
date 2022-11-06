# calculates ttf from the present battery charge status
def time_till_full(charge_in_battery:float, current:float, charge_status:float) -> float:
    # ttf_from_empty is how long it would take to charge battery from 0% - 100% assuming the current stays the same 
    # example: 5000 mAh/1000 mA = 5 hours till full from 0% 
    ttf_from_empty = charge_in_battery / current

    ttf = ttf_from_empty * (100 - charge_status)
    return ttf 
   
# calculates tte from the present battery charge status
def time_till_empty(charge_in_battery:float, drain: float, charge_status:float) -> float:
    tte_from_full = charge_in_battery / drain
    tte = tte_from_full * charge_status
    return tte

# SoC aka State of Charge calculates the battery percentage at time t
# Battery percentage can only be estimated not measured. SoC is a measurement metric for battery percentage
# variable i is dependent on if battery is charging or discharging
# time_step is the time interval between the last SoC calculation at t-1 and the current SoC calculation at time t
# Reference for SoC calculation: https://www.batterydesign.net/soc-estimation-by-coulomb-counting/
def state_of_charge(charge_status:float, is_charging:bool, current:float, drain:float, charge_in_battery:float, time_step:float) -> float:
    if is_charging:
        i = current
    else:
        i = drain
    soc = charge_status + ((i/charge_in_battery) * time_step)
    return soc

