# Import the Flask
from flask import Flask, jsonify
import requests

# Instantiate Flask class. This is just a representation of the application
# itself
app = Flask(__name__)


# /add/
@app.route("/add/<int:num1>/<int:num2>", methods=["GET"])
def add(num1, num2):
    return jsonify(status="success", result=num1 + num2), 200


# /subtract/
@app.route("/subtract/<int:num1>/<int:num2>", methods=["GET"])
def subtract(num1, num2):
    return jsonify(status="success", result=num1 - num2)


# /multiply/
@app.route("/multiply/<int:num1>/<int:num2>", methods=["GET"])
def multiply(num1, num2):
    return jsonify(status="success", result=num1 * num2)


# /divide/
@app.route("/divide/<int:num1>/<int:num2>", methods=["GET"])
def divide(num1, num2):
    if num2 == 0:
        return jsonify(error="Cannot divide by zero"), 400
    return jsonify(status="success", result=num1 / num2)


# Check if executed directly (not imported) -> run the app.
# debug=True enables debugger
if __name__ == "__main__":
    app.run(debug=True)
