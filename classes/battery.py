import math


# Class representing the state of a battery of a phone.
class Battery:
    def __init__(self, current: float, voltage: float) -> None:
        """
        Initializes an instance of the Battery class based on the arguments you pass to this constructor.

        Keyword arguments:
        current -- the current of the battery.
        voltage -- the voltage of the battery.
        """

        # Initialize instance variables based on arguments passed to the constructor.
        self._current = current
        self._voltage = voltage

        # Time 
        self._time = None
        self._time_last_changed = None

    def _get_current(self) -> float:
        """Returns the current of the battery."""
        return self._current

    def _set_current(self, current) -> None:
        """Updates the current of the battery."""
        self._current = current

    def _get_voltage(self) -> float:
        """Returns the voltage of the battery."""
        return self._voltage

    def _set_voltage(self, voltage) -> None:
        """Updates the voltage of the battery."""
        self._voltage = voltage
    
    def _get_time(self) -> float:
        return self._time

    def _set_time(self, time) -> float:
        self._time = time

    def _get_time_last_changed(self) -> float:
        return self._time_last_changed
    
    def _set_time_last_changed(self, time_last_changed) -> float:
        self._time_last_changed = time_last_changed

    
    # Assign all of the getters of setters to class properties.
    # This means private instance variables can be accessed "directly" by using the getters and setters as an interface.
    # E.g. my_battery.is_charging = False calls _set_is_charging(False) under the hood.
    current = property(_get_current, _set_current)
    voltage = property(_get_voltage, _set_voltage)
    time = property(_get_time, _set_time)
    time_last_changed = property(_get_time_last_changed, _set_time_last_changed)
