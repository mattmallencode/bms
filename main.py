from classes.battery import Battery
from classes.charger import Charger
from classes.phone import Phone
from classes.powerbrick import PowerBrick
from ms_modules.charging import decide_charge_mode, discharge
from ms_modules.metrics import state_of_charge, time_till_empty, time_till_full, adjust_lifespan
import config
from time import time, sleep

power_brick = PowerBrick(config.POWER_BRICK_CURRENT, config.POWER_BRICK_VOLTAGE)
battery = Battery(1, 3.0)
charger = Charger(battery, power_brick)
last_time_discharged = None

config.chargepercent = ((3.0 - config.VOLTAGE_MIN) * 100)/ (config.VOLTAGE_MAX - config.VOLTAGE_MIN)
config.ttf = 0.53
phone = Phone(True, True, True, True, 0.01)
config.tte = 0

while True: 
        phone._root.update_idletasks()
        phone._root.update()
        if phone._is_charging:
            phone._timetill.set(f"battery full in\n {phone._hours_minutes_seconds(config.ttf)} hours")
        else:
            phone._timetill.set(f"battery dead in\n {phone._hours_minutes_seconds(config.tte)} hours")
        if phone.is_charging == True:
            charger.charge_battery()
            decide_charge_mode(charger)
        if phone.powered_on == True:
            if last_time_discharged == None:
                last_time_discharged = time()
            soc_before = state_of_charge(charger, phone)
            discharge(battery, phone, last_time_discharged)
            soc_after = state_of_charge(charger, phone)
            adjust_lifespan(soc_after -soc_before)
            last_time_discharged = time()
            if phone.locked and phone.is_charging == True:
                time_till_full(charger)
            if phone.locked and phone.is_charging == False:
                time_till_empty(phone)
        print(charger.charge_setting, config.chargepercent, battery._current, battery._voltage)