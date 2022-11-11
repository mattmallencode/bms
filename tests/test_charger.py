from typing import Type
from unittest import TestCase
from classes.charger import Charger
from classes.battery import Battery
from classes.powerbrick import PowerBrick
import config

class TestChargingFunctions(TestCase):
    

    def __init__(self, battery: Type[Battery], powerbrick:Type[PowerBrick]) -> None:
        self._power_brick =  powerbrick(15, 15)
        # Create a dummy battery.
        self._battery = battery(10, 10, 10, 10)
        # Create a dummy charger.
        self._charger = Charger(battery, self._power_brick)

    def test_charging_function(self):
        """ Tests the charging function of the Charger class in classes.
        
            Ensures the CC, CV, TC all work appropriately"""
        Charger.affect_of_charging_the_battery(self)

