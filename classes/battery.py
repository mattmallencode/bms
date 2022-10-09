# Class representing the state of a battery of a phone.
class Battery:
    def __init__(self, is_charging: bool, current: float, voltage: float, drain: float, temperature: float, lifespan: int, voltage_norm: float, voltage_min: float, voltage_max: float,  charge_c: float, discharge_c: float, thermal_runaway: float, is_alive: bool, charge_status: float) -> None:
        """
        Initializes an instance of the Battery class based on the arguments you pass to this constructor.

        Keyword arguments:
        is_charging -- bool indicating whether the Battery is being charged by an instance of the Charger class.
        current -- the current of the battery.
        voltage -- the voltage of the battery.
        drain -- the load on the battery i.e. the charge being drawn from it by the phone.
        temperature -- the temperature of the battery.
        lifespan -- estimate of how many full charge and discharge cycles the battery can handle before it begins to lose functional capacity.
        voltage_norm -- the optimum voltage for this battery, should be trended towards to minimize battery degradation.
        voltage_min -- at this voltage the battery is dead, trending towards this voltage indicates a lower capacity.
        voltage_max -- if voltage trends towards this value, it leads to degradation.
        charge_c -- max rate of charge.
        discharge_c -- max rate of discharge.
        thermal_runaway -- the temperature at which the battery will keep increasing in temperature and go on fire.
        is_alive -- the battery's status, either dead or alive.
        charge_status -- how much the battery is currently charged.
        """
        # Initialize instance variables based on arguments passed to the constructor.
        self._is_charging = is_charging
        self._current = current
        self._voltage = voltage
        self._drain = drain
        self._temperature = temperature
        self._lifespan = lifespan
        self._voltage_norm = voltage_norm
        self._voltage_min = voltage_min
        self._voltage_max = voltage_max
        self._charge_c = charge_c
        self._discharge_c = discharge_c
        self._thermal_runaway = thermal_runaway
        self._is_alive = is_alive
        self._charge_status = charge_status

    def _get_is_charging(self) -> bool:
        """Returns whether the battery is charging or not."""
        return self._is_charging

    def _set_is_charging(self, is_charging) -> None:
        """Updates the charging status of the battery."""
        self._is_charging = is_charging

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

    def _get_drain(self) -> float:
        """Returns the current charge being drawn from the battery by the phone."""
        return self._drain

    def _set_drain(self, drain) -> None:
        """Updates the current charge being drawn from the battery by the phone."""
        self._drain = drain

    def _get_temperature(self) -> float:
        """Returns the temperature of the battery."""
        return self._temperature

    def _set_temperature(self, temperature) -> None:
        """Updates the temperature of the battery."""
        self._temperature = temperature

    def _get_lifespan(self) -> int:
        """Returns the current lifespan estimate of the battery."""
        return self._lifespan

    def _set_lifespan(self, lifespan) -> None:
        """Updates the current lifespan estimate of the battery."""
        self._lifespan = lifespan

    def _get_voltage_norm(self) -> float:
        """Returns the voltage norm of the battery."""
        return self._voltage_norm

    def _set_voltage_norm(self, voltage_norm) -> None:
        """Updates the voltage norm of the battery."""
        self._voltage_norm = voltage_norm

    def _get_voltage_min(self) -> float:
        """Returns the min voltage of the battery."""
        return self._voltage_min

    def _set_voltage_min(self, voltage_min) -> None:
        """Updates the min voltage of the battery."""
        self._voltage_min = voltage_min

    def _get_voltage_max(self) -> float:
        """Returns the max voltage of the battery."""
        return self._voltage_max

    def _set_voltage_max(self, voltage_max) -> None:
        """Updates the max voltage of the battery."""
        self._voltage_max = voltage_max

    def _get_charge_c(self) -> float:
        """Returns the max charge rate of the battery."""
        return self._charge_c

    def _set_charge_c(self, charge_c) -> None:
        """Updates the max charge rate of the battery."""
        self._charge_c = charge_c

    def _get_discharge_c(self) -> float:
        """Returns the max discharge rate of the battery."""
        return self._discharge_c

    def _set_discharge_c(self, discharge_c) -> None:
        """Updates the max discharge rate of the battery."""
        self._discharge_c = discharge_c

    def _get_thermal_runaway(self) -> float:
        """Returns the thermal runaway of the battery."""
        return self._thermal_runaway

    def _set_thermal_runaway(self, thermal_runaway) -> None:
        """Updates the thermal runaway of the battery."""
        self._thermal_runaway = thermal_runaway

    def _get_is_alive(self) -> bool:
        """Returns whether the battery is alive (True) or dead (False)."""
        return self._is_alive

    def _set_is_alive(self, is_alive) -> None:
        """Updates whether the battery is alive (True) or dead (False)."""
        self._is_alive = is_alive
    
    def _get_charge_status(self) -> float:
        """Returns how much the battery is charged."""
        return self._charge_status

    def _set_charge_status(self, charge_status) -> None:
        """Updates how much the battery is charged.."""
        self._charge_status = charge_status
    # Assign all of the getters of setters to class properties.
    # This means private instance variables can be accessed "directly" by using the getters and setters as an interface.
    # E.g. my_battery.is_charging = False calls _set_is_charging(False) under the hood.
    is_charging = property(_get_is_charging, _set_is_charging)
    current = property(_get_is_charging, _set_is_charging)
    voltage = property(_get_voltage, _set_voltage)
    drain = property(_get_drain, _set_drain)
    temperature = property(_get_temperature, _set_temperature)
    lifespan = property(_get_lifespan, _set_lifespan)
    voltage_norm = property(_get_voltage_norm, _set_voltage_norm)
    voltage_min = property(_get_voltage_min, _set_voltage_min)
    voltage_max = property(_get_voltage_max, _set_voltage_max)
    charge_c = property(_get_charge_c, _set_charge_c)
    discharge_c = property(_get_discharge_c, _set_discharge_c)
    thermal_runaway = property(_get_thermal_runaway, _set_thermal_runaway)
    is_alive = property(_get_is_alive, _set_is_alive)
    charge_status = property(_get_charge_status, _set_charge_status)
