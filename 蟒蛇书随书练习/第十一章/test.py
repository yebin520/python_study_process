import unittest
from name_function import get_formatted_name

class MyTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('chen','yebin')
        self.assertEqual(formatted_name, "Chen Yebin")  # add assertion here
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name("cai",'jia','yue')
        self.assertEqual(formatted_name,"Cai Jia Yue")



if __name__ == '__main__':
    unittest.main()
