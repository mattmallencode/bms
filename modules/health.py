# Estimate of how many full charge and discharge cycles the battery can handle before it begins to lose functional capacity.
LIFESPAN: int
# Importing the Charger class from the charger.py folder
from classes.charger import Charger
# Import everything from metrics
from metrics import *

def lifespan(charger: type[Charger], discharge_c: float, thermal_runaway: float, temperture_norm: float) -> int:
    ''' 
    State of health capacity of battery = Total capacity ( ah ) / Begining of life capacity ( ah )
    The BOL capacity for iPhone 13 Pro Max = 4352 mAH

    For each charging cycle the total capacity decreases 

    The resistence within the battery goes up ( Impedence ). with each cycle.

    Charge left in the battery = TTE * SOC 

    With each cycle I wil decrease the Total capacity by 0.5

    A cycle = When enough charge has flowed from the powerbrick to equal the total capacity of the battery.
    '''
    
    pass