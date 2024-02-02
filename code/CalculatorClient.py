#!/usr/bin/env python3

import requests

# def url
BASE_URL = "http://127.0.0.1:5000"


def calculate(operation, num1, num2):
    # construct the url/key to send to the be
    url = f"{BASE_URL}/{operation}/{num1}/{num2}"

    # send req
    response = requests.get(url)

    # check if
    if response.status_code == 200:
        # parse the JSON response and print the result
        result = response.json().get("result")
        print(f"The result is: {result}")
    else:
        # If something went wrong, print the error message
        error = response.json().get(
            "error", "There was an error processing your request."
        )
        print(f"Error: {error}")


def main():
    operation = (
        input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    )
    num1 = input("Enter the first number: ").strip()
    num2 = input("Enter the second number: ").strip()

    if operation not in ["add", "subtract", "multiply", "divide"]:
        print("Invalid operation. Please choose from add, subtract, multiply, divide.")
        return
    if not num1.isdigit() or not num2.isdigit():
        print("Please enter valid numbers.")
        return

    calculate(operation, num1, num2)


if __name__ == "__main__":
    main()
