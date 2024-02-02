# Import the Flask
from flask import Flask

# Instantiate Flask class. This is just a representation of the application
# itself
app = Flask(__name__)

# Define app route
# - app.route()
# - params:
#   - URL (a url or ip addr), default is just ("/") which is the base
#   - methods (), allows us to further specify what requests to mak e
@app.route("/", methods=["GET"])
def hello_world():
    # This function is called when a GET request is made to the root URL.
    # It returns the string 'Hello, World!' as a response.
    return "Hello, World!"


@app.route("/add/<int:num1>/<int:num2>", methods=["GET"])
def add(num1, num2):
    return jsonify(result=num1 + num2)


@app.route("/subtract/<int:num1>/<int:num2>", methods=["GET"])
def subtract(num1, num2):
    return jsonify(result=num1 - num2)


@app.route("/multiply/<int:num1>/<int:num2>", methods=["GET"])
def multiply(num1, num2):
    return jsonify(result=num1 * num2)


@app.route("/divide/<int:num1>/<int:num2>", methods=["GET"])
def divide(num1, num2):
    if num2 == 0:
        return jsonify(error="Cannot divide by zero"), 400
    return jsonify(result=num1 / num2)


# Check if executed directly (not imported) -> run the app.
# debug=True enables debugger
if __name__ == "__main__":
    app.run(debug=True)
