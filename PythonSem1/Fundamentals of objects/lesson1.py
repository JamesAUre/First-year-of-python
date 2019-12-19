import datetime
class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    #constructor
    def __init__(self, first, last, pay):
        #instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        #self.raise_amount is a class variable and must be accessed from the class itself or an instance
        self.pay = int(self.pay * self.raise_amount)

    #sets raise amount amongst all instances of the class
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    #creates new employee object of class
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')

        #creates new employee object and returns it
        return cls(first, last, int(pay))

    #static methods have no attributes to the class nor any instance
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


#instances of the class
emp1 = Employee('James', 'Ure', 500)

emp2 = Employee('Rebecca', 'Ur', 500)

emp_str_1 = 'Andrew-Ure-7000'

emp3 = Employee.from_string(emp_str_1)

my_date = datetime.date(2019,7,28)
print(Employee.is_workday(my_date))






#Employee.set_raise_amt(1.05)

#prints number of instantiated objects of the class
#if this is put before the declarations of the instances then the number would reduce
#print(Employee.num_of_emps)

#print(Employee.fullname(emp2))
#print(emp2.email)
#emp3.apply_raise()

