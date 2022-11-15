from classes.battery import Battery
from classes.charger import Charger
from classes.phone import Phone
from classes.powerbrick import PowerBrick
from ms_modules.charging import decide_charge_mode
import config

power_brick = PowerBrick(config.CURRENT, 5)
battery = Battery(0, 3.8)
charger = Charger(battery, power_brick)
phone = Phone(True, True, True, True, 10, charger)



while True: 
        phone._root.update_idletasks()
        phone._root.update()
        if phone.is_charging:
            decide_charge_mode(charger)
            charger.charge_battery()