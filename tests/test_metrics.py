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
    phone = Phone(False, False, True, False, 5)

    def test_time_till_full(self):
        "Method to test the time_till_full() function."
        # instantiate variables
        # instantiate variables
        config.chargepercent = 50
        config.last_soc_ttf = 49
        config.time_of_last_ttf = time()
        sleep(1)
        #calculate tte and check if it is equal to the expected result
        ttf = time_till_full(self.phone)
        self.assertTrue(ttf > 49 and ttf < 51)

    def test_time_till_empty(self):
        "Method to test the time_till_empty() function."
        # instantiate variables
        config.chargepercent = 99
        config.last_soc_tte = 100
        config.time_of_last_tte = time()
        sleep(1)
        #calculate tte and check if it is equal to the expected result
        tte = time_till_empty(self.phone)
        self.assertTrue(tte > 98 and tte < 100)

    def test_state_of_charge(self):
        "Method to test the state_of_charge() function."
        # instantiate variables for if the phone is charging test case
        self.phone.is_charging = True
        config.chargepercent = 60
        config.CAPACITY = 2600
        config.lifespan = 1
        config.time_since_last_soc_calculation = time()
        # sleep for 30 seconds to obtain a noticeable change in the SoC value
        sleep(5)
        #calculate soc
        soc = state_of_charge(self.charger, self.phone)
        soc = round(soc, 2)
        # check if soc value equal to expected result
        self.assertAlmostEqual(soc, 63.85, 1)


        # instantiate variables for if the phone is not charging test case
        self.phone.is_charging = False
        config.chargepercent = 60
        config.CAPACITY = 2600
        config.lifespan = 1
        self.time_since_last_soc_calulation = time()
        # sleep for 30 seconds to obtain a noticeable change in the SoC value
        sleep(5)
        #calculate soc
        soc = state_of_charge(self.charger, self.phone)
        soc = round(soc, 2)

        # check if soc value equal to expected result
        self.assertAlmostEqual(soc, 60, 1)