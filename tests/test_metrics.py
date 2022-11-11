from unittest import TestCase
from classes.phone import Phone
from classes.charger import Charger
from classes.battery import Battery
from classes.powerbrick import PowerBrick
from ms_modules.metrics import time_till_full, time_till_empty, state_of_charge
import config

class TestMetricsModule(TestCase):

    def __init__(self):
        self.battery = Battery(10.0, 10.0, 10.0, 10.0, 1200.0)
        self.powerbrick = PowerBrick(20, 20)
        self.charger = Charger(self.battery, self.powerbrick)
        self.phone = Phone(False, False, True, False, 10.0, self.charger)
        self._battery_percentage = 60

    def test_time_till_full(self):
        ttf = time_till_full(self.charger, self._battery_percentage)
        print(ttf)


    def test_time_till_empty(self):
        tte = time_till_empty(self.charger, self.phone, self._battery_percentage)
        print(tte)



        
        

