import config

def adjust_lifespan(dif_in_soc: float) -> float:
    ''' 
    Adjusts the lifespan of the battery according to how many full charge cycles it has gone through.
    A lithium ion battery retains 80% of its original capacity after 500 charge cycles.
    So, this means that per charge cycle the capacity should reduce by 0.04 percent per charge cycle or 0.0004% for every 1% of discharge.
    The above is taken from Apple (will reference properly later).

    Keyword arguments:
    charger -- the charger of the MS.
    dif_in_soc -- the difference in SoC before discharge was called, and after discharge was called.

    Returns the adjusted lifespan of the battery.
    '''
    config.lifespan -= ((0.0004 * dif_in_soc) / 100)