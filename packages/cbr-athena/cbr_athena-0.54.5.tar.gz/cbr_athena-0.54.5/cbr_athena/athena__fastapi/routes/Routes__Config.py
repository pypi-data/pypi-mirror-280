from cbr_athena.athena__fastapi.routes.Fast_API_Route import Fast_API__Routes
from cbr_athena.utils.Version import Version

class Routes__Config(Fast_API__Routes):
    path_prefix: str = "config"

    def add_routes(self):
        @self.router.get('/version')
        def version():
            return {"version": Version().version()}