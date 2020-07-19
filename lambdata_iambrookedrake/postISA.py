import pandas as pd


class TakeHomePay():
    # '''Accepts input for 'Salary Offer' and 'Tax Rate %' to provide
    # Annual, Monthly, and Weekly take home pay after taxes and
    # Lambda ISA deductions'''

    def __init__(self, salary, taxrate):
        self.salary = salary
        self.taxrate = taxrate

    def postISA(self, salary, taxrate):
        take_home = salary * (1-taxrate/100) * (1-0.17)
        return take_home

if __name__ == '__main__':
    salary = int(input("Salary Offer:"))
    taxrate = int(input('Tax Rate in %:'))
    take_home = TakeHomePay(salary, taxrate).postISA(salary, taxrate)
    print("Take Home Pay is:", round(take_home, 2), ", Annually;; ",
          round(take_home/12, 2), ", Monthly;;", round(take_home/52, 2),
          ", Weekly")
