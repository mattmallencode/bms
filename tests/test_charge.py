from unittest import TestCase

# Importing the Charger class
from classes.charger import Charger
# Importing the Battery class 
from classes.battery import Battery
# Importing the Powerbrick class
from classes.powerbrick import PowerBrick

from ms_modules.charging import *

import config


class TestChargeModeClass(TestCase):

    def test_DecideChargeMode(self):
        # Create a dummy power brick.
        power_brick = PowerBrick(15, 15)
        # Create a dummy battery.
        battery = Battery(10, 10, 10, 10)
        # Create a dummy charger.
        charger = Charger(battery, power_brick)

        battery.voltage = config.VOLTAGE_MIN-1
        ms_modules.decide_charge_mode(charger)
        self.assertEqual(charger.charge_setting, "trickle")

        battery.voltage = config.VOLTAGE_MIN+1
        ms_modules.decide_charge_mode(charger)
        self.assertEqual(charger.charge_setting, "constant_current")

        battery.voltage = config.VOLTAGE_MAX
        ms_modules.decide_charge_mode(charger)
        self.assertEqual(charger.charge_setting, "constant_voltage")

        battery.voltage = config.VOLTAGE_MAX+1
        ms_modules.decide_charge_mode(charger)
        self.assertEqual(charger.charge_setting, "constant_voltage")

        battery.current = config.THRESHOLD
        ms_modules.decide_charge_mode(charger)
        self.assertEqual(charger.charge_setting, "trickle")

        battery.current = config.THRESHOLD-1
        ms_modules.decide_charge_mode(charger)
        self.assertEqual(charger.charge_setting, "trickle")


    def test_discharge(self):
        # Create a dummy power brick.
        power_brick = PowerBrick(15, 15)
        # Create a dummy battery.
        battery = Battery(10, 10, 10, 10)
        # Create a dummy charger.
        charger = Charger(battery, power_brick)
        # Create a dummy phone instance.
        p = Phone(False, False, True, False, 5.0, charger)

        ms_modules.discharge(battery, p, time.time()-100)
        last_voltage = battery.voltage
        self.assertLess(charger.charge_setting, last_voltage)
        


