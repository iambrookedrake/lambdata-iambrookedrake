import unittest
from ..my_lambdata.postISA import TakeHomePay

salary = 50000
taxrate = 20


class TestIncomeMethod(unittest.TestCase):

    def test_postISA(self, salary=salary, taxrate=taxrate):
        # TakeHomePay.postISA(salary=salary, taxrate=taxrate)
        take_home = TakeHomePay(salary=salary, taxrate=taxrate).postISA(
                    salary=50000, taxrate=20)

        self.assertEqual(take_home, 33200)


if __name__ == '__main__':
    unittest.main()
