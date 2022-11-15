from typing import Type
from unittest import TestCase
from classes.charger import Charger
from classes.battery import Battery
from classes.powerbrick import PowerBrick

import config
import time

class TestChargingModule(TestCase):

    def test_charging_function(self):
        ''' This function tests if the charging functions constant current, constant voltage and trickle charge are functioning correctly.'''
        # Create a dummy power brick.
        power_brick = PowerBrick(2, 5)
        # Create a dummy battery.
        battery = Battery(10, 10)
        # Create dummy charger instance
        charger = Charger(battery, power_brick)

        
        
        # Trickle charge
        last_voltage = battery.voltage
        
        charger.charge_setting = "trickle"
        #call the charge battery function
        charger.charge_battery()
        self.assertGreater(battery.voltage, last_voltage)
        # Test for the current in trickle charge
        self.assertAlmostEqual(power_brick.current, power_brick.current / 100)

        # Constant current
        last_voltage = battery.voltage

        charger.charge_setting = "constant_current"
        #call the charge battery function
        charger.charge_battery()
        # Constant current voltage
        self.assertGreater(battery.voltage, last_voltage)
        # Constant current 
        self.assertAlmostEqual(config.CHARGE_C, power_brick.current)

        # Constant voltage
        last_voltage = battery.voltage
        initial_current = battery.current
        
        charger.charge_setting = "constant_voltage"
        charger.charge_battery()
        # Constant current
        self.assertGreater(battery.voltage, last_voltage)
        self.assertLessEqual(battery.current, initial_current)
        

        

        

    

        
     

