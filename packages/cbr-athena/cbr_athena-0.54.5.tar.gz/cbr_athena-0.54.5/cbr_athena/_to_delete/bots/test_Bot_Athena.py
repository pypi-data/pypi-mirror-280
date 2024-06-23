# from unittest import TestCase
#
# import frontmatter
# from fastapi import FastAPI
#
# from cbr_athena.bots.Bot_Athena import Bot_Athena
#
#
# class test_Bot_Athena(TestCase):
#
#     def setUp(self) -> None:
#         self.app    = FastAPI()
#         self.athena = Bot_Athena(self.app)
#
#     def test_athena_prompt(self):
#         assert self.athena.athena_prompt().startswith('You are The Cyber Boardroom')
#
#     def test_content__cybersecurity_in_the_boardroom(self):
#         raw_content = self.athena.content__cybersecurity_in_the_boardroom()
#
#         metadata, content = frontmatter.parse(raw_content)
#         assert metadata  == { 'sidebar_position': 1                                   ,
#                               'title'           : '1) Cybersecurity in the boardroom' }
#
#         assert content.startswith('Too many boards see cybersecurity')
#
#     def test_content__building_a_cybersecure_organisation(self):
#         raw_content = self.athena.content__building_a_cybersecure_organisation()
#         metadata, content = frontmatter.parse(raw_content)
#         assert metadata == {'sidebar_position': 2                             ,
#                             'title': '2) Building a cybersecure organisation.'}
#
#         assert content.startswith('Unfortunately, cyber crime is not going away')
#
#     def test_content__incident_management(self):
#         raw_content = self.athena.content__incident_management()
#         metadata, content = frontmatter.parse(raw_content)
#         assert metadata  == { 'sidebar_position': 3                                   ,
#                               'title'           : '3) Incident management' }
#         assert content.startswith('Boards need to be prepared to detect')
#
#     def test_content__importance_of_digital_trust(self):
#         raw_content = self.athena.content__importance_of_digital_trust()
#         metadata, content = frontmatter.parse(raw_content)
#         assert metadata  == { 'sidebar_position': 4                                   ,
#                               'title'           : '4) The importance of digital trust.' }
#
#         assert content.startswith('When an organisation has a strong')
#
#
#     def test_first_question(self):
#         assert self.athena.first_question() == {'question': 'Hi, this is my first question'}
#
#     # def test_git_repo_status(self):
#     #     assert self.athena.git_repo_status() != {}
#
#     def test_route_map(self):
#         from fastapi.testclient import TestClient
#
#         app = FastAPI()
#         Bot_Athena(app)  # This will register the routes
#
#         client = TestClient(app)
#
#         # Get all registered routes
#         registered_routes = [route.path for route in app.routes if route.name != 'root']
#
#         # Only public methods should be registered as routes
#         public_methods = [method_name for method_name in dir(Bot_Athena) if not method_name.startswith('_')]
#
#         for method_name in public_methods:
#             assert f"/{method_name}" in registered_routes, f"Route for {method_name} not found"
#
#
#         # todo: fix this code which is not mocking ok the methods at the moment (i.e. code is still being invoked)
#         # from unittest.mock import patch
#         # with patch.multiple(Bot_Athena, **{method: (lambda x: "Mocked") for method in public_methods}):
#         #
#         #     # Test if the registered routes actually work by calling them
#         #     for route in registered_routes:
#         #         response = client.get(route)
#         #         assert response.status_code == 200, f"Route {route} did not return 200 OK"
#         #         print()
#         #         print(response.text)  # This should now print "Mocked"
#         #         return
#
#         # this will actually invoke all (which we don't really want)
#         # Test if the registered routes actually work by calling them
#         # for route in registered_routes:
#         #     response = client.get(route)
#         #     assert response.status_code == 200, f"Route {route} did not return 200 OK"
#         #     print(response.text)
