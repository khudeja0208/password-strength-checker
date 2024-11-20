#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Khudeja Begum
Class: CS 521 - Fall 1
Date: 10/19/2024
Homework Problem # final
Description of Problem (1-2 sentence summary in your own words):
This is the main script that runs the program. It provides a text-based user 
interface where users can input passwords to check their strength, save 
results to a file, or load previously saved passwords.
"""

from password import Password

def main():
    while True:
        print("\nPassword Strength Checker")
        print("1. Check Password Strength")
        print("2. Save Password")
        print("3. Load Previous Passwords")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            password_input = input("Enter a password to check: ")
            pwd = Password(password_input)
            strength = pwd.evaluate_strength()
            print(f"The strength of your password is: {strength}")
            print(pwd)
        
        elif choice == '2':
            save_password(password_input)
        
        elif choice == '3':
            load_passwords()
        
        elif choice == '4':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, try again.")

def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")
    print(f"Password '{password}' saved.")

def load_passwords():
    try:
        with open("passwords.txt", "r") as file:
            passwords = file.readlines()
        print("Previously saved passwords:")
        for pwd in passwords:
            print(pwd.strip())
    except FileNotFoundError:
        print("No passwords found.")

if __name__ == "__main__":
    main()
