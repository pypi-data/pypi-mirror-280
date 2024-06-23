# from fastapi import FastAPI
# from starlette.responses import StreamingResponse
#
# import cbr_athena
# #from cbr_athena.api.Repo__CBR_Athena import Repo__CBR_Athena
# #from cbr_athena.api.Repo__CBR_HF_Gradio import Repo__CBR_HF_Gradio
# from cbr_athena.llms.API_Open_AI import API_Open_AI
# from cbr_athena.bots.GPT_Prompt import GPT_Prompt_With_System_And_History
# #from cbr_athena.utils.Git_Repo_Status import Git_Repo_Status
# from cbr_athena.utils.Version import Version
#
#
# # todo refactor to helper class
# def route_map(cls_instance, app: FastAPI):
#     for method_name in dir(cls_instance):
#         if not method_name.startswith('_'):  # skip private and built-in methods
#             method = getattr(cls_instance, method_name)
#             if callable(method):
#                 app.add_api_route(f"/{method_name}", method)
#
# def root():
#     return {"name": "Athena",
#             "version" : Version().version()}
#
# def add_extra_methods(app: FastAPI):
#     api_open_ai = API_Open_AI()
#
#     @app.post("/prompt_with_system__stream")
#     async def prompt_with_system__stream(gpt_prompt_with_system_and_history: GPT_Prompt_With_System_And_History):  # = Depends()):
#         async def streamer():
#             user_prompt     = gpt_prompt_with_system_and_history.user_prompt
#             images          = gpt_prompt_with_system_and_history.images
#             system_prompts  = gpt_prompt_with_system_and_history.system_prompts
#             histories       = gpt_prompt_with_system_and_history.histories
#             model           = gpt_prompt_with_system_and_history.model.value
#             temperature     = gpt_prompt_with_system_and_history.temperature
#             seed            = gpt_prompt_with_system_and_history.seed
#             max_tokens      = gpt_prompt_with_system_and_history.max_tokens
#             async_mode      = True
#             generator =      api_open_ai.ask_using_system_prompts(user_prompt=user_prompt,
#                                                                   images=images,
#                                                                   system_prompts=system_prompts,
#                                                                   histories=histories,
#                                                                   model=model,
#                                                                   temperature=temperature,
#                                                                   seed=seed,
#                                                                   max_tokens=max_tokens,
#                                                                   async_mode=async_mode)
#             for answer in generator:
#                 if answer:
#                     yield f"{answer}\n"
#
#         return StreamingResponse(streamer(), media_type="text/plain; charset=utf-8")
#
# class Bot_Athena:
#     def __init__(self, app: FastAPI):
#         add_extra_methods(app)
#
#
#         #self.repo__cbr_athena    = Repo__CBR_Athena()
#         #self.repo__cbr_hf_gradio = Repo__CBR_HF_Gradio()
#         app.add_api_route("/", root)
#         route_map(self, app)
#
#
#
#     # def athena_prompt(self):
#     #     return self.repo__cbr_hf_gradio.athena_prompt()
#
#     def content__cybersecurity_in_the_boardroom(self):
#         return self.repo__cbr_athena.content__cybersecurity_in_the_boardroom()
#
#     def content__building_a_cybersecure_organisation(self):
#         return self.repo__cbr_athena.content__building_a_cybersecure_organisation()
#
#     def content__incident_management(self):
#         return self.repo__cbr_athena.content__incident_management()
#
#     def content__importance_of_digital_trust(self):
#         return self.repo__cbr_athena.content__importance_of_digital_trust()
#
#     def first_question(self):
#         return {"question" : "Hi, this is my first question" }
#
#     # def git_repo_status(self):
#     #     return Git_Repo_Status().get_status()
#
#     def version(self):
#         return { "version": Version().version()}
#
#     def ping(self):
#         return {"ping": "pong"}
#
#
#
#
#
#     # def secure_endpoint(self, api_key: str = None):
#     #     if api_key != "your-expected-api-key":
#     #         raise HTTPException(status_code=401, detail="Unauthorized")
#     #     return {"message": "You are authorized!"}