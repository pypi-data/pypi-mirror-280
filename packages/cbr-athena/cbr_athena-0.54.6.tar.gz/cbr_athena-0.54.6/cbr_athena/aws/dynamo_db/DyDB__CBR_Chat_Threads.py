from cbr_athena.schemas.Chat_Thread                                     import Chat_Thread
from cbr_athena.schemas.for_fastapi. GPT_Prompt_With_System_And_History import GPT_Prompt_With_System_And_History
from cbr_athena.utils.Utils                                             import Utils
from osbot_aws.aws.dynamo_db.domains.DyDB__Table_With_Timestamp         import DyDB__Table_With_Timestamp
from osbot_utils.utils.Misc                                             import date_time_now


DYNAMO_DB__TABLE_NAME__CHAT_THREADS = '{env}__cbr_chat_threads'
TABLE_CHAT_THREADS__INDEXES_NAMES   = [ 'date', 'user_name', 'chat_thread_id']

class DyDB__CBR_Chat_Threads(DyDB__Table_With_Timestamp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.table_name    = DYNAMO_DB__TABLE_NAME__CHAT_THREADS.format(env=Utils.current_execution_env())
        self.table_indexes = TABLE_CHAT_THREADS__INDEXES_NAMES

    def add_chat_thread(self, chat_thread : Chat_Thread):
        chat_thread.date = self.date_today()                                       # make sure date field is set
        document         = chat_thread.json()
        response         = super().add_document(document)
        if response.get('document'):
            return response.get('document', {}).get('id')
        return response

    def add_prompt_request(self, gpt_prompt_with_system_and_history: GPT_Prompt_With_System_And_History, gpt_response:str, request_headers:dict, source='Athena'):
        prompt_data = gpt_prompt_with_system_and_history.dict()

        user_prompt    = prompt_data.get('user_prompt'   ) or 'NA'
        user_data      = prompt_data.get('user_data'     ) or {}
        session_id     = user_data.get('session_id'      ) or 'NA'
        chat_thread_id = prompt_data.get('chat_thread_id') or 'NA'
        user_name      = 'NA'
        chat_kwargs = dict(user_prompt     = user_prompt     ,
                           session_id      = session_id      ,
                           user_name       = user_name       ,
                           chat_thread_id  = chat_thread_id  ,
                           gpt_response    = gpt_response    ,
                           source          = source          ,
                           prompt_data     = prompt_data     ,
                           request_headers = request_headers )

        cbr_logging = Chat_Thread(**chat_kwargs)

        return self.add_chat_thread(cbr_logging)

    def date_today(self):
        return date_time_now(date_time_format='%Y-%m-%d')       # force the correct value of date

dydb_cbr_chat_threads = DyDB__CBR_Chat_Threads