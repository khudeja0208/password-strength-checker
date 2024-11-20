#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Khudeja Begum
Class: CS 521 - Fall 1
Date: 10/19/2024
Homework Problem # final
Description of Problem (1-2 sentence summary in your own words):
This file contains unit tests for the Password class. It includes test cases 
that validate the correctness of the password evaluation logic, such as 
checking that weak and strong passwords are categorized correctly using 
assert statements.

    
"""

import unittest
from password import Password

class TestPassword(unittest.TestCase):
    
    def test_weak_password(self):
        pwd = Password("123")
        self.assertEqual(pwd.evaluate_strength(), "Weak")
    
    def test_strong_password(self):
        pwd = Password("StrongPass1!")
        self.assertEqual(pwd.evaluate_strength(), "Strong")

if __name__ == '__main__':
    unittest.main()
