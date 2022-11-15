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
        battery = Battery(10, 10, 10, 10)
        # Create dummy charger instance
        charger = Charger(battery, power_brick)
        
        
        # Trickle charge
        battery.voltage = config.VOLTAGE_MIN-1
        last_voltage = battery.voltage
        
        charger.charge_setting = "trickle"
        #call the charge battery function
        charger.charge_battery()
        self.assertGreater(battery.voltage, last_voltage)
        # Test for the current in trickle charge
        self.assertAlmostEqual(power_brick.current, power_brick.current / 100)

        # Constant current
        battery.voltage = config.VOLTAGE_MIN+1
        last_voltage = battery.voltage
        charger.charge_setting = "constant_current"
        # Constant current
        self.assertGreater(battery.voltage, last_voltage)


        # Constant voltage
        battery.voltage = config.VOLTAGE_MAX+1
        last_voltage = battery.voltage
        battery.current = config.THRESHOLD
        charger.charge_setting = "constant_voltage"
        charger.charge_battery()
        # Constant current
        self.assertGreater(battery.voltage, last_voltage)
        

        
        

    

        
     

