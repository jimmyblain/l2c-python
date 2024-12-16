# 11-3

class Employee:
    '''Represents employees and their salaries'''

    def __init__(self, first, last, salary):
        '''Store the employee information'''
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, raise_amount=5000):
        '''Increase salary by amount in raise'''
        self.salary += raise_amount