# from os import environ
# from unittest import TestCase
#
# from dotenv import load_dotenv
#
#
# from cbr_athena.utils.Version import Version
#
# from osbot_utils.utils.Dev import pprint
# from osbot_utils.utils.Files import parent_folder, file_name, current_temp_folder
# from osbot_utils.utils.Misc import list_set, timestamp_to_str
#
#
# class test_DB__CBR__Content(TestCase__GitHub__API):
#     cbr_content = DB__CBR__Content()
#
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         load_dotenv()
#         cls.cbr_content = DB__CBR__Content().setup()
#
#     def test__init__(self):
#         with self.cbr_content as _:
#             assert _.exists() is True              # bug
#             if environ.get('PATH_LOCAL_DBS'):
#                 assert parent_folder(_.db_path) == environ.get('PATH_LOCAL_DBS')
#             else:
#                 assert parent_folder(_.db_path) == current_temp_folder()
#             assert file_name    (_.db_path)     == SQLITE_DB_NAME
#
#     def test_db_file(self):
#         path = 'docs/prompts/misc_prompt_experiments.txt'
#         file = self.cbr_content.db_file(path)
#         assert file.get('path') == path
#
#     def test_db_file_content(self):
#         path             = 'docs/prompts/misc_prompt_experiments.txt'
#         expected_content = '- When starting a new conversation with a board member, suggest 3 topics'
#         content = self.cbr_content.db_file_contents(path)
#         assert expected_content    in content
#         assert Version().version() in content
#
#     def test_files__from_github(self):
#         files = self.cbr_content.files__from_github()
#         #file  = files[0]
#         assert len(files) > 0
#         #assert file.get('path') == 'docs/prompts/misc_prompt_experiments.txt'
#
#     def test_load_files_into_db(self):
#         self.cbr_content.load_files_into_db(path='docs')
#         with self.cbr_content.table_files() as _:
#             assert _.size() == 7
#             file = _.where_one(path='docs/prompts/misc_prompt_experiments.txt')
#             assert type(file) is dict
#             assert list_set(file) == ['contents', 'id', 'metadata', 'path', 'timestamp']
#             assert file.get('path') == 'docs/prompts/misc_prompt_experiments.txt'
#
#
#
