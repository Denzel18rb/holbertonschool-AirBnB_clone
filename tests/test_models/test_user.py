#!/usr/bin/python3


import unittest
from models.base_model import BaseModel


class testUser(unittest.TestCase):

    def test_attributes(self):
        user = User()

        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))


if __name__ == '__main__':
    unittest.main()
