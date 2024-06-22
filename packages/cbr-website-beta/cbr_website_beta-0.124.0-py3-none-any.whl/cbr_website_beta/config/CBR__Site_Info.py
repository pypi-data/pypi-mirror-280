from osbot_utils.base_classes.Type_Safe import Type_Safe

from cbr_website_beta.utils.Version import version
from osbot_fast_api.api.Fast_API import Fast_API
from osbot_utils.decorators.methods.cache_on_self import cache_on_self


class CBR__Site_Info(Type_Safe):

    @cache_on_self
    def version__fast_api_server(self):
        return Fast_API().version__fast_api_server()

    @cache_on_self
    def version(self):
        return version
