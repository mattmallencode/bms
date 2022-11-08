from classes.phone import Phone
from ms_modules import charging
from ms_modules.health import lifespan

"""
last_time_discharged: float = None
"""
phone = Phone(False, False, False, True, 10)

#battery = Battery(1.0, 1.0, 1.0, 1.0)
#charger = Charger(battery)
#brick = PowerBrick(1.0, 1.0)

# we will need to reset some attribtues in battery and in MS when major events happen e.g. stopping charge, stopping discharge
# we also need to make sure that things are "finished" out when one of these major events happens -- this definitely does not make sense I'll explain in person.

# Just testing here
lifespan(10, phone, 100, 10)
print(charging.CAPACITY)



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