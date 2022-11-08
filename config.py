# The optimum voltage for this battery, should be trended towards to minimize battery degradation.
VOLTAGE_NORM: float
# At this voltage the battery is dead, trending towards this voltage indicates a lower capacity.
VOLTAGE_MIN: float
# If voltage trends towards this value, it leads to degradation.
VOLTAGE_MAX: float
# Max rate of charge.
CHARGE_C: float
# Max rate of discharge.
DISCHARGE_C: float
# The temperature at which the battery will keep increasing in temperature and go on fire.
THERMAL_RUNAWAY: float
# The battery's status, either dead or alive.
BATTERY_ALIVE: bool
# The original capacity of the battery.
CAPACITY: float = 4352
# The threshold of the current when battery is fully charged
THRESHOLD: float

