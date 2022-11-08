from classes.phone import Phone
from ms_modules import charging
from ms_modules.health import lifespan
from classes import charger 

"""
last_time_discharged: float = None
"""
phone = Phone(False, False, False, True, 10)

# Taking the amount of time has passed since the last charge state. # Assume it has been charging in trickle charge for that length of time.
            # Modify the variables accordingly 


"""
while True:
    if phone.power_on == True:
        if last_time_discharged is None:
            last_time_discharged = time.time()
        else:
            charging.discharge(battery, phone, last_time_discharged)
    else:
        if last_time_discharged is not None:
            charging.discharge(battery, phone, last_time_discharged)
            last_time_discharged = None
"""
