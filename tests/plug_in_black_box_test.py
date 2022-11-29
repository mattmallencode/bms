from unittest import TestCase
from classes.phone import Phone

from unittest import TestCase
from classes.phone import Phone


# Need to create a dummy click event class to test UI elements.
class ClickEvent:
        def __init__(self, x, y):
            self.x = x
            self.y = y

class PlugInTest(TestCase):

    def test_plug_in(self):
        '''Test that the plug in function works. When the user clocks on the charger'''
        p = Phone(False, False, True, False, 5.0)

        # Do the same as above but for the charging lead.
        mouse_click = ClickEvent(p._connector_corners["X1"] + 1, p._connector_corners["Y1"] + 1)
        p._press(mouse_click)
        self.assertEqual(p.is_charging, True)
        p._press(mouse_click)
        self.assertEqual(p.is_charging, False)

        



