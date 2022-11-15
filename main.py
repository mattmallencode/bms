from classes.battery import Battery
from classes.charger import Charger
from classes.phone import Phone
from classes.powerbrick import PowerBrick
from ms_modules.charging import decide_charge_mode
from ms_modules.metrics import state_of_charge, time_till_empty, time_till_full
import config
from time import time

power_brick = PowerBrick(config.POWER_BRICK_CURRENT, config.POWER_BRICK_VOLTAGE)
battery = Battery(1, 3.6)
charger = Charger(battery, power_brick)


config.chargepercent = ((3.6 - config.VOLTAGE_MIN) * 100)/ (config.VOLTAGE_MAX - config.VOLTAGE_MIN)
config.ttf = time_till_full(charger, config.chargepercent, config.CAPACITY * config.lifespan)
phone = Phone(True, True, True, True, 0.6, charger)
config.tte = time_till_empty(phone, config.chargepercent, config.CAPACITY * config.lifespan)

while True: 
        phone._root.update_idletasks()
        phone._root.update()
        if phone.is_charging:
            decide_charge_mode(charger)
            charger.charge_battery()
        time_since_last_charge = time()
        state_of_charge(charger, phone, config.chargepercent, time_since_last_charge, config.CAPACITY * config.lifespan)
        time_till_empty(phone, config.chargepercent, config.CAPACITY * config.lifespan)
        time_till_full(charger, config.chargepercent, config.CAPACITY * config.lifespan)