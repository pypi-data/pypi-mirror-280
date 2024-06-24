import requests

from cbr_website_beta.config.CBR_Config import CBR_Config
from osbot_utils.context_managers.capture_duration import capture_duration

from osbot_utils.base_classes.Type_Safe import Type_Safe
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Misc import list_set
from osbot_utils.utils.Objects import class_functions
from osbot_utils.utils.Status import status_ok, status_error

class Health_Checks__CBR__Internal_Data:

    @staticmethod
    def cbr_config_data():
        cbr_config = CBR_Config().config()
        if list_set(cbr_config) == [ 'data', 'error', 'message', 'status']:
            return 'CBR_Config had the expected data'
        raise Exception('CBR_Config did NOT had the expected data')

class Health_Checks__Http__External_Sites:

    @staticmethod
    def head__google():
        url = 'https://www.google.com'
        response = requests.head(url)
        if response.status_code != 200:
            raise Exception('head__google status code was not 200')
        return 'google is up'

class CBR__Health_Checks(Type_Safe):

    def execute_health_check(self, function):
        with capture_duration() as duration:
            try:
                return_value = function()
                result       = status_ok(data=return_value)
            except Exception as error:
                result       = status_error(error=f'{error}')

        result['duration'     ] = duration.seconds
        return result

    def execute_health_checks(self):
        results     = {}
        health_checks  = [ Health_Checks__CBR__Internal_Data  ,
                           Health_Checks__Http__External_Sites]

        for health_check_class in health_checks:
            results[health_check_class.__name__] = self.execute_health_checks__from_class(health_check_class)
        return results

    def execute_health_checks__from_class(self, class_with_health_checks):
        items = {}

        http_perf_functions = class_functions(class_with_health_checks())
        for function_name, function in http_perf_functions.items():
            items[function_name] = self.execute_health_check(function)
        return items


