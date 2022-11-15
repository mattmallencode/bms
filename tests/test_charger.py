from typing import Type
from unittest import TestCase
from classes.charger import Charger
from classes.battery import Battery
from classes.powerbrick import PowerBrick

import config
import time

class TestChargingModule(TestCase):

    def test_charging_function(self):
        # Create a dummy power brick.
        power_brick = PowerBrick(15, 15)
        # Create a dummy battery.
        battery = Battery(10, 10, 10, 10)
        # Create dummy charger instance
        charger = Charger(battery, power_brick)
        # Create a dummy charging instance.
        charger.charge_battery()
        if charger._charge_setting == "trickle":
            self.assertAlmostEqual(charger._battery.voltage, 0.0042)
            self.assertAlmostEqual(charger._battery.current, 0.02)
        if charger._charge_setting == "constant_current":
            self.assertAlmostEqual(charger._battery.voltage, 1.0)
            self.assertAlmostEqual(charger._battery.current, 1.0)
        if charger._charge_setting == "constant_voltage":
            self.assertAlmostEqual(charger._battery.voltage, 4.2)
            self.assertAlmostEqual(charger._battery.current, 1.54)
        

    

        
     

