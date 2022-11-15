from unittest import TestCase
from time import time

# Importing the phone class
from classes.phone import Phone
# Importing the Battery class 
from classes.battery import Battery
# Importing the Charger class
from classes.charger import Charger
# Importing the Powerbrick class
from classes.powerbrick import PowerBrick

# importing the functions that get tested
from ms_modules.charging import decide_charge_mode, discharge

# Import all from config.py
import config 


class TestChargeModeClass(TestCase):

    def test_DecideChargeMode(self):
        # Create a dummy power brick.
        power_brick = PowerBrick(15, 15)
        # Create a dummy battery.
        battery = Battery(10, 10, 10, 10)
        # Create a dummy charger.
        charger = Charger(battery, power_brick)
        # Create a dummy phone instance.
        p = Phone(False, False, True, False, 5.0, charger)

        battery.voltage = config.VOLTAGE_MIN-1
        decide_charge_mode(charger)
        self.assertEqual(charger.charge_setting, "trickle")

        battery.voltage = config.VOLTAGE_MIN+1
        decide_charge_mode(charger)
        self.assertEqual(charger.charge_setting, "constant_current")

        battery.voltage = config.VOLTAGE_MAX
        decide_charge_mode(charger)
        self.assertEqual(charger.charge_setting, "constant_voltage")

        battery.voltage = config.VOLTAGE_MAX+1
        decide_charge_mode(charger)
        self.assertEqual(charger.charge_setting, "constant_voltage")

        battery.current = config.THRESHOLD
        decide_charge_mode(charger)
        self.assertEqual(charger.charge_setting, "trickle")

        battery.current = config.THRESHOLD-1
        decide_charge_mode(charger)
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

        last_voltage = battery.voltage
        discharge(battery, p, time()-100)        
        self.assertLess(battery.voltage, last_voltage)