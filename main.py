from classes.battery import Battery
from classes.charger import Charger
from classes.phone import Phone
from classes.powerbrick import PowerBrick
from ms_modules.charging import decide_charge_mode
from ms_modules.metrics import state_of_charge
import config
from time import time

power_brick = PowerBrick(15, 15)
battery = Battery(10, 3.6)
charger = Charger(battery, power_brick)
phone = Phone(True, True, True, True, 10, charger)

config.chargepercent = ((3.6 - config.VOLTAGE_MIN) * 100)/ (config.VOLTAGE_MAX - config.VOLTAGE_MIN)

while True: 
        phone._root.update_idletasks()
        phone._root.update()
        if phone.is_charging:
            decide_charge_mode(charger)
            charger.charge_battery()
        time_since_last_charge = time()
        config.chargepercent = state_of_charge(charger, phone, config.chargepercent, time_since_last_charge, config.CAPACITY * config.lifespan)
        print(battery.current)