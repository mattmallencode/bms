# The optimum voltage for this battery, should be trended towards to minimize battery degradation.
VOLTAGE_NORM: float = 3.6
# At this voltage the battery is dead, trending towards this voltage indicates a lower capacity.
VOLTAGE_MIN: float = 3
# If voltage trends towards this value, it leads to degradation.
VOLTAGE_MAX: float = 4.2
# Max rate of charge.
CHARGE_C: float = 1
# Max rate of discharge.
DISCHARGE_C: float = 1
# The temperature at which the battery will keep increasing in temperature and go on fire.
THERMAL_RUNAWAY: float = 105
# The battery's status, either dead or alive. 
BATTERY_ALIVE: bool = True
# The original capacity of the battery.
CAPACITY: float = 4352
# The threshold of the current when battery is fully charged
THRESHOLD: float = 0.05
# Estimate of how many full charge and discharge cycles the battery can handle before it begins to lose functional capacity.
lifespan: float = 1