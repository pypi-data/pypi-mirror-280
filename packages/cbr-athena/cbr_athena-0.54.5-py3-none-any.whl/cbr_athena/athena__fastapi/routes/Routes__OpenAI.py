from starlette.responses import StreamingResponse, Response

from fastapi import Request, UploadFile, File

from cbr_athena.aws.dynamo_db.DyDB__CBR_Chat_Threads                    import DyDB__CBR_Chat_Threads
from cbr_athena.athena__fastapi.routes.Fast_API_Route                           import Fast_API__Routes
from cbr_athena.llms.API_Open_AI                                        import API_Open_AI
from cbr_athena.schemas.for_fastapi.GPT_Audio_To_Text                   import GPT_Audio_To_Text
from cbr_athena.schemas.for_fastapi.GPT_Prompt_With_System_And_History  import GPT_Prompt_With_System_And_History
from cbr_athena.schemas.for_fastapi.GPT_Text_To_Audio                   import GPT_Text_To_Audio
from cbr_athena.utils.Logging                                           import Logging
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Misc import base64_to_bytes, bytes_to_base64, wait_for


class Routes__OpenAI(Fast_API__Routes):
    path_prefix: str = 'open_ai'

    def __init__(self):
        super().__init__()
        self.api_open_ai = API_Open_AI().setup()
        self.logging     = Logging()
        self.dydb_chat_threads = DyDB__CBR_Chat_Threads()

    def add_routes(self):
        @self.router.post('/prompt_with_system__stream')
        async def prompt_with_system__stream(gpt_prompt_with_system_and_history: GPT_Prompt_With_System_And_History, request: Request):  # = Depends()):
            async def streamer():
                user_prompt     = gpt_prompt_with_system_and_history.user_prompt
                images          = gpt_prompt_with_system_and_history.images
                system_prompts  = gpt_prompt_with_system_and_history.system_prompts
                histories       = gpt_prompt_with_system_and_history.histories
                model           = gpt_prompt_with_system_and_history.model.value
                temperature     = gpt_prompt_with_system_and_history.temperature
                seed            = gpt_prompt_with_system_and_history.seed
                max_tokens      = gpt_prompt_with_system_and_history.max_tokens
                async_mode      = True
                generator       = await self.api_open_ai.ask_using_system_prompts(user_prompt=user_prompt,
                                                                                  images=images,
                                                                                  system_prompts=system_prompts,
                                                                                  histories=histories,
                                                                                  model=model,
                                                                                  temperature=temperature,
                                                                                  seed=seed,
                                                                                  max_tokens=max_tokens,
                                                                                  async_mode=async_mode)

                gpt_response = ''
                async for answer in generator:
                    if answer:
                        gpt_response += answer
                        yield f"{answer}\n"

                request_headers  = {key: value for key, value in request.headers.items()}
                kwargs = dict(gpt_prompt_with_system_and_history = gpt_prompt_with_system_and_history ,
                              gpt_response                       = gpt_response                       ,
                              request_headers                    = request_headers                    ,
                              source                             = 'Athena'                           )
                self.dydb_chat_threads.add_prompt_request(**kwargs)
                #self.logging          .add_prompt_request(gpt_prompt_with_system_and_history, gtp_response, request_headers)  # todo: remove this one once the dydb_chat_threads is working
            return StreamingResponse(streamer(), media_type='text/event-stream"; charset=utf-8')

        @self.router.post('/audio_to_text')
        async def audio_to_text(gpt_audio_to_text: GPT_Audio_To_Text):
            audio_base_64 = gpt_audio_to_text.audio_base_64
            audio_bytes   = base64_to_bytes(audio_base_64)
            audio_text    = self.api_open_ai.audio_to_text(audio_bytes=audio_bytes)

            return Response(content=audio_text, media_type="text/plain")

        @self.router.post('/text_to_audio')
        async def text_to_audio(gpt_text_to_audio: GPT_Text_To_Audio):
            input_text  = gpt_text_to_audio.audio_text
            audio_bytes = self.api_open_ai.text_to_audio(input_text)
            audio_base_64 = bytes_to_base64(audio_bytes)
            return Response(content=audio_base_64, media_type="text/plain")
