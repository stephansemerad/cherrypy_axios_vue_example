import cherrypy
import os
from mako.lookup import TemplateLookup
import json

path = os.path.join(os.getcwd(), 'templates')
lookup = TemplateLookup(directories=[path])


class HelloWorld(object):
    @cherrypy.expose
    def index(self, **kwargs):
        print()
        print('index')
        print('--------')
        print('kwargs:', kwargs)

        template = lookup.get_template("index.html")
        return template.render(
            id=kwargs.get('id', 1),
            name=kwargs.get('name', None),
            age=kwargs.get('age', None)
        )

    @cherrypy.expose
    def get_users(self, **kwargs):

        print()
        print('get_users')
        print('--------')
        id = kwargs.get('id', 1)
        print('id:', id)
        print('kwargs:', kwargs)

        if id == '1':
            data = [{"name": "John", "age": 30},
                    {"name": "James", "age": 29}]

        if id == '2':
            data = [{"name": "Leisheng", "age": 30},
                    {"name": "Phillip", "age": 29}]

        return json.dumps(data)


cherrypy.quickstart(HelloWorld())
