from collections import namedtuple
from simple_roman_numbers import RomanNumber

EQUAL_OPERATOR = "="

class Operation(namedtuple("operator",("symbol", "func"))):
    __slots__ = ()

    def resolve(self, v1, v2):
        return self.func(v1, v2)
    
Operators = [Operation("+", lambda a, b: a + b),
             Operation("-", lambda a, b: a - b),
             Operation("*", lambda a, b: a * b),
             Operation("/", lambda a, b: a / b),
             Operation("=", lambda a, b: None)]

class Calculation:
    operators = {op.symbol: op.func for op in Operators}

    def __init__(self, op1 = None, op2 = None, operator = None):
        self._op1 = op1
        self._op2 = op2
        self._operator = operator
        self._resolved = False
        self.display = 0

    def __resolve(self):
        operation = self.operators.get(self._operator)
        result = operation(self.op1, self.op2) if operation and self.op2 else None
        return result

    def add_number(self, value):
        if self._op1 is None:
            self._op1 = value
        elif self._op2 is None:
            self._op2 = value
        else:
            self._op1 = self._op2
            self._op2 = value

        self.display = self.op2 or self.op1
        self._resolved = False
    
    @property
    def op1(self):
        return self._op1
    

    @property
    def op2(self):
        return self._op2
    

    @property
    def operator(self):
        return self._operator
    
    @operator.setter
    def operator(self, value):
        if value not in list(self.operators):
            raise ValueError(f"{value} must be in ({','.join(self.operators)})")

        if self.op2 is None:
            self._operator = value
            return
        
        if value != EQUAL_OPERATOR:
            if not self._resolved:
                self.display = self.__resolve()
                self._op2 = self.display
            else:
                self._op1 = self._op2 = self.display
        
            self._operator = value
            self._resolved = True
        else:
            self.display = self.__resolve()
            if not self._resolved:
                self.add_number(self.display)
            else:
                self._op2 = self.display

            self._resolved = True
        
    def receive(self, value: str):
        if value in list(self.operators):
            self.operator = value
        else:
            self.add_number(float(value))

class RomanCalculation(Calculation):
    def receive(self, value: str):
        if value in list(self.operators):
            self.operator = value
        else:
            self.add_number(float(RomanNumber(value)))

