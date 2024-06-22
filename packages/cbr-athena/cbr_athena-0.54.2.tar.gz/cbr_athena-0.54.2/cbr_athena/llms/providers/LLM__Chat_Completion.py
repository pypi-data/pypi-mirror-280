import requests

from osbot_utils.base_classes.Kwargs_To_Self import Kwargs_To_Self
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Misc import wait_for
from osbot_utils.utils.Status import status_error


class LLM__Chat_Completion(Kwargs_To_Self):
    base_url : str
    api_key  : str
    model    : str
    messages : list

    def add_message__system(self, system_prompt):
        self.add_message('system', system_prompt)
        return self

    def add_message__user(self, user_prompt):
        self.add_message('user', user_prompt)
        return self

    def add_messages__system(self, system_prompts):
        for system_prompt in system_prompts:
            self.add_message__system(system_prompt)
        return self

    def add_messages__user(self, user_prompts):
        for user_prompt in user_prompts:
            self.add_message__user(user_prompt)
        return self


    def add_message(self, role, content):
        message = {'role': role, 'content': content}
        self.messages.append(message)
        return self

    def json_data(self):
        payload = { "messages": self.messages,
                    "model"   : self.model  }
        return payload

    def make_request(self, post_data):
        response  = requests.post(**post_data)
        if response.status_code == 200:
            if response.headers['Content-Type'] == 'application/x-ndjson':
                return response
            else:
                return response.json()
        else:
            return status_error(error=response.text, message=f'request failed with status code: {response.status_code}')

    def post_data(self):
        url     = self.base_url
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers['Authorization'] = f"Bearer {self.api_key}"
        json    = self.json_data()
        return dict(url=url, headers=headers, json=json)

    def send_post_data(self):
        post_data = self.post_data()
        return self.make_request(post_data=post_data)

    def send_user_prompt(self, user_prompt):                # todo: see if we need this
        self.add_message__user(user_prompt)
        post_data = self.post_data()
        #pprint(post_data)
        return self.make_request(post_data=post_data)