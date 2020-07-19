import unittest
#import lambdata_iambrookedrake.postISA.py

salary = 50000
taxrate = 20

class TestIncomeMethod(unittest.TestCase):

    def test_postISA(self):
        take_home = TakeHomePay.postISA(salary=50000, taxrate=20)
        #TakeHomePay.postISA(salary=salary, taxrate=taxrate)
        self.assertEqual(take_home,33200)


if __name__ == '__main__':
    unittest.main()
