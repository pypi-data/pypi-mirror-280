# from unittest import TestCase
#
# import frontmatter
# from osbot_utils.testing.Duration import Duration
#
# from osbot_utils.utils.Dev import pprint
#
# from cbr_athena.api.Repo__CBR_Athena import Repo__CBR_Athena
#
# class test_Repo__CBR_Athena(TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.github_cbr_athena = Repo__CBR_Athena()
#
#
#     def test_content__cybersecurity_in_the_boardroom(self):
#         raw_content = self.github_cbr_athena.content__cybersecurity_in_the_boardroom()
#
#         metadata, content = frontmatter.parse(raw_content)
#         assert metadata  == { 'sidebar_position': 1                                   ,
#                               'title'           : '1) Cybersecurity in the boardroom' }
#
#         assert content.startswith('Too many boards see cybersecurity')
#
#     def test_content__building_a_cybersecure_organisation(self):
#         raw_content = self.github_cbr_athena.content__building_a_cybersecure_organisation()
#         metadata, content = frontmatter.parse(raw_content)
#         assert metadata == {'sidebar_position': 2                             ,
#                             'title': '2) Building a cybersecure organisation.'}
#
#         assert content.startswith('Unfortunately, cyber crime is not going away')
#
#     def test_content__incident_management(self):
#         raw_content = self.github_cbr_athena.content__incident_management()
#         metadata, content = frontmatter.parse(raw_content)
#         assert metadata  == { 'sidebar_position': 3                                   ,
#                               'title'           : '3) Incident management' }
#         assert content.startswith('Boards need to be prepared to detect')
#
#     def test_content__importance_of_digital_trust(self):
#         raw_content = self.github_cbr_athena.content__importance_of_digital_trust()
#         metadata, content = frontmatter.parse(raw_content)
#         assert metadata  == { 'sidebar_position': 4                                   ,
#                               'title'           : '4) The importance of digital trust.' }
#
#         assert content.startswith('When an organisation has a strong')
#
