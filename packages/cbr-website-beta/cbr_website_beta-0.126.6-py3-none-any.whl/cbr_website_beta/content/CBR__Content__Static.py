import os
from os.path import normpath, commonpath, join

import cbr_static
from cbr_website_beta.utils.Markdown_Parser import markdown_parser
from cbr_website_beta.utils._for_osbot.for_OSBot_Utils  import path_combine_safe
from osbot_utils.base_classes.Type_Safe                 import Type_Safe
from osbot_utils.utils.Files import files_list, file_exists, file_contents
from osbot_utils.utils.Misc                             import remove

FOLDER_NAME__STATIC__CONTENT = 'content'
FOLDER_NAME__WEB_PAGES       = 'web-pages'

class CBR__Content__Static(Type_Safe):

    def content_files(self, pattern="*"):
        return files_list(self.path_static_content(), pattern=pattern)

    def content_files__md(self):
        base_folder = self.path_static_content() + '/'
        md_files = []
        for file_path in self.content_files(pattern="*.md"):
            md_file = remove(file_path, base_folder)
            md_files.append(md_file)
        return md_files

    def file_contents(self, target_file):
        full_path = path_combine_safe(self.path_static_content(), target_file)
        if file_exists(full_path):
            return file_contents(full_path)

    def file_contents__for__web_page(self, file_name, language='en', file_extension='md'):
        target_file           = f'{language}/{FOLDER_NAME__WEB_PAGES}/{file_name}.{file_extension}'
        file_contents__raw    = self.file_contents(target_file)
        if file_contents__raw:
            file_contents__parsed = self.parse_file_contents(file_contents__raw, file_extension=file_extension)
            return file_contents__parsed
        return '(no content)'

    def parse_file_contents(self, file_contents, file_extension):
        if file_extension == 'md':
            return markdown_parser.content_to_html(file_contents)
        return 'aaa'

    def path_to_file(self, file_location):
        return path_combine_safe(self.path_static_content(), file_location)

    def path_static_content(self):
        return path_combine_safe(cbr_static.path, FOLDER_NAME__STATIC__CONTENT)

