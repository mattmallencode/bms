from classes.battery import Battery
from classes.charger import Charger
from classes.phone import Phone
from ms_modules.health import lifespan
from classes import charger 


battery = Battery(1.0, 1.0, 1.0, 1.0)
charger = Charger(battery)
phone = Phone(False, False, False, True)
brick = PowerBrick(1.0, 1.0)

from modules.charging import decide_charge_mode

while True:
    if charger.is_powerbrick_plugged_in():
        charge_mode = decide_charge_mode()
       
    else:
        phone._is_charging = False

    

