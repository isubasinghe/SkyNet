"""The index handler"""

import views.views as views

def index_handler():
    # Insert the a html loader function here for the
    # index/landing page of our site
    return views.index_get_page()