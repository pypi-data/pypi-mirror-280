from calculator.models import Calculation, RomanCalculation

def test_operation_simple():
    calculation = Calculation()
    assert calculation.display == 0

    calculation.receive('1')
    assert calculation.display == 1

    calculation.receive('+')
    assert calculation.display == 1

    calculation.receive('2')
    assert calculation.display == 2

def test_operations_repe_equals():
    calculation = Calculation()
    calculation.receive('1')
    calculation.receive('+')
    calculation.receive('2')

    calculation.receive('+')
    assert calculation.display == 3

    calculation.receive('+')
    assert calculation.display == 3

    calculation.receive('=')
    assert calculation.display == 6

    calculation.receive('=')
    assert calculation.display == 9
    
    
def test_operations_contiguous_operator():
    calculation = Calculation()
    calculation.receive('1')
    calculation.receive('+')
    calculation.receive('2')

    calculation.operator = '+'
    assert calculation.display == 3

    calculation.receive('5')
    assert calculation.display == 5

    calculation.operator = '-'
    assert calculation.display == 8

    calculation.receive('1')
    assert calculation.display == 1

    calculation.operator = '-'
    assert calculation.display == 7

    calculation.receive('3')
    assert calculation.display == 3

    calculation.operator = '='
    assert calculation.display == 4


def test_operation_equal_after_repe_operator():
    calculation = Calculation()
    calculation.receive('1')
    calculation.receive('+')
    calculation.receive('2')

    calculation.operator = '+'
    assert calculation.display == 3

    calculation.operator = '+'
    assert calculation.display == 3

    calculation.operator = '='
    assert calculation.display == 6

def test_operation_more_than_one():
    calculation = Calculation()
    calculation.receive('1')
    calculation.receive('+')
    calculation.receive('2')

    calculation.receive('+')
    assert calculation.display == 3

    calculation.receive('2')
    assert calculation.display == 2

    calculation.receive('-')
    assert calculation.display == 5

    calculation.receive('1')
    assert calculation.display == 1

    calculation.receive('*')
    assert calculation.display == 4

    calculation.receive('3')
    assert calculation.display == 3

    calculation.receive('=')
    assert calculation.display == 12

def test_roman_operation_simple():
    calculation = RomanCalculation()
    assert calculation.display == 0

    calculation.receive('I')
    assert calculation.display == 1

    calculation.receive('+')
    assert calculation.display == 1

    calculation.receive('II')
    assert calculation.display == 2





    


