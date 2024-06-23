from cbr_athena.content.CBR__Content                import CBR__Content
from cbr_athena.athena__fastapi.routes.Fast_API_Route       import Fast_API__Routes
from osbot_utils.decorators.methods.cache_on_self   import cache_on_self


class Routes__Content(Fast_API__Routes):
    path_prefix: str = "content"

    # def __init__(self):
    #     super().__init__()
    #     load_dotenv()
    #     # self.db_cbr_content      = DB__CBR__Content   ()              #.setup()
    #     # DB__CBR__Content().setup()                                    # can't create the db here since we hit on a sqlite thread issue

    @cache_on_self
    def cbr_content(self):
        return CBR__Content()

    def add_routes(self):

        @self.router.get('/cybersecurity_in_the_boardroom')
        def content__cybersecurity_in_the_boardroom():
            return self.cbr_content().content__cybersecurity_in_the_boardroom()

        @self.router.get('/building_a_cybersecure_organisation')
        def content__building_a_cybersecure_organisation():
            return self.cbr_content().content__building_a_cybersecure_organisation()

        @self.router.get('/incident_management')
        def content__incident_management():
            return self.cbr_content().content__incident_management()

        @self.router.get('/importance_of_digital_trust')
        def content__importance_of_digital_trust():
            return self.cbr_content().content__importance_of_digital_trust()