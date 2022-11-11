from classes.charger import Charger
from classes.powerbrick import PowerBrick
from classes.battery import Battery
from classes.phone import Phone
from ms_modules.charging import decide_charge_mode

power_brick = PowerBrick(15, 15)
battery = Battery(10, 10, 10, 10, 1200)
charger = Charger(battery, power_brick)
phone = Phone(True, True, True, True, 10, charger)

while True: 
        phone._root.update_idletasks()
        phone._root.update()
        if phone.is_charging:
            decide_charge_mode(charger)
            charger.charge_battery()