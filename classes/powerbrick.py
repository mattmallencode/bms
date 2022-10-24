# Class representing the state of a phone power brick.
class PowerBrick:
    def __init__(self, CURRENT: float, VOLTAGE: float, ) -> None:
        """
        Initializes an instance of the Charger class based on the arguments you pass to this constructor.

        Keyword arguments:
        CURRENT -- constant, the current of the charger.
        VOLTAGE -- constant, the voltage of the charger.
        """
        self._CURRENT = CURRENT
        self._VOLTAGE = VOLTAGE

    def _get_current(self) -> float:
        """Returns the current of the charger."""
        return self._CURRENT

    def _get_voltage(self) -> float:
        """Returns the voltage of the charger"""
        return self._VOLTAGE
    # Assign all of the getters to class properties. No setters as all of the class' attribtutes are constants.
    # This means private instance variables can be accessed "directly" by using the getters and setters as an interface.
    # E.g. my_charger.current calls _get_current() under the hood.
    current = property(_get_current)
    voltage = property(_get_current)
