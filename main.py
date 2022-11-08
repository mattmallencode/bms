from classes.phone import Phone
from ms_modules import charging
from ms_modules.health import lifespan
from classes.charger import Charger
from classes.battery import Battery
from classes.phone import Phone
from ms_modules.health import lifespan
from classes import charger 


"""
last_time_discharged: float = None
"""

# Taking the amount of time has passed since the last charge state. # Assume it has been charging in trickle charge for that length of time.
            # Modify the variables accordingly 
VOLTAGE_MAX = 10
time1 = 19
time_last_changed = 10
voltage = 20
current = 0
pcurrent = 4
time_in_trickle_charge = time1 - time_last_changed
            # apply the formulas to the varibles for the duration that they were affected

            # the voltage
voltage_max = VOLTAGE_MAX
            # Apply the voltage formula for trickle charge
new_voltage = (voltage_max / 1000) * time_in_trickle_charge
voltage = new_voltage
            # The current is 1/100 of the normal current in trickle charge
current = pcurrent/100 

print(voltage)
print(current)


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

