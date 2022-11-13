from unittest import TestCase
import time

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

    def __init__(self):
        # Create a dummy power brick.
        self.power_brick = PowerBrick(15, 15)
        # Create a dummy battery.
        self.battery = Battery(10, 10, 10, 10)
        # Create a dummy charger.
        self.charger = Charger(self.battery, self.power_brick)
        # Create a dummy phone instance.
        p = Phone(False, False, True, False, 5.0, self.charger)

    def test_DecideChargeMode(self):
        self.battery.voltage = config.VOLTAGE_MIN-1
        decide_charge_mode(self.charger)
        self.assertEqual(self.charger.charge_setting, "trickle")

        self.battery.voltage = config.VOLTAGE_MIN+1
        decide_charge_mode(self.charger)
        self.assertEqual(self.charger.charge_setting, "constant_current")

        self.battery.voltage = config.VOLTAGE_MAX
        decide_charge_mode(self.charger)
        self.assertEqual(self.charger.charge_setting, "constant_voltage")

        self.battery.voltage = config.VOLTAGE_MAX+1
        decide_charge_mode(self.charger)
        self.assertEqual(self.charger.charge_setting, "constant_voltage")

        self.battery.current = config.THRESHOLD
        decide_charge_mode(self.charger)
        self.assertEqual(self.charger.charge_setting, "trickle")

        self.battery.current = config.THRESHOLD-1
        decide_charge_mode(self.charger)
        self.assertEqual(self.charger.charge_setting, "trickle")


    def test_discharge(self):
        discharge(self.battery, self.p, time.time()-100)
        last_voltage = self.battery.voltage
        self.assertLess(self.charger.charge_setting, last_voltage)
        
if __name__ == '__main__':
    unittest.main()