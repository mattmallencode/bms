from time import sleep, time
from unittest import TestCase

from classes.battery import Battery
from classes.charger import Charger
from classes.phone import Phone
from classes.powerbrick import PowerBrick
from ms_modules.metrics import state_of_charge, time_till_empty, time_till_full


class TestMetricsModule(TestCase):
    battery = Battery(10.0, 10.0, 10.0, 10.0)
    powerbrick = PowerBrick(20.0, 20.0)
    charger = Charger(battery, powerbrick)
    phone = Phone(False, False, True, False, 10.0, charger)

    def test_time_till_full(self):
        # instantiate variables
        self.battery_percentage = 60
        self.functional_capacity = 1200
        
        #calculate ttf and check if it is equal to the expected result
        ttf = time_till_full(self.charger, self.battery_percentage, self.functional_capacity)
        self.assertEqual(ttf, 48)

    def test_time_till_empty(self):
        # instantiate variables
        self.battery_percentage = 60
        self.functional_capacity = 1200
        
        #calculate tte and check if it is equal to the expected result
        tte = time_till_empty(self.charger, self.phone, self.battery_percentage, self.functional_capacity)
        self.assertEqual(tte, 72)

    def test_state_of_charge(self):
        # instantiate variables for if the phone is charging test case
        self.phone.is_charging = True
        self.battery_percentage = 60
        self.functional_capacity = 1200
        self.time_since_last_soc_calulation = time()
        # sleep for 30 seconds to obtain a noticeable change in the SoC value
        sleep(30)
        #calculate soc
        soc = state_of_charge(self.charger, self.phone, self.battery_percentage, self.time_since_last_soc_calulation, self.functional_capacity)
        soc = round(soc, 2)
        # check if soc value equal to expected result
        self.assertAlmostEqual(soc, 60.25)


        # instantiate variables for if the phone is not charging test case
        self.phone.is_charging = False
        self.battery_percentage = 60
        self.functional_capacity = 1200
        self.time_since_last_soc_calulation = time()
        # sleep for 30 seconds to obtain a noticeable change in the SoC value
        sleep(30)
        #calculate soc
        soc = state_of_charge(self.charger, self.phone, self.battery_percentage, self.time_since_last_soc_calulation, self.functional_capacity)
        soc = round(soc, 2)
        # check if soc value equal to expected result
        self.assertAlmostEqual(soc, 59.75)




        
        

