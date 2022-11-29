from unittest import TestCase
from classes.phone import Phone
from classes.charger import Charger
from classes.battery import Battery
from classes.powerbrick import PowerBrick
from ms_modules.metrics import state_of_charge
import config
import time

# Need to create a dummy click event class to test UI elements.
class ClickEvent:
        def __init__(self, x, y):
            self.x = x
            self.y = y

class PlugInTest(TestCase):

    def test_plug_in(self):
        '''Test that the plug in function works. When the user clicks on the charger. After a time period the percentage will increase'''
        p = Phone(False, False, True, False, 5.0)
        # Create a dummy power brick.
        power_brick = PowerBrick(config.POWER_BRICK_CURRENT, config.POWER_BRICK_VOLTAGE)
        # Create a dummy battery.
        battery = Battery(10, 3.6)
        # Create dummy charger instance
        charger = Charger(battery, power_brick)

        # First we must power the phone on.
        mouse_click = ClickEvent(p._power_button_corners["X1"] + 1, p._power_button_corners["Y1"] + 1)
        p._press(mouse_click)
        # The phone's powered_on state should now be true.
        self.assertEqual(p.powered_on, True)

        # Hit the home button to turn the screen on 
        mouse_click = ClickEvent(p._home_button_corners["X1"] + 1, p._home_button_corners["Y1"] + 1)
        p._press(mouse_click)
        self.assertEqual(p.display_on, True)

        # Hit the unlock button to get access to the settings button.
        mouse_click = ClickEvent(p._unlock_button["X1"] + 1, p._unlock_button["Y1"] + 1)
        p._press(mouse_click)
        self.assertEqual(p.locked, False)

        # Next the settings button is pressed. If this is true then the battery health is visible.
        mouse_click = ClickEvent(p._settings_button["X1"] + 1, p._settings_button["Y1"] + 1)
        p._press(mouse_click)
        self.assertEqual(p._settings, True)

        # Now that you can see the battery percentage plug in the phone and wait 5 seconds. The battery percentage will increase.
        # Do the same as above but for the charging lead.
        mouse_click = ClickEvent(p._connector_corners["X1"] + 1, p._connector_corners["Y1"] + 1)
        p._press(mouse_click)
        self.assertEqual(p.is_charging, True)

        #call the charge battery function
        charger.charge_battery()
        #The battery state of charge is updated.
        state_of_charge(charger, p)
        last_battery_percent = config.chargepercent
        # User leaves the phone charge for 5 seconds
        time.sleep(5)
        # The battery should be charging. 
        charger.charge_battery()
        # State of battery will be updated.
        state_of_charge(charger, p)
        # This is the updated percent on the screen.
        current_battery_percent = config.chargepercent
        self.assertGreater(current_battery_percent, last_battery_percent)
