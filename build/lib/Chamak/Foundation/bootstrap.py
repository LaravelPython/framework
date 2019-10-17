from Chamak.Foundation.app import Application
import importlib
from config.app import config
from config.database import database
from Chamak.Foundation.Router import Router
from Chamak.Foundation.Request import Request
from Chamak.Foundation.Response import Response


class Bootstrap:
    def __init__(self, env, response):
        self.env = env
        self.response = response
        self.boot()

    def boot(self):
        Application.bind('env', self.env)
        Application.bind('config', config)
        Application.bind('response', Response(self.response))

    @staticmethod
    def run():
        return Router.load('routes.web').direct(Request.uri(), Request.method())
