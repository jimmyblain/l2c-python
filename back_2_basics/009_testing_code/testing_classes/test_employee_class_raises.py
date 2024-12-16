# 11-3
from employee_class import Employee
import pytest

# Use pytest fixture (imported above) to ensure all functions can access this object
# Eliminates the need to define this object in every single test case
@pytest.fixture
def basic_employee():
    '''Defining a basic employee object'''
    new_staff = Employee('John', 'Doe', 10000)
    # Must return a value, to be used as variable in other functions
    return new_staff

# When using a fixture, all functions use the original function name as a paramete
def test_give_default_raise(basic_employee):
    '''Testing output of a default raise'''
    basic_employee.give_raise()
    assert basic_employee.salary == 15000

def test_give_custom_raise(basic_employee):
    '''Testing output of a default raise'''
    basic_employee.give_raise(20000)
    assert basic_employee.salary == 30000
