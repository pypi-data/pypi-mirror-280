from simple_screen import pause, locate, STDSRC, A_UNDERLINE, A_REVERSE, Print, BACKSPACE, TAB, ENTER, STAB, key_map
from abc import ABC, abstractmethod
from easy_tui import widgets, tabulatables, buttons, LAST_COL, LAST_ROW

key_list = list(key_map.values())

def click_animate(method):
    def wrapper(self, *args, **kwargs):
        if self.clicked:
            A_REVERSE.on()
            pause(10)
        result = method(self, *args, **kwargs)
        if self.clicked:
            A_REVERSE.off()
            self.clicked = False
        return result
    return wrapper

class Mixin(ABC):
    @abstractmethod
    def configure(self):
        pass

class Control(ABC):
    def __init__(self, col=0, fila=0, ancho=16, alto=1):
        self.col = col
        self.fila = fila
        self.ancho = ancho
        self.alto = alto

        widgets.append(self)
        if isinstance(self, Mixin):
            self.configure()

    @abstractmethod
    def draw(self, *args):
        pass

    """ @abstractmethod
    def update(self, *args):
        pass

    @abstractmethod
    def handle_input(self, key, *args):
        pass

    @abstractmethod
    def validate(self, value):
        pass """

class ButtonMixin(Mixin):
    def configure(self):
        buttons.append(self)

class TabulatableMixin(Mixin):
    _focused = False

    def configure(self):
        tabulatables.append(self)

    @property
    def focused(self):
        return self._focused
    
    def focus_in(self):
        self._focused = True

    def focus_out(self):
        self._focused = False

class Label(Control):
    def __init__(self, col=0, fila=0, text="Label"):
        super().__init__(col, fila)
        self.text = text
        
    def draw(self):
        locate(self.col, self.fila, self.text)


class Entry(Control, TabulatableMixin):
    def __init__(self, col=0, fila=0, label="", ancho=16):
        super().__init__(col, fila, ancho)

        self.label = label
        self.col_value = self.col + len(self.label) + 1
        self.buffer = []

    def draw(self):
        locate(self.col, self.fila, f"{self.label}")

        if self.focused:
            A_UNDERLINE.on()
        locate(self.col + len(self.label), self.fila, (self.value or ' '))
        A_UNDERLINE.off()
        Print(" ")

    @property
    def value(self):
        return ''.join(self.buffer)
    
    @value.setter
    def value(self, text: str):
        self.buffer = list(text)
    
    def handle_input(self, key):
        if key in BACKSPACE:
            if self.buffer:
                self.buffer.pop()
        elif key in (TAB, ENTER, STAB):
            return True
        elif key and key not in key_list:
            self.buffer.append(key)


class KeyButton(Control, ButtonMixin):
    def __init__(self, col=0, fila=LAST_ROW, key=None, command=None, label=""):
        super().__init__(col, fila)
        self.key = key
        self.label = f"{key}: {label}" if label else key
        self._command = command or (lambda: True)
        self.clicked = False

    def click(self):
        self.clicked = True
        self.command()


    @property
    def command(self):
        return self._command
    
    @command.setter
    def command(self, f):
        self._command = f
    
    @click_animate
    def draw(self):
        locate(self.col, self.fila, f"| {self.label} |")



