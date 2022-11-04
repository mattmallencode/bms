from typing import Type
from classes.battery import Battery
from classes.powerbrick import PowerBrick
from classes.phone import Phone

class Charger:
    def __init__(self, battery: Type[Battery], phone: Type[Phone]):
        self._battery = battery
        self._phone = phone
        self._charge_setting = None
        
    def is_powerbrick_plugged_in(self):
        if self._phone.is_charging:
            return True
        else:
            return False

    def _get_charge_setting(self):
        return self._charge_setting

    def _set_charge_setting(self, setting):
        self._charge_setting = setting

    charge_setting = property(_get_charge_setting, _set_charge_setting)