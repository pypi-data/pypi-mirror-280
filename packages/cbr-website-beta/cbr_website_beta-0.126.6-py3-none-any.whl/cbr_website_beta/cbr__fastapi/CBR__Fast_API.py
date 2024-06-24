import cbr_static
from starlette.responses                            import RedirectResponse, FileResponse
from starlette.staticfiles                          import StaticFiles
from cbr_athena.athena__fastapi.FastAPI_Athena      import FastAPI_Athena
from cbr_website_beta.config.CBR_Config             import cbr_config
from cbr_website_beta.cbr__flask.Flask_Site         import Flask_Site
from cbr_website_beta.config.CBR__Site_Info import CBR__Site_Info
from cbr_website_beta.utils.performance.CBR__Health_Checks import CBR__Health_Checks
from osbot_fast_api.api.Fast_API                    import Fast_API
from osbot_utils.decorators.methods.cache_on_self   import cache_on_self
from osbot_utils.utils.Files                        import path_combine, file_exists, file_contents_as_bytes
from osbot_utils.utils.Objects                      import type_full_name


class CBR__Fast_API(Fast_API):

    def add_athena(self):
        cbr_athena_app = self.cbr_athena().app()
        self.app().mount("/api", cbr_athena_app)

    def add_static_routes(self):
        assets_path = path_combine(cbr_static.path, 'assets')
        self.app().mount("/assets", StaticFiles(directory=assets_path, html=True), name="assets")
        return self

    def add_flask__cbr_website(self):
        flask_site = self.cbr_apps__flask_site()
        flask_app  = flask_site.app()
        path       = '/'
        self.add_flask_app(path, flask_app)
        return self

    def cbr_athena(self):
        return FastAPI_Athena().setup()

    def cbr_apps__flask_site(self):
        return Flask_Site()

    def cbr_config(self):
        return cbr_config

    def setup(self):
        super().setup()
        self.add_athena()
        self.add_static_routes()
        self.add_flask__cbr_website()
        return self

    def setup_add_root_route(self):
        app = self.app()

        @app.get("/")                                # todo: move this to a separate method
        def read_root():
            return RedirectResponse(url="/web/home")

        @app.get('/cbr_config')
        def cbr_config__config():
            return cbr_config.config()

        @app.get('/cbr_site_info')
        def cbr_config__config():
            return CBR__Site_Info().data()

        @app.get('/favicon.ico')                # todo: convert the png below to .ico file (also see what are the side effects of returning a png instead of an ico)
        def favicon_ico():
            file_path = path_combine(cbr_static.path, "/assets/cbr/tcb-favicon.png")
            return FileResponse(file_path, media_type="image/png")

        @app.get('/health_checks')
        def health_checks():
            cbr_health_checks = CBR__Health_Checks().execute_health_checks()
            return cbr_health_checks