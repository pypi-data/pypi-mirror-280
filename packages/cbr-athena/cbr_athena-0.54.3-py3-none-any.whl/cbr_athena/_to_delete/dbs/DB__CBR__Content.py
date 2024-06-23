# from cbr_athena.utils.Version                               import Version
# from osbot_utils.helpers.sqlite.domains.Sqlite__DB__Files   import Sqlite__DB__Files
# from osbot_github.dbs.Sqlite__GitHub__Files                 import Sqlite__GitHub__Files
# from osbot_github.api.GitHub__Repo                          import GitHub__Repo
#
# GIT_HUB_REPO__CBR_ATHENA = "the-cyber-boardroom/cbr-athena"
# SQLITE_DB_NAME           = "cbr_athena.sqlite"
# REPO_FOLDER__DOCS        = 'docs'
#
# class DB__CBR__Content(Sqlite__GitHub__Files):
#
#     def __init__(self, db_path=None):
#         db_name        = SQLITE_DB_NAME
#         repo_full_name = GIT_HUB_REPO__CBR_ATHENA
#         Sqlite__DB__Files.__init__(self, db_path=db_path, db_name=db_name)
#         GitHub__Repo     .__init__(self, full_name=repo_full_name)
#         self.version   = Version().version()
#
#     def db_file(self, path):
#         return self.table_files().where_one(path=path)
#
#     def db_file_contents(self, path):
#         file = self.db_file(path)
#         if file:
#             file_contents = file.get('contents')
#             file_contents += f'\n*********\n\n{self.version }'
#             return file_contents
#
#     def files__from_github(self, path=None):
#         target_path = path or REPO_FOLDER__DOCS
#         return self.all_files(path=target_path)
#
#     def load_files_into_db(self, path=None):
#         table_files = self.table_files()
#         if table_files.size() == 0:
#             for file in self.files__from_github(path):
#                 kwargs = dict(path     = file.get('path'   ),
#                               contents = file.get('content'),
#                               metadata = file)
#                 table_files.add_file(**kwargs)
#
#     def setup(self):
#         super().setup()
#         self.load_files_into_db()
#         return self
#
#
#
