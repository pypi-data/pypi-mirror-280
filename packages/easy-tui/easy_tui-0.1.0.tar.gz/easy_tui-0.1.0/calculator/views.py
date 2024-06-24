from easy_tui import controls
import easy_tui as sTUI

teclas = ['M', '•', '/', 'C', 'D', '*', 'X', 'L', '-', 'I', 'V', '+']

class CalcButton(controls.KeyButton):
    def __init__(self, col, fila, key, command):
        super().__init__(col, fila, key, command)

    @controls.click_animate
    def draw(self):
        limit = "+-----+"
        middle = "|     |"
        sTUI.locate(self.col, self.fila, limit)
        sTUI.locate(self.col, self.fila+1, middle)
        sTUI.locate(self.col, self.fila+2, f"|  {self.label}  |")
        sTUI.locate(self.col, self.fila+3, middle)
        sTUI.locate(self.col, self.fila+4, limit)


class Display(controls.Label):
    def __init__(self, col, fila):
        super().__init__(col, fila, ">")
        self.value = ""

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, v: str):
        self._value = v
        self.text = f"> {v:>15s}"

    def draw(self):
        sTUI.locate(self.col, self.fila,     "+-----------------+")
        sTUI.locate(self.col, self.fila + 1, "|                 |")
        sTUI.locate(self.col, self.fila + 2, f"|{self.text}|")
        sTUI.locate(self.col, self.fila + 3, "|                 |")
        sTUI.locate(self.col, self.fila + 4, "+-----------------+")
    

class Keyboard:
    def __init__(self, col=0, fila=0, output=None):
        teclas = ['M', '•', '/', 'C', 'D', '*', 'X', 'L', '-', 'I', 'V', '+']
        ix = 0
        f0 = fila
        c0 = col

        self.output = output

        def make_fn(key):
            return lambda: self.send(key)
            
        for fila in range(4):
            for col in range(3):
                button = CalcButton(c0 + col * 6, f0 + fila * 4, teclas[ix], make_fn(teclas[ix]))
                ix += 1

        

    def send(self, key):
        if self.output:
            self.output(key)
        



