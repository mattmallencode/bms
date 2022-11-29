from unittest import TestCase
from classes.phone import Phone


# Need to create a dummy click event class to test UI elements.
class ClickEvent:
        def __init__(self, x, y):
            self.x = x
            self.y = y

class TestTimeTillFull(TestCase):
    
    def test_time_till_full(self):
        '''User process to see the time till varible
        If a user can execute these steps the TTF will be visible'''
        p = Phone(False, False, True, False, 5.0)

        # Create a dummy mouse click that should be within the bounds of the power on button.
        mouse_click = ClickEvent(p._power_button_corners["X1"] + 1, p._power_button_corners["Y1"] + 1)
        # Call the button press function with this mouse click.
        p._press(mouse_click)
        # The phone's powered_on state should now be true.
        self.assertEqual(p.powered_on, True)
        # plug in the phone 
        mouse_click = ClickEvent(p._connector_corners["X1"] + 1, p._connector_corners["Y1"] + 1)
        p._press(mouse_click)
        self.assertEqual(p.is_charging, True)
        # Do the same as above but for the home button i.e. display on.
        # then hit te home button to turn the screen on The time till full should be visible.
        mouse_click = ClickEvent(p._home_button_corners["X1"] + 1, p._home_button_corners["Y1"] + 1)
        p._press(mouse_click)
        self.assertEqual(p.display_on, True)
