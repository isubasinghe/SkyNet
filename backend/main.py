from flask import Flask

from models import env as env
from controllers import register

def main():
    # Create a new flask instance
    app = Flask(__name__)
    # Register the route/endpoints for the web
    # page
    register.routes(app)
    # Obtain, the current running conditions, 
    # is it a debug case, or is it a production case.
    # PROD=(host='0.0.0.0', port=80)
    # DEBUG=(host='localhost', port=8080)
    app.run(host=env.get_host(), port=env.get_port())
    
if __name__ == '__main__':
    # We can change host(localhost only or not), port
    # and enable debugging based on whether this is our
    # test instance or not
    env.set_test_env()
    main()