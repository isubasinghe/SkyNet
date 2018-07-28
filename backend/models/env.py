import os
from flask import Flask

def get_host():
    # Sets reachability of server depending on
    # the enviroment FLASK_ENV.
    if os.environ["FLASK_ENV"] == "production":
        return "0.0.0.0"
    else:
        return "localhost"

def get_port():
    # Sets the port to run on depending on the 
    # environment variable FLASK_ENV
    if os.environ["FLASK_ENV"] == "production":
        return 80
    else:
        return 8080

# Two setter functions for the production or development environment
# variable FLASK_ENV
def set_prod_env():
    os.environ["FLASK_ENV"] = "production"

def set_test_env():
    os.environ["FLASK_ENV"] = "development"