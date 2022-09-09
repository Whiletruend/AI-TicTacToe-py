# Imports
import tkinter as tk
from src.game.gameplay import Gameplay


# Frame class
class Frame:
    # Construct (init)
    def __init__(self, title, size):
        self.title = title
        self.size = size
        self.buttons_Array = []

    # Show func
    def show(self):
        # Variables
        inc = 0

        # Frame
        Game_Frame = tk.Tk()
        Game_Frame.geometry(self.size)
        Game_Frame.title(self.title)
        Game_Frame.resizable(False, False)

        # Buttons (9)
        for i in range(3):
            for j in range(3):
                inc = inc + 1

                if inc % 2 == 0:
                    new_text = "X"
                else:
                    new_text = "O"

                self.buttons_Array.append(tk.Button(Game_Frame, text=new_text, width=15, height=7))
                self.buttons_Array[inc - 1].grid(row=i, column=j)

        # Show the frame
        Game_Frame.mainloop()
