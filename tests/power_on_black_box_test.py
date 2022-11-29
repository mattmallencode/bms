'''When the phone is powered on the ON symbol appears on the screen.'''

# Test whether the on sybol appears
from unittest import TestCase
from classes.phone import Phone
# Need to create a dummy click event class to test UI elements.
class ClickEvent:
        def __init__(self, x, y):
            self.x = x
            self.y = y

class TestPowerOn(TestCase):
    # Create a dummy phone
    def test_power_on(self):
        p = Phone(False, False, True, False, 5.0)
        p.powered_on = False

        # Do the same as above but for the home button i.e. display on.
        # First we must power the phone on.
        mouse_click = ClickEvent(p._power_button_corners["X1"] + 1, p._power_button_corners["Y1"] + 1)
        p._press(mouse_click)

        # See if the boolean value for turned on has changed.
        print(p.powered_on)
        self.assertTrue(p.powered_on, "Phone is not powered on." )
