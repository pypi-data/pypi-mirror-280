# from cbr_athena.api.GitHub_Rest_API import GitHub_Rest_API
#
# TARGET_REPO = "the-cyber-boardroom/cbr-athena"
#
# class Repo__CBR_Athena(GitHub_Rest_API):
#
#     def __init__(self):
#         super().__init__(target_repo=TARGET_REPO)
#
#     def content__cybersecurity_in_the_boardroom(self):
#         file_path = 'docs/content/1-cybersecurity-in-the-boardroom.md'
#         return self.file_content(file_path)                #   todo: figure out if there is a way to defined when this is need
#                                                            #        vs using self.file_download(file_path) which is faster but is stuck in GH's update delays
#
#
#     def content__building_a_cybersecure_organisation(self):
#         file_path = 'docs/content/2-building-a-cybersecure-organisation.md'
#         return self.file_content(file_path)
#
#     def content__incident_management(self):
#         file_path = 'docs/content/3-Incident-management.md'
#         return self.file_content(file_path)
#
#     def content__importance_of_digital_trust(self):
#         file_path = 'docs/content/4-the-importance-of-digital-trust.md'
#         return self.file_content(file_path)