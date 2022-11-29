from unittest import TestCase
from classes.phone import Phone


# Need to create a dummy click event class to test UI elements.
class ClickEvent:
        def __init__(self, x, y):
            self.x = x
            self.y = y

class TestTimeTillEmpty(TestCase):

    def test_time_till_empty(self):
        ''' What the user does to see the time till empty
        If the user is able to execute the following steps the TTE will be visible on the screen'''
        p = Phone(False, False, True, False, 5.0)

        # Create a dummy mouse click that should be within the bounds of the power on button.
        mouse_click = ClickEvent(p._power_button_corners["X1"] + 1, p._power_button_corners["Y1"] + 1)
        # Call the button press function with this mouse click.
        p._press(mouse_click)
        # The phone's powered_on state should now be true.
        self.assertEqual(p.powered_on, True)

        # Do the same as above but for the charging lead.
        mouse_click = ClickEvent(p._connector_corners["X1"] + 1, p._connector_corners["Y1"] + 1)
        p._press(mouse_click)
        p._press(mouse_click)
        self.assertEqual(p.is_charging, False)

        # then hit te home button to turn the screen on then off
        mouse_click = ClickEvent(p._home_button_corners["X1"] + 1, p._home_button_corners["Y1"] + 1)
        p._press(mouse_click)
        self.assertEqual(p.display_on, True)
        # If these hold true then the TTE will be visible to the user.