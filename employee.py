"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, string, total_pay, name, contract, wage,  number_of_hours):
        self.name = name
        self.contract = contract
        self.wage = wage
        self.number_of_hours = number_of_hours
        self.total_pay = total_pay
        self.string = f"{self.name} works on a "

    def get_pay(self):
        if self.contract == 'monthly':
            self.total_pay = self.wage
        elif self.contract == 'hourly':
            self.total_pay = self.wage * self.number_of_hours
        return self.total_pay

    def __str__(self):
        if self.contract == 'monthly':
            self.string = self.string + f'monthly salary of {self.wage} '
        else:
            self.string = self.string + f'contract of {self.number_of_hours} hours at {self.wage}/hour '
        return self.string +f'. Their total pay is {self.get_pay()}.'

class CommissionedEmployee(Employee):
    def __init__(self, string, total_pay, name, contract, wage, commission_type, commission_value, number_of_commissions, number_of_hours):
        super().__init__(string, total_pay, name, contract, wage,  number_of_hours)
        self.commission_type = commission_type
        self.commission_value = commission_value
        self.number_of_commissions = number_of_commissions

    def get_pay(self):
        super().get_pay()
        if self.commission_type == 'fixed':
            self.total_pay = self.total_pay + self.commission_value
        elif self.commission_type == 'variable':
            self.total_pay = self.total_pay + (self.number_of_commissions * self.commission_value)
        return self.total_pay

    def __str__(self):
        super().__str__()
        if self.commission_type == 'fixed':
            self.string = self.string + f'and receives a bonus commission of {self.commission_value}'
        elif self.commission_type == 'variable':
            self.string = self.string + f'and receives a commission for {self.number_of_commissions} contract(s) at {self.commission_value}/contract'
        return self.string +f'. Their total pay is {self.get_pay()}.' 

billie = Employee("", 0, 'Billie', 'monthly' , 4000, 0)

charlie = Employee("", 0, 'Charlie', 'hourly', 25, 100)

renee = CommissionedEmployee("", 0, 'Renee', 'monthly', 3000, 'variable', 200, 4, 0)

jan = CommissionedEmployee("", 0, 'Jan', 'hourly', 25, 'variable', 220, 3, 150)

robbie = CommissionedEmployee("", 0, 'Robbie', 'monthly', 2000, 'fixed', 1500, 0, 0)

ariel = CommissionedEmployee("", 0, 'Ariel', 'hourly', 30, 'fixed', 600, 0, 120)

