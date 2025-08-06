#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name):
    print(f"Hello, {name}!")
greet("Ayub")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("Karanja")

def add(num1, num2):
    return num1 + num2
print(add(7, 4))

def halve(number):
    return number / 2
print(halve(6))
