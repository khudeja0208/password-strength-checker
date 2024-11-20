#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Khudeja Begum
Class: CS 521 - Fall 1
Date: 10/19/2024
Homework Problem # final
Description of Problem (1-2 sentence summary in your own words):
This file contains the Password class, which is responsible for evaluating 
the strength of the password based on length, characters used, and other 
criteria. It includes methods like evaluate_strength, __init__, __str__, and 
a few others.

"""

import re

class Password:
    def __init__(self, password):
        self.__password = password  
        self.length = len(password)  
        self.strength = "Unknown" 
    
    def evaluate_strength(self):
        if self.length < 8:
            self.strength = "Weak"
        elif self.length >= 8 and re.search(r'[A-Za-z]', self.__password) and re.search(r'[0-9]', self.__password):
            if re.search(r'[\W]', self.__password):  
                self.strength = "Strong"
            else:
                self.strength = "Moderate"
        else:
            self.strength = "Weak"
        return self.strength
    
    def __str__(self):
        return f"Password: {'*' * len(self.__password)}, Length: {self.length}, Strength: {self.strength}"
    
    def __eq__(self, other):
        return self.__password == other.__password
