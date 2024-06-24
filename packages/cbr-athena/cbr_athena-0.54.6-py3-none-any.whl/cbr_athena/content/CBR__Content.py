import cbr_static
from cbr_athena.utils.Version import version__cbr_athena

from osbot_utils.base_classes.Type_Safe import Type_Safe
from osbot_utils.utils.Files import path_combine, file_contents

FOLDER__STATIC_CONTENT   = 'content'
FOLDER__SECURITY_CONTENT = 'security-content'

class CBR__Content(Type_Safe):

    def content__cybersecurity_in_the_boardroom(self):
        return self.security_content('1-cybersecurity-in-the-boardroom.md')

    def content__building_a_cybersecure_organisation(self):
        return self.security_content('2-building-a-cybersecure-organisation.md')

    def content__incident_management(self):
        return self.security_content('3-Incident-management.md')

    def content__importance_of_digital_trust(self):
        return self.security_content('4-the-importance-of-digital-trust.md')

    def path_security_content(self):
        return path_combine(self.path_static_content(), FOLDER__SECURITY_CONTENT)

    def path_static_content(self):
        return path_combine(cbr_static.path,FOLDER__STATIC_CONTENT)

    def security_content(self, file_name):
        file_path = path_combine(self.path_security_content(), file_name)
        md_file_contents = file_contents(file_path)
        if md_file_contents:
            return md_file_contents +  f'\n*********\n\n{version__cbr_athena }'
        return f"(failed to retrieve content) in {file_path}"
