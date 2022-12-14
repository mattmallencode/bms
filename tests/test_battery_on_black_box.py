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

class TestPowerOn(TestCase):
    # Create a dummy phone
    def test_power_on(self):
        ''' To test that the phone is on we press the on button and confirm the phone is actually on we navigate
        to the settings page on the UI and watch as power is drawn. The phone must be unplugged for this to work'''
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
        # See if the boolean value for turned on has changed.
        self.assertTrue(p.powered_on)

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

        # We wait five seconds for the battery percent to decrease to show that the phone is on.
        # The battery state of percent is updated.
        state_of_charge(charger, p)
        last_battery_percent = config.chargepercent
        time.sleep(5)
        state_of_charge(charger, p)
        current_battery_percent = config.chargepercent

        self.assertLess(current_battery_percent, last_battery_percent)