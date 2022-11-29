from typing import Type
from unittest import TestCase
from classes.charger import Charger
from classes.battery import Battery
from classes.powerbrick import PowerBrick

from time import sleep
import config


class TestChargingModule(TestCase):

    def test_charging_function(self):
        ''' This function tests if the charging functions constant current, constant voltage and trickle charge are functioning correctly.'''
        # Create a dummy power brick.
        power_brick = PowerBrick(config.POWER_BRICK_CURRENT, config.POWER_BRICK_VOLTAGE)
        # Create a dummy battery.
        battery = Battery(10, 3.6)
        # Create dummy charger instance
        charger = Charger(battery, power_brick)

        
        
        # Trickle charge
        last_voltage = battery.voltage
        
        charger.charge_setting = "trickle"
        #call the charge battery function
        charger.charge_battery()
        sleep(1)
        charger.charge_battery()
        self.assertGreater(battery.voltage, last_voltage)
        # Test for the current in trickle charge
        self.assertAlmostEqual(battery.current, power_brick.current / 100)

        # Constant current
        last_voltage = battery.voltage

        charger.charge_setting = "constant_current"
        #call the charge battery function
        charger.charge_battery()
        sleep(1)
        charger.charge_battery()
        print()
        # Constant current voltage
        self.assertGreater(battery.voltage, last_voltage)
        # Constant current 
        self.assertLess(config.CHARGE_C, power_brick.current)

        # Constant voltage
        last_voltage = battery.voltage
        initial_current = battery.current
        
        charger.charge_setting = "constant_voltage"
        charger.charge_battery()
        sleep(1)
        charger.charge_battery()
        # Constant voltage 
        self.assertEqual(battery.voltage, last_voltage)
        # Constant voltage  current 
        self.assertLess(battery.current, initial_current)