from easy_tui import loop, LAST_COL, LAST_ROW
from calculator.views import *
from calculator.models import RomanCalculation
from simple_roman_numbers import RomanNumber

class Calculator:
    def __init__(self):
        f0 = (LAST_ROW - 20) // 2
        c0 = (LAST_COL - 17) // 2
        self.display = Display(fila=f0, col=c0)
        self.keyboard = Keyboard(output=self.receive, col=c0, fila = f0 + 4)
        self.calculation = RomanCalculation()
        self.resetDisplay = False
        self.keyboard_buffer = ""
        

    def receive(self, key):
        if key in tuple(self.calculation.operators):
            if self.keyboard_buffer:
                self.calculation.receive(self.keyboard_buffer)
                self.keyboard_buffer = ""
            self.calculation.receive(key)
            self.display.value = RomanNumber(self.calculation.display).lit
        else:
            buffer = self.keyboard_buffer + key
            try:
                value = RomanNumber(buffer)
                self.keyboard_buffer += key
                self.display.value = str(value)
            except ValueError:
                pass

    def start(self):
        loop()

