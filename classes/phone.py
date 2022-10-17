import tkinter

# Class representing the state of a phone.
class Phone:
    def __init__(self, powered_on: bool, display_on: bool, locked: bool) -> None:
        """
        Initializes an instance of the Phone class based on the arguments you pass to this constructor.

        Keyword arguments:
        powered_on -- bool indicating whether the phone is currently powered on.
        display_on -- bool indicating whether the phone's screen / display is turned on.
        locked -- bool indicating whether the phone is currently locked.
        """
        # Initialize instance variables based on arguments passed to the constructor.
        self._powered_on = powered_on
        self._display_on = display_on
        self._locked = locked

        self._root = tkinter.Tk()
        self._root.title("Phone")

        self._size = {"x":300, "y":550}
        self._radius = 50
        self._top_corner = {"x":5, "y":5}
        self._bar = {"x":100, "y":20}
        self._button_radius = 50

        # phone body
        self.Canvas = tkinter.Canvas(self._root, bg="white", width=self._size["x"], height=self._size["y"])
        self.Canvas.create_rectangle(self._radius, self._top_corner["y"], self._size["x"]-self._radius, self._size["y"], fill="black", outline="black")
        self.Canvas.create_rectangle(self._top_corner["x"], self._radius, self._size["x"], self._size["y"]-self._radius, fill="black", outline="black")
        self.Canvas.create_oval(self._top_corner["x"], self._top_corner["y"], (self._radius*2), (self._radius*2), fill="black", outline="black")
        self.Canvas.create_oval((self._size["x"]-(self._radius*2)), self._top_corner["y"], self._size["x"], (self._radius*2), fill="black", outline="black")
        self.Canvas.create_oval(self._top_corner["x"], (self._size["y"]-(self._radius*2)), (self._radius*2), self._size["y"], fill="black", outline="black")
        self.Canvas.create_oval((self._size["x"]-(self._radius*2)), (self._size["y"]-(self._radius*2)), self._size["x"], self._size["y"], fill="black", outline="black") 

        # screen
        self.Canvas.create_rectangle((self._radius/5)+self._top_corner["x"], (self._radius*1.5)+self._top_corner["y"], (self._size["x"]-(self._radius/5)), (self._size["y"]-(self._radius*1.5)), fill="grey16", outline="black")

        # top speaker
        self.Canvas.create_rectangle(((self._size["x"]*0.5)-(self._bar["x"]*0.5))+self._top_corner["x"], ((self._size["y"]*0.08)-(self._bar["y"]*0.5))+self._top_corner["y"], ((self._size["x"]*0.5)+(self._bar["x"]*0.5)), ((self._size["y"]*0.08)+(self._bar["y"]*0.5)), fill="grey12", outline="black")

        # bottom button
        self.button = self.Canvas.create_oval(((self._size["x"]*0.5)-(self._button_radius*0.5))+self._top_corner["x"], ((self._size["y"]*0.925)-(self._button_radius*0.5))+self._top_corner["y"], ((self._size["x"]*0.5)+(self._button_radius*0.5)), ((self._size["y"]*0.925)+(self._button_radius*0.5)), fill="grey30", outline="black")
        self.Canvas.create_rectangle(((self._size["x"]*0.5)-((self._button_radius/1.5)*0.5))+self._top_corner["x"], ((self._size["y"]*0.925)-((self._button_radius/1.5)*0.5))+self._top_corner["y"], ((self._size["x"]*0.5)+((self._button_radius/1.5)*0.5)), ((self._size["y"]*0.925)+((self._button_radius/1.5)*0.5)), outline="black")
        self.Canvas.bind("<Button-1>", self._press)

        self.Canvas.pack()
        self._root.mainloop()

    def _press(self, event):
        """Handles button clicks ont he "screen" """
        # home button
        if ((((self._size["x"]*0.5)-(self._button_radius*0.5))+self._top_corner["x"]) < event.x) and ((((self._size["y"]*0.925)-(self._button_radius*0.5))+self._top_corner["y"]) < event.y) and (((self._size["x"]*0.5)+(self._button_radius*0.5)) > event.x) and (((self._size["y"]*0.925)+(self._button_radius*0.5)) > event.y):
            self._set_display_on(True)
            self.Canvas.create_rectangle((self._radius/5)+self._top_corner["x"], (self._radius*1.5)+self._top_corner["y"], (self._size["x"]-(self._radius/5)), (self._size["y"]-(self._radius*1.5)), fill="white", outline="black")
            self.Canvas.create_text(self._size["x"]/2, self._size["y"]/2, fill="black", text="Phone is on\nthis is where inside\ndetails will go!")
        elif self._get_display_on == True:
            if ((self._radius/5)+self._top_corner["x"] < event.x) and ((self._radius*1.5)+self._top_corner["y"] < event.y) and ((self._size["x"]-(self._radius/5)) > event.x) and ((self._size["y"]-(self._radius*1.5)) > event.y):
                print("pog")
    

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
    # Assign all of the getters to class properties. No setters as all of the class' attribtutes are constants.
    # This means private instance variables can be accessed "directly" by using the getters and setters as an interface.
    # E.g. my_phone.powered_on = False calls _set_powered_on(False) under the hood.
    powered_on = property(_get_powered_on, _set_powered_on)
    display_on = property(_get_display_on, _set_display_on)
    locked = property(_get_locked, _set_locked)


if __name__ == "__main__":
    Phone(True, False, False)