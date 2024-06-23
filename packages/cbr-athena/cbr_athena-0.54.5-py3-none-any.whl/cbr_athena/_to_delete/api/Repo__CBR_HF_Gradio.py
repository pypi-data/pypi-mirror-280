# from cbr_athena.api.GitHub_Rest_API import GitHub_Rest_API
#
# TARGET_REPO = "the-cyber-boardroom/cbr-hf-gradio"
#
# class Repo__CBR_HF_Gradio(GitHub_Rest_API):
#
#     def __init__(self):
#         super().__init__(target_repo=TARGET_REPO)
#
#     def athena_prompt(self):
#         file_path = 'docs/prompts/athena_main_prompt.txt'
#         #return self.file_download(file_path)               # faster but issue with GH taking almost 1 minute to update the 'https://raw.githubusercontent.com/'
#         return self.file_content(file_path)
