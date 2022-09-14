# Imports
import tkinter as tk
from src.game.gameplay import Gameplay


# Frame class
class Frame:
    # Construct (init)
    def __init__(self, title, size):
        self.title: str = title
        self.size: str = size
        self.gameplay: Gameplay = Gameplay()
        self.buttons_List: list = []

    # Show func
    def show(self):
        # Variables
        inc: int = 0
        self.gameplay.game_running: bool = True

        # Frame
        Game_Frame: tk = tk.Tk()
        Game_Frame.geometry(self.size)
        Game_Frame.title(self.title)
        Game_Frame.resizable(False, False)

        # Board
        Game_Board: tk = tk.Frame(Game_Frame, width=350, height=350)

        # Buttons (9)
        for i in range(3):
            for j in range(3):
                inc: int = inc + 1

                self.buttons_List.append(tk.Button(Game_Board, text="", width=15, height=7))
                self.buttons_List[inc - 1].configure(command=lambda button_id=inc: self.gameplay.Button_Click(button_id, self.buttons_List))
                self.buttons_List[inc - 1].grid(row=i, column=j)

        # Show the frame
        Game_Board.pack(padx=10, pady=25)
        Game_Frame.mainloop()