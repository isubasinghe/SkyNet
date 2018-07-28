""" Register all the routes for our web page by calling the routes function"""

from flask import Flask
from views.views import index_get_page

def routes(app):
    # add a rule for the landing page to redirect to index_get_page
    app.add_url_rule('/', 'index', index_get_page)