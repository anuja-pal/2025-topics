import unittest
from age import categorize_by_age

class TestCategorizeByAge(unittest.TestCase):
    def test_child(self):
        self.assertEqual(categorize_by_age(5),"Child")
        self.assertEqual(categorize_by_age(0),"Child")
        self.assertEqual(categorize_by_age(9),"Child")

    def test_adolescent(self):
        self.assertEqual(categorize_by_age(12),"Adolescent")
        self.assertEqual(categorize_by_age(18),"Adolescent")

    def test_adult(self):
        self.assertEqual(categorize_by_age(30),"Adult")
        self.assertEqual(categorize_by_age(65),"Adult")
        
    def test_golden_age(self):
        self.assertEqual(categorize_by_age(100),"Golden Age")
        self.assertEqual(categorize_by_age(150),"Golden Age")
    
    def test_invalid_age(self):
        self.assertEqual(categorize_by_age(200),"Invalid age: 200")

    def test_multiple_children(self):
        for possible_child in [0,1,2,3,4,5,6,7,8,9]:
            with self.subTest(possible_child=possible_child):
                print(f"Testing multiple children case for age {possible_child}")
                self.assertEqual(categorize_by_age(possible_child),"Child")

if __name__ == '__main__':
    unittest.main(verbosity=2)