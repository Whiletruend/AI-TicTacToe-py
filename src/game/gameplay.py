# Imports

# Gameplay class
class Gameplay:
    # Construct (init)
    def __init__(self):
        self.current_mark = ""
        self.actual_try = 0

    # Show func
    def Button_Click(self, button):
        self.actual_try = self.actual_try + 1

        if self.actual_try % 2 == 0:
            self.current_mark = "x"
        else:
            self.current_mark = "o"

        button.configure(text=self.current_mark)
