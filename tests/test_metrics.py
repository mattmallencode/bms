from time import sleep, time
from unittest import TestCase

from classes.battery import Battery
from classes.charger import Charger
from classes.phone import Phone
from classes.powerbrick import PowerBrick
from ms_modules.metrics import state_of_charge, time_till_empty, time_till_full
import config


class TestMetricsModule(TestCase):
    battery = Battery(2, 3.6)
    power_brick = PowerBrick(2, 5)
    charger = Charger(battery, power_brick)
    phone = Phone(False, False, True, False, 5, charger)

    def test_time_till_full(self):
        # instantiate variables
        self.battery_percentage = 60
        self.functional_capacity = 2600
        
        #calculate ttf and check if it is equal to the expected result
        ttf = time_till_full(self.charger, self.battery_percentage, self.functional_capacity)
        self.assertAlmostEqual(ttf, 0.52)

    def test_time_till_empty(self):
        # instantiate variables
        self.battery_percentage = 60
        self.functional_capacity = 2600
        
        #calculate tte and check if it is equal to the expected result
        tte = time_till_empty(self.phone, self.battery_percentage, self.functional_capacity)
        self.assertEqual(tte, 0.312)

    def test_state_of_charge(self):
        # instantiate variables for if the phone is charging test case
        self.phone.is_charging = True
        self.battery_percentage = 60
        self.functional_capacity = 2600
        self.time_since_last_soc_calulation = time()
        # sleep for 30 seconds to obtain a noticeable change in the SoC value
        sleep(5)
        #calculate soc
        soc = state_of_charge(self.charger, self.phone, self.battery_percentage, self.time_since_last_soc_calulation, self.functional_capacity)
        soc = round(soc, 2)
        # check if soc value equal to expected result
        self.assertAlmostEqual(soc, 63.85, 1)


        # instantiate variables for if the phone is not charging test case
        self.phone.is_charging = False
        self.battery_percentage = 60
        self.functional_capacity = 2600
        self.time_since_last_soc_calulation = time()
        # sleep for 30 seconds to obtain a noticeable change in the SoC value
        sleep(5)
        #calculate soc
        soc = state_of_charge(self.charger, self.phone, self.battery_percentage, self.time_since_last_soc_calulation ,self.functional_capacity)
        soc = round(soc, 2)

        # check if soc value equal to expected result
        self.assertAlmostEqual(soc, 50.38, 1)