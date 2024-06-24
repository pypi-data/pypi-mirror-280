from os import environ

import cbr_athena

import cbr_static

import cbr_website_beta
from cbr_website_beta.config.CBR_Config                     import cbr_config
from cbr_website_beta.utils._for_osbot.for_OSBot_Utils      import env__remove__old_pwd, env__pwd
from osbot_utils.utils.Env                                  import get_env
from cbr_athena.utils.Version                               import version__cbr_athena
from cbr_static.utils.Version                               import Version as Version__cbr_static
from osbot_aws.AWS_Config                                   import aws_config
from osbot_fast_api.utils.Version                           import Version as Version__osbot_fast_api
from osbot_utils.utils.Status                               import status_error
from osbot_utils.utils.Version                              import Version as Version__osbot_utils
from osbot_utils.base_classes.Type_Safe                     import Type_Safe
from cbr_website_beta.utils.Version                         import version, version__cbr_website
from osbot_utils.decorators.methods.cache_on_self           import cache_on_self


class CBR__Site_Info(Type_Safe):


    def aws_configured(self):
        with aws_config as _:
            if _.aws_access_key_id():
                if _.aws_secret_access_key():
                    if _.region_name():
                        return True
        return False

    def data(self):
        try:
            return dict(dates    = self.dates    (),
                        env_vars = self.env_vars (),
                        paths    = self.paths    (),
                        urls     = self.urls     (),
                        versions = self.versions ())
        except Exception as error:
            return status_error(message="error in CBR__Site_Info.data", error=f'{error}')

    def dates(self):
        return dict(cbr_site_published_at = get_env('CBR__SITE__PUBLISHED_AT', ''))

    def env_vars(self):
        return dict(status = self.env_vars__status(),
                    values = self.env_vars__values())

    def env_vars__status(self):
        api_key__open_ai  = bool(get_env('OPEN_AI__API_KEY'))
        api_key__ip_data = bool(get_env('IP_DATA__API_KEY'))
        aws_configured   = self.aws_configured()
        return dict( api_key__open_ai  = api_key__open_ai ,
                     api_key__ip_data  = api_key__ip_data ,
                     aws_configured    = aws_configured   )

    def env_vars__values(self):
        return dict(cbr_config_file  = get_env('CBR_CONFIG_FILE' ),
                    execution_env    = get_env('EXECUTION_ENV'   ),
                    port             = get_env('PORT'            ),
                    s3_dev__version  = get_env('S3_DEV__VERSION' ))

    def paths(self):
        return dict(cbr_athena       = env__remove__old_pwd(cbr_athena      .path),
                    cbr_static       = env__remove__old_pwd(cbr_static      .path),
                    cbr_website_beta = env__remove__old_pwd(cbr_website_beta.path),
                    pwd              = env__pwd()                                )


    def target_athena_url(self):        # todo: refactor out once new setup is stable
        return cbr_config.athena_path()

    def url_athena__internal(self):
        port        = self.cbr_host__port()
        athena_path = cbr_config.athena_path()
        if athena_path.startswith('http'):
            return athena_path
        if port:
            return f'http://localhost:{port}{athena_path}'

    def urls(self):
        return dict(url_athena           = self.target_athena_url   (),
                    url_athena__internal = self.url_athena__internal(),
                    url_assets_dist      = cbr_config.assets_dist   (),
                    url_assets_root      = cbr_config.assets_root   ())

    @cache_on_self
    def version(self):
        return version

    def versions(self):
        cbr   = dict(cbr_athena     = version__cbr_athena              ,
                     cbr_website    = version__cbr_website             ,
                     cbr_static     = Version__cbr_static    ().value())       # todo create: version__cbr_static
        osbot = dict(osbot_fast_api = Version__osbot_fast_api().value(),        # todo create: version__osbot_fast_api
                     osbot_utils    = Version__osbot_utils   ().value())       # todo create: version__osbot_utils

        return dict(cbr      = cbr   ,
                    osbot    = osbot )


    # individual values
    def cbr_host__port(self):
        return get_env('PORT')

cbr_site_info = CBR__Site_Info()