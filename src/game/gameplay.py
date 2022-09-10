# Imports
import math
from tabulate import tabulate


# Gameplay class
class Gameplay:
    # Construct (init)
    def __init__(self):
        self.current_mark = "X"
        self.buttons_clicked = []
        self.actual_board = []
        self.actual_try = 0

        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.actual_board.append(row)

    # Button Click func
    def Button_Click(self, button_id, buttons_array):
        if buttons_array[button_id - 1] in self.buttons_clicked:
            pass
        else:
            # Increment the actual tries var
            self.actual_try = self.actual_try + 1

            # To get the actual row of the clicked button, I just divide it by 3, for the row I just use a modulo 3,
            # so I instantly get the right row. (need to math.ceil because values are often like 0.3333333)
            row = (button_id - 1) % 3
            col = math.ceil(button_id / 3)

            # Check if someone won when tries hit 5
            if self.actual_try >= 5:
                self.Win_Check()

            # Add the clicked button object to the array (list) and change the current text by the current mark instead
            buttons_array[button_id - 1].configure(text=self.current_mark)
            self.buttons_clicked.append(buttons_array[button_id - 1])

            # Add the current mark to the "actual board" array
            self.actual_board[col - 1][row] = self.current_mark

            # Know if it's actually X or O by using a modulo
            if self.actual_try % 2 == 0:
                self.current_mark = "X"
            else:
                self.current_mark = "O"

            # Test
            print(tabulate(self.actual_board, headers=['1', '2', '3']))

    # Check if there's a winner
    def Win_Check(self):
        pass
