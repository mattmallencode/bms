from unittest import TestCase
from classes.phone import Phone
from classes.charger import Charger
from classes.battery import Battery
from classes.powerbrick import PowerBrick

# Need to create a dummy click event class to test UI elements.
class ClickEvent:
        def __init__(self, x, y):
            self.x = x
            self.y = y

class TestPhoneClass(TestCase):

    def test_phone_buttons(self):
        """
        Test to make sure that the phone buttons are functional and that the phone's state is captured correctly.
        """
        # Create a dummy power brick.
        power_brick = PowerBrick(15, 15)
        # Create a dummy battery.
        battery = Battery(10, 10)
        # Create a dummy charger.
        charger = Charger(battery, power_brick)
        # Create a dummy phone instance.
        p = Phone(False, False, True, False, 5.0, charger)

        # Create a dummy mouse click that should be within the bounds of the power on button.
        mouse_click = ClickEvent(p._power_button_corners["X1"] + 1, p._power_button_corners["Y1"] + 1)
        # Call the button press function with this mouse click.
        p._press(mouse_click)
        # The phone's powered_on state should now be true.
        self.assertEqual(p.powered_on, True)
        # Toggle phone off again.
        p._press(mouse_click)
        # The phone's powered_on state should now be false.
        self.assertEqual(p.powered_on, False)

        # Do the same as above but for the charging lead.
        mouse_click = ClickEvent(p._connector_corners["X1"] + 1, p._connector_corners["Y1"] + 1)
        p._press(mouse_click)
        self.assertEqual(p.is_charging, True)
        p._press(mouse_click)
        self.assertEqual(p.is_charging, False)

        # Do the same as above but for the home button i.e. display on.
        # First we must power the phone on.
        mouse_click = ClickEvent(p._power_button_corners["X1"] + 1, p._power_button_corners["Y1"] + 1)
        p._press(mouse_click)
        # then hit te home button to turn the screen on then off
        mouse_click = ClickEvent(p._home_button_corners["X1"] + 1, p._home_button_corners["Y1"] + 1)
        p._press(mouse_click)
        self.assertEqual(p.display_on, True)
        p._press(mouse_click)
        self.assertEqual(p.display_on, False)

        # Now to test the "unlock" and "lock" -> must turn display back on first.
        mouse_click = ClickEvent(p._home_button_corners["X1"] + 1, p._home_button_corners["Y1"] + 1)
        p._press(mouse_click)
        mouse_click = ClickEvent(p._unlock_button["X1"] + 1, p._unlock_button["Y1"] + 1)
        self.assertEqual(p.locked, True)
        p._press(mouse_click)
        self.assertEqual(p.locked, False)

        # Now for the settings screen -> display must be on and phone must be unlocked
        mouse_click = ClickEvent(p._settings_button["X1"] + 1, p._settings_button["Y1"] + 1)
        self.assertEqual(p._settings, False)
        p._press(mouse_click)
        self.assertEqual(p._settings, True)
        p._press(mouse_click)
        self.assertEqual(p._settings, False)
