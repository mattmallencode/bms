def lifespan(temperture: float, temperture_norm: float, voltage: float, current: float, discharge_c: float, thermal_runaway: float) -> int:
    ''' 
    The degradation of the lifespan of the battery is affected by multiple factors.
    These include:
        temperture
        voltage in and out 
        current 
        the rate of charge / discharge 

    The higher the voltage and current in the faster the rate of charge.
    Temperture is self explanatory 
    The rate of discharge will affect the lifespan.

    important:

        I have added in a variable that does not exist yet in the class and that is the temperture_norm of the battery 
        I have also stated type hinted that the return type will be an int as that is what the lifespan will be represented by.
    '''
    pass