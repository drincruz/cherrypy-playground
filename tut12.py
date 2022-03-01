import random
import string

import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))


if __name__ == '__main__':  # pragma: no cover
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(StringGenerator())