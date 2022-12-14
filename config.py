# https://www.aliexpress.com/item/1005002877506257.html?spm=a2g0o.productlist.0.0.9b4551fdEulDv5&algo_pvid=8c6cf013-c144-455b-ad81-7fe01dc505a4&algo_exp_id=8c6cf013-c144-455b-ad81-7fe01dc505a4-0&pdp_ext_f=%7B%22sku_id%22%3A%2212000022586204386%22%7D&pdp_npi=2%40dis%21EUR%2111.93%219.54%21%21%21%21%21%40210318b816684264364232188e374e%2112000022586204386%21sea&curPageLogUid=fgLi3LoKrm6H
from time import time

# At this voltage the battery is dead, trending towards this voltage indicates a lower capacity.
VOLTAGE_MIN: float = 3.0
# If voltage trends towards this value, it leads to degradation.
VOLTAGE_MAX: float = 4.2
# Max rate of charge.
CHARGE_C: float = 0.25
# Max rate of discharge.
DISCHARGE_C: float = 1
# The threshold of the current when battery is fully charged
THRESHOLD: float = 0
# The battery's status, either dead or alive. 
BATTERY_ALIVE: bool = True
# The original capacity of the battery.
CAPACITY: float = 2400
# Estimate of how many full charge and discharge cycles the battery can handle before it begins to lose functional capacity.
lifespan: float = 1
# variable to hold charge percent
chargepercent: int = 0
# variable to hold Time Till Full
ttf: float = 0.5
# variable to hold Time Till Empty
tte: float = 3.4
# constant for current from power brick.
POWER_BRICK_CURRENT: int = 2
# constant for voltage from power brick.
POWER_BRICK_VOLTAGE: int = 5
# variable to hold time since the last state of charge was calculated
time_since_last_soc_calculation = time()
time_of_last_ttf: time = time()
last_soc_ttf: float = chargepercent - 0.01
time_of_last_tte: time = time()
last_soc_tte: float = chargepercent + 0.01
POWERDRAWSCREENOFF = 0.1

POWERDRAWSCREENON = 0.1

POWERDRAWMAX = 0.1


THRESHHOLDPRECENTAGE = 5