# Imports

# Gameplay class
class Gameplay:
    # Construct (init)
    def __init__(self):
        self.current_mark = "x"
        self.buttons_clicked = []
        self.actual_try = 0

    # Button Click func
    def Button_Click(self, button_id, buttons_array):
        if buttons_array[button_id - 1] in self.buttons_clicked:
            pass
        else:
            self.actual_try = self.actual_try + 1

            buttons_array[button_id - 1].configure(text=self.current_mark)
            self.buttons_clicked.append(buttons_array[button_id - 1])

            if self.actual_try % 2 == 0:
                self.current_mark = "x"
            else:
                self.current_mark = "o"
