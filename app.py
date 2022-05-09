import cherrypy
import os
from mako.lookup import TemplateLookup
lookup = TemplateLookup(
    directories=['templates'], input_encoding='utf-8', output_encoding='utf-8', encoding_errors='replace'
)


class webapp(object):
    @cherrypy.expose
    def index(self):
        template = lookup.get_template("index.html")


cherrypy.quickstart(webapp, '/')
