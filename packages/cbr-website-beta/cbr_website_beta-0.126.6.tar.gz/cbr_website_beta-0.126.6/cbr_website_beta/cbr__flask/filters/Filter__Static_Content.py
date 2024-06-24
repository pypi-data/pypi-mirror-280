from cbr_website_beta.content.CBR__Content__Static import CBR__Content__Static
from osbot_utils.base_classes.Type_Safe import Type_Safe
from osbot_utils.utils.Dev import pprint


class Filter__Static_Content():

    filter_name = 'static_content'

    def __init__(self, app):
        app.jinja_env.filters[self.filter_name] = self.static_content
        self.cbr_static_content = CBR__Content__Static()


    def static_content(self,target, lang='en'):
        pprint(lang)
        return self.cbr_static_content.file_contents__for__web_page(target,language=lang)