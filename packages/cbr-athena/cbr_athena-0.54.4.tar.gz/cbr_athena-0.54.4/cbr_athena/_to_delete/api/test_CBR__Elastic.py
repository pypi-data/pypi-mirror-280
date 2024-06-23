# from datetime import datetime
# from unittest import TestCase
#
# import pytest
# from dotenv import load_dotenv
#
# from cbr_athena.api.CBR__Elastic import CBR__Elastic
# from osbot_utils.context_managers.capture_duration import print_duration
# from osbot_utils.utils.Dev import pprint
# from osbot_utils.utils.Misc import timestamp_utc_now
# from osbot_utils.utils.Objects import obj_info
#
#
# class test_CBR__Elastic(TestCase):
#
#     cbr_elastic : CBR__Elastic
#
#     @classmethod
#     def setUpClass(cls):
#         load_dotenv()
#         cls.cbr_elastic = CBR__Elastic()
#
#     @pytest.mark.skip("needs to be implemented using lambda")
#     def test_info(self):
#         with self.cbr_elastic as _:
#             info_body = _.info().body
#             assert info_body == { 'cluster_name': info_body.get('cluster_name'),
#                                   'cluster_uuid': info_body.get('cluster_uuid'),
#                                   'name'        : info_body.get('name'),
#                                   'tagline'     : 'You Know, for Search',
#                                   'version'     : info_body.get('version')}
#
#     @pytest.mark.skip("needs to be implemented using lambda")
#     def test_send_documents(self):
#         documents = [ {'index': {'_id': '9780553351', '_index': 'books'}},
#                       { 'author': 'CCCCCC',
#                         'name': 'Snow Crash',
#                         'page_count': 470,
#                         'release_date': '1992-06-01'},
#                       {'index': {'_id': '9780441017225', '_index': 'books'}},
#                       { 'author': 'Alastair Reynolds',
#                         'name': 'Revelation Space',
#                         'page_count': 585,
#                         'release_date': '2000-03-15'},
#                       {'index': {'_id': '9780451524935', '_index': 'books'}},
#                       { 'author': 'George Orwell',
#                         'name': '1984',
#                         'page_count': 328,
#                         'release_date': '1985-06-01'},
#                       {'index': {'_id': '9781451673319', '_index': 'books'}},
#                       { 'author': 'Ray Bradbury',
#                         'name': 'Fahrenheit 451',
#                         'page_count': 227,
#                         'release_date': '1953-10-15'},
#                       {'index': {'_id': '9780060850524', '_index': 'books'}},
#                       { 'author': 'Aldous Huxley',
#                         'name': 'Brave New World',
#                         'page_count': 268,
#                         'release_date': '1932-06-01'},
#                       {'index': {'_id': '9780385490818', '_index': 'books'}},
#                       { 'author': 'Margaret Atwood',
#                         'name': "The Handmaid's Tale",
#                         'page_count': 311,
#                         'release_date': '1985-06-01'}]
#         #pprint(documents)
#
#         # with print_duration():
#         #     result = client.bulk(operations=documents)
#         #     pprint(result)
#
#         # doc = {
#         #     'name' : 'this is the name',
#         #     'author': 'author',
#         #     'text': 'Some content',
#         #     'timestamp': timestamp_utc_now(),
#         # }
#         # resp = client.index(index="books", id=2, document=doc)
#         # pprint(resp)