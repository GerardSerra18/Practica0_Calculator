from cgitb import handler
from distutils.log import error
from errno import errorcode

from flask import render_template

def basic_calculator(a,b,operation):
      

  if (a.isnumeric() & b.isnumeric()):
    a=float(a)
    b=float(b)
    
    if operation == "ADDITION":
      result = a + b
    elif operation == "SUBSTRACTION":
      result = a - b
    elif operation == "DIVISION":
      result = a / b
    elif operation == "MULTIPLICATION":
      result = a * b
      
  return result