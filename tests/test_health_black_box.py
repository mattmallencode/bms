from unittest import TestCase
from classes.phone import Phone


# Need to create a dummy click event class to test UI elements.
class ClickEvent:
        def __init__(self, x, y):
            self.x = x
            self.y = y

class HealthTest(TestCase):

    def test_health(self):
        '''If the user can execute all these tasks within the UI it means they will be able to see the health metric displayed.'''
        p = Phone(False, False, True, False, 5.0)

        # Create a dummy mouse click that should be within the bounds of the power on button.
        mouse_click = ClickEvent(p._power_button_corners["X1"] + 1, p._power_button_corners["Y1"] + 1)
        # Call the button press function with this mouse click.
        p._press(mouse_click)
        # The phone's powered_on state should now be true.
        self.assertEqual(p.powered_on, True)
        # Do the same as above but for the home button i.e. display on.

        # then hit te home button to turn the screen on 
        mouse_click = ClickEvent(p._home_button_corners["X1"] + 1, p._home_button_corners["Y1"] + 1)
        p._press(mouse_click)
        self.assertEqual(p.display_on, True)

        # Hit the unlock button.
        mouse_click = ClickEvent(p._unlock_button["X1"] + 1, p._unlock_button["Y1"] + 1)
        p._press(mouse_click)
        self.assertEqual(p.locked, False)

        #Next the settings button is pressed. If this is true then the battery health is visible.
        mouse_click = ClickEvent(p._settings_button["X1"] + 1, p._settings_button["Y1"] + 1)
        p._press(mouse_click)
        self.assertEqual(p._settings, True)

