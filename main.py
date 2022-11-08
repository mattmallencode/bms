from classes.phone import Phone
from ms_modules import charging
from ms_modules.health import lifespan
from classes.charger import Charger
from classes.battery import Battery
from classes.phone import Phone
from classes.powerbrick import PowerBrick

"""
last_time_discharged: float = None
"""


battery = Battery(1.0, 1.0, 1.0, 1.0)
charger = Charger(battery)
brick = PowerBrick(1.0, 1.0)

print(config.lifespan)
