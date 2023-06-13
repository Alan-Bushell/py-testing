import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('Alan', 'Bushell')
        self.assertEqual(student.full_name, 'Alan Bushell')

    def test_alert_santa(self):
        student = Student('Alan', 'Bushell')
        student.alert_santa()

        self.assertTrue(student.naughty_list)

    def test_email(self):
        student = Student('Alan', 'Bushell')
        self.assertEqual(student.email, 'alanbushell@email.com')


if __name__ == '__main__':
    unittest.main()
