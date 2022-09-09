# Imports
import tkinter as tk
from src.game.gameplay import Gameplay


# Frame class
class Frame:
    # Construct (init)
    def __init__(self, title, size):
        self.title = title
        self.size = size
        self.gameplay = Gameplay()
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

        # Board
        Game_Board = tk.Frame(Game_Frame, width=350, height=350)

        # Buttons (9)
        for i in range(3):
            for j in range(3):
                inc = inc + 1

                self.buttons_Array.append(tk.Button(Game_Board, text="", width=15, height=7))
                self.buttons_Array[inc - 1].configure(command=lambda: self.gameplay.Button_Click(self.buttons_Array[inc - 1]))
                self.buttons_Array[inc - 1].grid(row=i, column=j)

        # Show the frame
        Game_Board.pack(padx=10, pady=25)
        Game_Frame.mainloop()
