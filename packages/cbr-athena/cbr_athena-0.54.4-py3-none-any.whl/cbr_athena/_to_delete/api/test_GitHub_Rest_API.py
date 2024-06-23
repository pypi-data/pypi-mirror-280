# from unittest import TestCase
# from osbot_utils.utils.Misc import list_set
#
# from cbr_athena.api.GitHub_Rest_API import GitHub_Rest_API
# import pytest
#
#
# class test_GitHub_Rest_API(TestCase):
#
#     def setUp(self) -> None:
#         target_repo = "the-cyber-boardroom/cbr-athena"
#         self.github_rest_api = GitHub_Rest_API(target_repo=target_repo)
#
#     def test__init__(self):
#         assert self.github_rest_api.target_repo == "the-cyber-boardroom/cbr-athena"
#
#     def test_access_token(self):
#         assert self.github_rest_api.access_token() is not None
#         assert len(self.github_rest_api.access_token()) > 10
#
#     def test_commits(self):
#         commits = self.github_rest_api.commits()
#         for commit in commits:
#             assert list_set(commit) == ['author','date', 'message', 'sha']
#
#     def test_file_content(self):
#         file_path = 'docs/content/1-cybersecurity-in-the-boardroom.md'
#         assert '1) Cybersecurity in the boardroom'     in self.github_rest_api.file_content(file_path)
#
#     def test_file_parsed_content(self):
#         file_path = 'docs/content/1-cybersecurity-in-the-boardroom.md'
#         result    = self.github_rest_api.file_parsed_content(file_path)
#         assert '1) Cybersecurity in the boardroom' in result.get('content')
#
#     def test_file_download(self):
#         file_path    = 'docs/content/1-cybersecurity-in-the-boardroom.md'
#         assert '1) Cybersecurity in the boardroom' in self.github_rest_api.file_download(file_path)
#
#     @pytest.mark.skip("to be refactored into s3")
#     def test_folder_contents(self):
#         result = self.github_rest_api.folder_contents('docs')
#         assert len(result) == 3
#
#     @pytest.mark.skip("to be refactored into s3")
#     def test_folder_files(self):
#         result = self.github_rest_api.folder_files("docs")
#         assert len(result) == 1
#         assert result[0].get('path') == 'docs/homepage.md'
#
#     @pytest.mark.skip("to be refactored into s3")
#     def test_folder_folders(self):
#         result = self.github_rest_api.folder_folders("docs")
#         assert len(result) > 1
#
#     @pytest.mark.skip("to be refactored into s3")
#     def test_folders_and_files(self):
#         result = self.github_rest_api.folders_and_files("docs", index_by='path')
#         assert 'docs/content/1-cybersecurity-in-the-boardroom.md' in  result
#         assert len(result) > 3
#
#     def test_parse_raw_content(self):
#         result = self.github_rest_api.parse_raw_content([])
#         assert result == {}
#
#     def test_repo(self):
#         repo = self.github_rest_api.repo()
#         assert repo.default_branch == 'dev'
#         assert repo.id             ==  678116177
#         assert repo.full_name      == "the-cyber-boardroom/cbr-athena"
#         assert repo.name           == 'cbr-athena'
#         assert repo.git_url        == 'git://github.com/the-cyber-boardroom/cbr-athena.git'
#
#     @pytest.mark.skip("to be refactored into s3")
#     def test___get_last_action_details(self):
#         print()
#         repo = self.github_rest_api.repo()
#         workflow_runs_list = []
#         n = 2
#         kwargs = {'branch': 'dev'}
#         for i, workflow_run in enumerate(repo.get_workflow_runs(**kwargs)):
#             if i >= n:
#                 break
#             workflow_runs_list.append(workflow_run)
#             assert len(list(workflow_run.jobs())) == 1
#             # for job in workflow_run.jobs():
#             #     print(job.url)
#             #     logs_url = job.url + '/logs'
#             #     headers = {'Authorization': f'token {self.github_rest_api.access_token()}',
#             #                'Accept-Encoding': 'gzip'}
#             #     print(logs_url)
#             #     print()
#             #
#             #     data = requests.get(job.url, headers=headers)
#             #     pprint(data.json())
#             #     data = requests.get(logs_url, headers=headers)
#             #     print(data.text)
#
#
#         #pprint(workflow_runs_list)
#         #workflow_runs_list = [run for run in workflow_runs]
#
#         #print(len(workflow_runs_list))
#         return
#         # for workfow_run in repo.get_workflow_runs():
#         #     pprint(workfow_run)
#         #     break
#         # return
#         # last_workflow_run = repo.get_workflow_runs().get_page(0)[0]  # Assuming the latest run is what you want
#         # #obj_info(last_workflow_run)
#         # for job in last_workflow_run.get_jobs():
#         #     pprint(job)
#         #job_id = last_workflow_run.get_jobs().get_page(0)[0].id