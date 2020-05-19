# Put your app in here.
from flask import Flask, request
from operations import add, sub, div, mult

app = Flask(__name__)

@app.route("/add")

def addition():
    """Return the sum of the first and second numbers in a query string"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    added = add(a, b)
    return str(added)

@app.route("/sub")

def subtraction():
    """ Return the difference of the first and second numbers in a query string"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    difference = sub(a, b)
    return str(difference)


@app.route("/mult")

def multiplication():
    """"Return the product of the first and second numbers in a query string"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    product = mult(a, b)
    return str(product)


@app.route("/div")

def division():
    """"Return the quotient of the first and second numbers in a query string"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    quotient = div(a, b)
    return str(quotient)

MATH = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div":div
}


@app.route("/math/<operation>")

def math_operation(operation):
    """Return the result of the passed in operation done on the first and second numbers in a query string """
    a = int(request.args["a"])
    b = int(request.args["b"])

    operator = MATH[operation]
    result = operator(a, b)
    return str(result)
