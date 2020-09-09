import pandas as pd


class TakeHomePay():
    # Accepts input for 'Salary Offer' and 'Tax Rate %' to provide
    # Annual, Monthly, and Weekly take home pay after taxes and
    # Lambda ISA deductions

    def __init__(self, salary, taxrate):
        self.salary = salary
        self.taxrate = taxrate

    def postISA(self, salary, taxrate):
        ISArate = 17  # Whole number % of ISA rate
        take_home = self.salary * (1-self.taxrate/100) * (1-ISArate/100)
        return take_home

if __name__ == '__main__':
    salary = int(input("Salary Offer $:"))
    taxrate = int(input('Tax Rate as Whole Number ___%:'))
    take_home = TakeHomePay(salary, taxrate).postISA(salary, taxrate)
    print("After ISA and Taxes, Take Home Pay is:", round(take_home, 2),
          "Annually/// ", round(take_home/12, 2), "Monthly///",
          round(take_home/52, 2), "Weekly")
