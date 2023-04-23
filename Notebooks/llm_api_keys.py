import os

api_key_list = os.listdir("C:\\Users\\micha\\Documents\\GitHub\\Prompt-Engineering\\hidden_folder\\LLM_api_keys\\")

for file in api_key_list:
    with open("C:\\Users\\micha\\Documents\\GitHub\\Prompt-Engineering\\hidden_folder\\LLM_api_keys\\"+file) as f:
        os.environ[file[:-4]] = f.readlines()[0].strip()