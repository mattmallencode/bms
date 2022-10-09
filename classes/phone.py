# Class representing the state of a phone.
class Phone:
    def __init__(self, powered_on: bool, display_on: bool, locked: bool) -> None:
        """
        Initializes an instance of the Phone class based on the arguments you pass to this constructor.

        Keyword arguments:
        powered_on -- bool indicating whether the phone is currently powered on.
        display_on -- bool indicating whether the phone's screen / display is turned on.
        locked -- bool indicating whether the phone is currently locked.
        """
        # Initialize instance variables based on arguments passed to the constructor.
        self._powered_on = powered_on
        self._display_on = display_on
        self._locked = locked

    def _get_powered_on(self) -> bool:
        """Returns whether the phone is powered on or not."""
        return self._powered_on

    def _set_powered_on(self, true_or_false: bool) -> None:
        """Updates whether the phone is powered on or not."""
        self._powered_on = true_or_false

    def _get_display_on(self) -> bool:
        """Returns whether the phone's display is turned on or not."""
        return self._display_on

    def _set_display_on(self, true_or_false: bool) -> None:
        """Updates whether the phone's display is turned on or not."""
        self._display_on = true_or_false

    def _get_locked(self) -> bool:
        """Returns whether the phone is locked or not."""
        return self._locked

    def _set_locked(self, true_or_false: bool) -> None:
        """Updates whether the phone is locked or not."""
        self._locked = true_or_false
    # Assign all of the getters to class properties. No setters as all of the class' attribtutes are constants.
    # This means private instance variables can be accessed "directly" by using the getters and setters as an interface.
    # E.g. my_phone.powered_on = False calls _set_powered_on(False) under the hood.
    powered_on = property(_get_powered_on, _set_powered_on)
    display_on = property(_get_display_on, _set_display_on)
    locked = property(_get_locked, _set_locked)
