#!/usr/bin/env python3

def welcome():
    print("Welcome to the test.")
    input("When you are ready press Enter")

def ask_questions():
    name = input("name: ")
    print(f"It is nice to meet you {name}")

    color = input("What is your favorite color? ")
    print(f"{color} is a great color!")

    input("Describe yourself: ")
    print("admirable!")

def goodbye():
    print("Goodbye.")

welcome()
ask_questions()
goodbye()

