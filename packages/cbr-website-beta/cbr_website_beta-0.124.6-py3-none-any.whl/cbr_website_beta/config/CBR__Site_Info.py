from cbr_athena.utils.Version           import version__cbr_athena
from cbr_static.utils.Version           import Version as Version__cbr_static
from osbot_fast_api.utils.Version       import Version as Version__osbot_fast_api
from osbot_utils.utils.Version          import Version as Version__osbot_utils
from osbot_utils.base_classes.Type_Safe import Type_Safe

from cbr_website_beta.utils.Version import version, version__cbr_website
from osbot_fast_api.api.Fast_API import Fast_API
from osbot_utils.decorators.methods.cache_on_self import cache_on_self


class CBR__Site_Info(Type_Safe):

    @cache_on_self
    def version__fast_api_server(self):
        return Fast_API().version__fast_api_server()

    @cache_on_self
    def version(self):
        return version

    def versions(self):
        cbr   = dict(cbr_athena     = version__cbr_athena              ,
                     cbr_website    = version__cbr_website             ,
                     cbr_static     = Version__cbr_static    ().value() )       # todo create: version__cbr_static
        osbot = dict(osbot_fast_api = Version__osbot_fast_api().value(),        # todo create: version__osbot_fast_api
                     osbot_utils    = Version__osbot_utils   ().value() )       # todo create: version__osbot_utils
        return dict(cbr   = cbr  ,
                    osbot = osbot)
    def data(self):
        return dict(versions= self.versions())
