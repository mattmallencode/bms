import tkinter
import config

""" use properties dont change self.X """


# Class representing the state of a phone.
class Phone:
    def __init__(self, powered_on: bool, display_on: bool, locked: bool, is_charging: bool, power_draw: float) -> None:
        """
        Initializes an instance of the Phone class based on the arguments you pass to this constructor.

        Keyword arguments:
        powered_on -- bool indicating whether the phone is currently powered on.
        display_on -- bool indicating whether the phone's screen / display is turned on.
        locked -- bool indicating whether the phone is currently locked.
        is_charging -- bool indicating whether the charger is plugged in 
        power_draw -- how much voltage should be decreased per second.
        """
        # Initialize instance variables based on arguments passed to the constructor.
        self._powered_on = powered_on
        self._display_on = display_on
        self._locked = locked
        self._is_charging = is_charging
        self._power_draw = power_draw
        self._is_dead = False
        self._settings = False

        self._root = tkinter.Tk()
        self._root.title("Phone")
        
        self._timetill = tkinter.StringVar(self._root)
        
        self._canvas_size = {"x":300, "y":550}
        self._bevel_radius = 50
        self._top_corner = {"x":10, "y":10}
        self._bar_size = {"x":100, "y":20}
        self._home_button_radius = 50
        self._power_button_size = {"x":5, "y":50}
        self._notification_pannel_height = 20
        self._connector_size = {"x":50, "y":100}
        self._unlock_button_size = {"x":100, "y":75}
        self._lock_button_size = {"x":100, "y":75}
        self._settings_button_size = {"x":50, "y":50}
        self._settings_return_button_size = {"x":50, "y":50}
        #self._middle_x = self._screen_corners["X2"] - self._screen_corners["X1"]
        #self._middle_y = self._screen_corners["Y2"] - self._screen_corners["Y1"]

        # corners = {"X1":, "Y1":, "X2":, "Y2":}
        self._screen_corners = {"X1":(self._bevel_radius/5)+self._top_corner["x"], "Y1":(self._bevel_radius*1.5)+self._top_corner["y"], "X2":(self._canvas_size["x"]-(self._bevel_radius/5)), "Y2":(self._canvas_size["y"]-(self._bevel_radius*1.5))}
        self._home_button_corners = {"X1":(((self._canvas_size["x"]/2)-(self._home_button_radius/2))+self._top_corner["x"]), "Y1":(((self._canvas_size["y"]*0.925)-(self._home_button_radius/2))+self._top_corner["y"]), "X2":((self._canvas_size["x"]/2)+(self._home_button_radius/2)), "Y2":((self._canvas_size["y"]*0.925)+(self._home_button_radius/2))}
        self._power_button_corners = {"X1":self._canvas_size["x"], "Y1":self._bevel_radius+100, "X2":self._canvas_size["x"]+self._power_button_size["x"], "Y2":self._bevel_radius+100+self._power_button_size["y"]}
        self._notification_pannel_corners = {"X1":(self._bevel_radius/5)+self._top_corner["x"], "Y1":(self._bevel_radius*1.5)+self._top_corner["y"], "X2":(self._canvas_size["x"]-(self._bevel_radius/5)), "Y2":(self._bevel_radius*1.5)+self._top_corner["y"]+self._notification_pannel_height}
        self._connector_corners = {"X1":((self._canvas_size["x"]/2)-(self._connector_size["x"]/2)+self._top_corner["x"]/2), "Y1":self._canvas_size["y"], "X2":((self._canvas_size["x"]/2)+(self._connector_size["x"]/2))+self._top_corner["x"]/2, "Y2":(self._canvas_size["y"])+(self._connector_size["x"])}
        self._unlock_button = {"X1":((self._canvas_size["x"]/2)-(self._unlock_button_size["x"]/2)+self._top_corner["x"]/2), "Y1":self._canvas_size["y"]*2/3, "X2":((self._canvas_size["x"]/2)+(self._unlock_button_size["x"]/2))+self._top_corner["x"]/2, "Y2":(self._canvas_size["y"]*2/3)+self._unlock_button_size["y"]} 
        self._lock_button = {"X1":((self._canvas_size["x"]/2)-(self._lock_button_size["x"]/2)+self._top_corner["x"]/2), "Y1":self._canvas_size["y"]*2/3, "X2":((self._canvas_size["x"]/2)+(self._lock_button_size["x"]/2))+self._top_corner["x"]/2, "Y2":(self._canvas_size["y"]*2/3)+self._lock_button_size["y"]} 
        self._settings_button = {"X1":((self._canvas_size["x"]/2)-(self._settings_button_size["x"]/2)+self._top_corner["x"]/2), "Y1":((self._canvas_size["x"]/2)-(self._settings_button_size["y"]/2)+self._top_corner["x"]/2), "X2":((self._canvas_size["x"]/2)+(self._settings_button_size["x"]/2))+self._top_corner["x"]/2, "Y2":((self._canvas_size["x"]/2)+(self._settings_button_size["y"]/2)+self._top_corner["x"]/2)} 
        self._settings_return_button = {"X1":((self._canvas_size["x"]/2)-(self._settings_return_button_size["x"]/2)+self._top_corner["x"]/2), "Y1":((self._canvas_size["x"]/2)-(self._settings_return_button_size["y"]/2)+self._top_corner["x"]/2), "X2":((self._canvas_size["x"]/2)+(self._settings_return_button_size["x"]/2))+self._top_corner["x"]/2, "Y2":((self._canvas_size["x"]/2)+(self._settings_return_button_size["y"]/2)+self._top_corner["x"]/2)} 


        self._canvas = tkinter.Canvas(self._root, bg="white", width=self._canvas_size["x"]+self._power_button_size["x"], height=self._canvas_size["y"]+self._connector_size["x"])
        self._canvas.bind("<Button-1>", self._press)

        # phone body
        self._canvas.create_rectangle(self._bevel_radius, self._top_corner["y"], self._canvas_size["x"]-self._bevel_radius, self._canvas_size["y"], fill="black", outline="black")
        self._canvas.create_rectangle(self._top_corner["x"], self._bevel_radius, self._canvas_size["x"], self._canvas_size["y"]-self._bevel_radius, fill="black", outline="black")
        self._canvas.create_oval(self._top_corner["x"], self._top_corner["y"], (self._bevel_radius*2), (self._bevel_radius*2), fill="black", outline="black")
        self._canvas.create_oval((self._canvas_size["x"]-(self._bevel_radius*2)), self._top_corner["y"], self._canvas_size["x"], (self._bevel_radius*2), fill="black", outline="black")
        self._canvas.create_oval(self._top_corner["x"], (self._canvas_size["y"]-(self._bevel_radius*2)), (self._bevel_radius*2), self._canvas_size["y"], fill="black", outline="black")
        self._canvas.create_oval((self._canvas_size["x"]-(self._bevel_radius*2)), (self._canvas_size["y"]-(self._bevel_radius*2)), self._canvas_size["x"], self._canvas_size["y"], fill="black", outline="black") 
        # screen
        self._screen_state()

        # top speaker
        self._canvas.create_rectangle(((self._canvas_size["x"]*0.5)-(self._bar_size["x"]*0.5))+self._top_corner["x"], ((self._canvas_size["y"]*0.08)-(self._bar_size["y"]*0.5))+self._top_corner["y"], ((self._canvas_size["x"]*0.5)+(self._bar_size["x"]*0.5)), ((self._canvas_size["y"]*0.08)+(self._bar_size["y"]*0.5)), fill="grey12", outline="black")
        # bottom button
        self._home_button = self._canvas.create_oval(self._home_button_corners["X1"], self._home_button_corners["Y1"], self._home_button_corners["X2"], self._home_button_corners["Y2"], fill="grey30", outline="black")
        self._canvas.create_rectangle(((self._canvas_size["x"]*0.5)-((self._home_button_radius/1.5)*0.5))+self._top_corner["x"], ((self._canvas_size["y"]*0.925)-((self._home_button_radius/1.5)*0.5))+self._top_corner["y"], ((self._canvas_size["x"]*0.5)+((self._home_button_radius/1.5)*0.5)), ((self._canvas_size["y"]*0.925)+((self._home_button_radius/1.5)*0.5)), outline="black")
        # Power button
        self._power_button = self._canvas.create_rectangle(self._power_button_corners["X1"], self._power_button_corners["Y1"], self._power_button_corners["X2"], self._power_button_corners["Y2"], fill="grey40", outline="grey30")
        # charger icon
        self._charging_set()

        self._canvas.pack()


    def _screen_state(self):
        if self._powered_on and not self.display_on:
            self._on_screen()
        elif self._display_on:
            if self._locked:
                self._lock_screen()
            else:
                if self._settings:
                    self._settings_screen()
                else:
                    self._home_screen()
        else:
            self._off_screen()

    def _press(self, event):
        #print("powered_on", self._powered_on, "|display_on", self.display_on, "|locked", self._locked, "|is_charging", self._is_charging, "|power_draw", self._power_draw, "|settings", self._settings)

        """ Handles clicks on the canvas """
        # power button
        if (self._power_button_corners["X1"] < event.x) and (self._power_button_corners["Y1"] < event.y) and (self._power_button_corners["X2"] > event.x) and (self._power_button_corners["Y2"] > event.y) and not self._is_dead:
            if self.powered_on:
                self._display_on = False
                self._powered_on = False
                self._locked = True
                self._power_draw = 0
                self._off_screen()
            else:
                self._powered_on = True
                self._power_draw = config.POWERDRAWSCREENON
                self._on_screen()
            return self.powered_on

        # Charger toggle
        elif (self._connector_corners["X1"] < event.x) and (self._connector_corners["Y1"] < event.y) and (self._connector_corners["X2"] > event.x) and (self._connector_corners["Y2"] > event.y):
            if self.is_charging:
                self.is_charging = False
            else:
                self.is_charging = True
            self._charging_set()
            return self.is_charging
            
        # home button
        elif (self._home_button_corners["X1"] < event.x) and (self._home_button_corners["Y1"] < event.y) and (self._home_button_corners["X2"] > event.x) and (self._home_button_corners["Y2"] > event.y) and self._powered_on:
            if self._display_on == True:
                self.display_on = False
                self._locked = True
                self._settings = False
                
            else:
                self._display_on = True
            self._screen_state()
            return self.display_on

        # Handles button clicks on the "screen" 
        elif self._display_on == True:
             # unlock button pressed when phone is on 
            if (self._unlock_button["X1"] < event.x) and (self._unlock_button["Y1"] < event.y) and (self._unlock_button["X2"] > event.x) and (self._unlock_button["Y2"] > event.y) and self._locked:
                self._locked = False
                self._home_screen()
                return self.locked
            
            # lock button pressed in homescreen 
            elif (self._lock_button["X1"] < event.x) and (self._lock_button["Y1"] < event.y) and (self._lock_button["X2"] > event.x) and (self._lock_button["Y2"] > event.y) and not self._locked:
                self._locked = True
                self._lock_screen()
                return self.locked
            
            # settings button pressed in homescreen
            elif (self._settings_button["X1"] < event.x) and (self._settings_button["Y1"] < event.y) and (self._settings_button["X2"] > event.x) and (self._settings_button["Y2"] > event.y) and not self._locked and not self._settings:
                self._settings = True
                self._settings_screen()
                return self._settings
            
            # return button pressed in settings -> go back to homescreen
            elif (self._settings_button["X1"] < event.x) and (self._settings_button["Y1"] < event.y) and (self._settings_button["X2"] > event.x) and (self._settings_button["Y2"] > event.y) and not self._locked and self._settings:
                self._settings = False
                self._locked = False
                self._home_screen()
                return self.locked

        #print("powered_on", self._powered_on, "|display_on", self.display_on, "|locked", self._locked, "|is_charging", self._is_charging, "|power_draw", self._power_draw)

    def _off_screen(self):
        self._canvas.create_rectangle(self._screen_corners["X1"], self._screen_corners["Y1"], self._screen_corners["X2"], self._screen_corners["Y2"], fill="grey10", outline="black")
        self._canvas.create_text(self._canvas_size["x"]/2, self._canvas_size["y"]/2, fill="black", text="OFF", font="Helvetica 40 bold")

    def _on_screen(self):
        self._canvas.create_rectangle(self._screen_corners["X1"], self._screen_corners["Y1"], self._screen_corners["X2"], self._screen_corners["Y2"], fill="grey16", outline="black")
        self._canvas.create_text(self._canvas_size["x"]/2, self._canvas_size["y"]/2, fill="black", text="ON", font="Helvetica 40 bold")
    
    def _lock_screen(self):
        """Handles lock screen"""
        self._canvas.create_rectangle(self._screen_corners["X1"], self._screen_corners["Y1"], self._screen_corners["X2"], self._screen_corners["Y2"], fill="white", outline="black")
        self._notification_pannel = self._canvas.create_rectangle(self._notification_pannel_corners["X1"], self._notification_pannel_corners["Y1"], self._notification_pannel_corners["X2"], self._notification_pannel_corners["Y2"], fill="red", outline="black")
        # display ttf plugged in or tte when not
        self._canvas.create_text(self._canvas_size["x"]/2, self._canvas_size["y"]/2, fill="green3", text=self._timetill.get(), font="Helvetica 12")

        # unlock button
        self._canvas.create_rectangle(self._unlock_button["X1"], self._unlock_button["Y1"], self._unlock_button["X2"], self._unlock_button["Y2"], fill="medium purple", outline="black")
        self._canvas.create_text(self._unlock_button["X1"]+(self._unlock_button_size["x"]/2), self._unlock_button["Y1"]+(self._unlock_button_size["y"]/2), fill="pale green", text="unlock", font="Helvetica 12")


    def _home_screen(self):
        """Handles home screen"""
        self._canvas.create_rectangle(self._screen_corners["X1"], self._screen_corners["Y1"], self._screen_corners["X2"], self._screen_corners["Y2"], fill="steelblue1", outline="black")

        # lock button
        self._canvas.create_rectangle(self._lock_button["X1"], self._lock_button["Y1"], self._lock_button["X2"], self._lock_button["Y2"], fill="pale green", outline="black")
        self._canvas.create_text(self._lock_button["X1"]+(self._lock_button_size["x"]/2), self._lock_button["Y1"]+(self._lock_button_size["y"]/2), fill="medium purple", text="lock", font="Helvetica 12")

        # settings button
        self._canvas.create_rectangle(self._settings_button["X1"], self._settings_button["Y1"], self._settings_button["X2"], self._settings_button["Y2"], fill="DarkOrange1", outline="black")
        self._canvas.create_text(self._settings_button["X1"]+(self._settings_button_size["x"]/2), self._settings_button["Y1"]+(self._settings_button_size["y"]/2), fill="thistle1", text="settings", font="Helvetica 12")

    def _settings_screen(self):
        """Handles settings screen"""
        self._canvas.create_rectangle(self._screen_corners["X1"], self._screen_corners["Y1"], self._screen_corners["X2"], self._screen_corners["Y2"], fill="green yellow", outline="black")
        self._canvas.create_text(self._canvas_size["x"]/2, self._canvas_size["y"]/2, fill="black", text=f"Battery at {round(config.chargepercent, 2)}%\n\nBattery Health: {round(config.lifespan, 2)}", font="Helvetica 16 bold")

        # return button
        self._canvas.create_rectangle(self._settings_return_button["X1"], self._settings_return_button["Y1"], self._settings_return_button["X2"], self._settings_return_button["Y2"], fill="thistle1", outline="black")
        self._canvas.create_text(self._settings_return_button["X1"]+(self._settings_return_button_size["x"]/2), self._settings_return_button["Y1"]+(self._settings_return_button_size["y"]/2), fill="DarkOrange1", text="return", font="Helvetica 12")

    def _charging_set(self):
        if self._is_charging:
            self._timetill.set(f"battery full in\n {self._hours_minutes_seconds(config.ttf)} hours")
            self._connector = self._canvas.create_rectangle(self._connector_corners["X1"], self._connector_corners["Y1"], self._connector_corners["X2"], self._connector_corners["Y2"], fill="green3", outline="black")
        else:
            self._timetill.set(f"battery dead in\n {self._hours_minutes_seconds(config.tte)} hours")
            self._connector = self._canvas.create_rectangle(self._connector_corners["X1"], self._connector_corners["Y1"], self._connector_corners["X2"], self._connector_corners["Y2"], fill="red3", outline="black")
        self._screen_state()

    def _hours_minutes_seconds(self, hours:float) -> str:
        min = hours - int(hours)
        min = int(min * 60)
        hoursMin = f"{int(hours)} hours and {min} minutes"
        return hoursMin

    """ Getters / Setters ------------------------------------------------------------------------ """
    def _get_powered_on(self) -> bool:
        """Returns whether the phone is powered on or not."""
        return self._powered_on

    def _set_powered_on(self, true_or_false: bool) -> None:
        """Updates whether the phone is powered on or not."""
        self._powered_on = true_or_false

    def _get_display_on(self) -> bool:
        """Returns whether the phone's display is turned on or not."""
        return self._display_on

    def _set_display_on(self, true_or_false: bool) -> None:
        """Updates whether the phone's display is turned on or not."""
        self._display_on = true_or_false

    def _get_locked(self) -> bool:
        """Returns whether the phone is locked or not."""
        return self._locked

    def _set_locked(self, true_or_false: bool) -> None:
        """Updates whether the phone is locked or not."""
        self._locked = true_or_false

    def _get_is_charging(self) -> bool:
        """Returns whether the phone is charging or not."""
        return self._is_charging

    def _set_is_charging(self, true_or_false: bool) -> None:
        """Updates whether the phone is charging or not."""
        self._is_charging = true_or_false
    
    def _get_power_draw(self) -> float:
        """Returns the power the phone is drawing."""
        return self._power_draw
    
    def _set_power_draw(self, power_draw: float) -> None:
        """Updates the phone's power draw."""
        self._power_draw = power_draw

    def _get_is_dead(self) -> bool:
        """Returns whether the phone is alive or dead."""
        return self._is_dead

    def _set_is_dead(self, _is_dead) -> None:
        """Updates whether the phone is alive or dead."""
        self._is_dead = _is_dead

    # Assign all of the getters to class properties. No setters as all of the class' attribtutes are constants.
    # This means private instance variables can be accessed "directly" by using the getters and setters as an interface.
    # E.g. my_phone.powered_on = False calls _set_powered_on(False) under the hood.
    powered_on = property(_get_powered_on, _set_powered_on)
    display_on = property(_get_display_on, _set_display_on)
    locked = property(_get_locked, _set_locked)
    is_charging = property(_get_is_charging, _set_is_charging)
    power_draw = property(_get_power_draw, _set_power_draw)
    is_dead = property(_get_is_dead, _get_is_dead)

if __name__ == "__main__":
    P = Phone(False, False, True, False, 5.0)
    while True:
        P._root.update_idletasks()
        P._root.update()
        # https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop