from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.responses import RedirectResponse

import cbr_static
from cbr_website_beta.config.CBR_Config import CBR_Config
from cbr_website_beta.cbr__flask.Flask_Site import Flask_Site
from osbot_fast_api.api.Fast_API import Fast_API
from osbot_utils.base_classes.Type_Safe import Type_Safe

from osbot_utils.decorators.methods.cache_on_self import cache_on_self
from osbot_utils.utils.Files import path_combine


class CBR__Fast_API(Fast_API):

    # def add_routes(self):
    #     self.add_routes__cbr_website__flask()

    def add_static_routes(self):
        assets_path = path_combine(cbr_static.path, 'assets')
        from starlette.staticfiles import StaticFiles
        self.app().mount("/assets", StaticFiles(directory=assets_path), name="assets")
        return self

    def add_flask__cbr_website(self):
        flask_site = self.cbr_apps__flask_site()
        flask_app  = flask_site.app()
        path       = '/'
        self.add_flask_app(path, flask_app)
        return self

    @cache_on_self
    def app(self):
        return FastAPI()

    def cbr_apps__flask_site(self):
        return Flask_Site()

    def cbr_config(self):
        return CBR_Config()

    def setup(self):
        super().setup()
        self.add_static_routes()
        self.add_flask__cbr_website()
        return self

    def setup_add_root_route(self):
        app = self.app()

        @app.get("/")                                # todo: move this to a separate method
        def read_root():
            return RedirectResponse(url="/web")

        @app.get('/cbr_config')
        def cbr_config():
            return CBR_Config().config()