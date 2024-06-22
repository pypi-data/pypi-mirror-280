import os
import uvicorn
from fastapi                                            import FastAPI
from starlette.middleware.cors                          import CORSMiddleware
from starlette.responses                                import RedirectResponse
from cbr_athena.fastapi.middleware.add_logging          import Middleware_Logging
from cbr_athena.fastapi.odin.api .Odin__FastAPI__API    import Odin__FastAPI__API
from cbr_athena.fastapi.odin.chat.Odin__FastAPI__Chat   import Odin__FastAPI__Chat
from cbr_athena.fastapi.routes.Routes__Auth             import Routes__Auth
from cbr_athena.fastapi.routes.Routes__Config           import Routes__Config
from cbr_athena.fastapi.routes.Routes__Content          import Routes__Content
from cbr_athena.fastapi.routes.Routes__Dev              import Routes__Dev
from cbr_athena.fastapi.routes.Routes__Logging          import Routes__Logging
from cbr_athena.fastapi.routes.Routes__Ollama import Routes__Ollama
from cbr_athena.fastapi.routes.Routes__OpenAI           import Routes__OpenAI
from cbr_athena.fastapi.routes.Routes__User             import Routes__User
from cbr_athena.utils.Utils                             import Utils
from osbot_utils.decorators.methods.cache_on_self       import cache_on_self


class FastAPI_Athena:

    def __enter__(self                           ): return self
    def __exit__ (self, exc_type, exc_val, exc_tb): return

    @cache_on_self
    def app(self):
        return FastAPI()

    def router(self):
        return self.app().router

    def setup(self):
        self.setup_routes()
        return self

    def add_middlewares(self, app):
        if os.getenv('ENVIRONMENT') == 'Dev':
            app.add_middleware(
                CORSMiddleware,
                allow_origins    = ["*"],  # Allows all origins
                allow_credentials= True ,
                allow_methods    = ["*"],  # Allows all methods
                allow_headers    = ["*"],  # Allows all headers
            )
        app.add_middleware(Middleware_Logging)

    def setup_routes(self):
        self.router().get("/")(self.redirect_to_docs)
        app = self.app()

        self.add_middlewares(app)
        #
        Routes__Auth    ().setup(app)
        Routes__Config  ().setup(app)
        Routes__Content ().setup(app)
        Routes__Dev     ().setup(app)
        Routes__Logging ().setup(app)
        Routes__OpenAI  ().setup(app)
        Routes__Ollama  ().setup(app)
        Routes__User    ().setup(app)

        self.setup_middleware()

        self.mount_other_fastapis()

    def mount_other_fastapis(self):

        Odin__FastAPI__API ().setup().mount(self.app())
        Odin__FastAPI__Chat().setup().mount(self.app())

    def setup_middleware(self):
        if Utils.current_execution_env() == 'LOCAL':
            # Configure CORS for local server manually since this is done automatically by AWS Lambda
            self.app().add_middleware(CORSMiddleware,
                                      allow_origins     = ["*"]                         ,
                                      allow_credentials = True                          ,
                                      allow_methods     = ["GET", "POST", "HEAD"]       ,
                                      allow_headers     = ["Content-Type", "X-Requested-With", "Origin", "Accept", "Authorization"],
                                      expose_headers    = ["Content-Type", "X-Requested-With", "Origin", "Accept", "Authorization"])

    def run_in_lambda(self):
        lambda_host = '127.0.0.1'
        lambda_port = 8080
        self.setup()
        kwargs = dict(app  =  self.app(),
                      host = lambda_host,
                      port = lambda_port)
        uvicorn.run(**kwargs)

    # default routes
    async def redirect_to_docs(self):
        return RedirectResponse(url="/docs")
