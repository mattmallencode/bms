# bms model
This battery management system is modeled in python with a tkinter interface. Using the config.py file any lithium type battery can be modeled as long as it follows the charging cadence: trickle charge, constant current, constant voltage.

## classes
This folder is for any "object" that is not the management system, namely the battery class, charger class, phone, and powerbrick class.

## ms_modules
This folder is for all of the different "modules" of the management system: charging, health, and metrics. Its functions all make up the management system.

## tests
The tests verify that the implementation that we created. This ensures that the code we wrote does as we intended.

## config
This file is for all the constants and global variables needed by the MS and phone GUI

## main
This is where the model is run. Where the objects are instanciated and the while loop for the Tkinter is run.