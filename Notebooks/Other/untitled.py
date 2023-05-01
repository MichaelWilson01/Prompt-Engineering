import os

api_key_list = os.listdir("C:\\Users\\micha\\Desktop\\LLM_api_keys\\")

for file in api_key_list:
    with open('C:\\Users\\micha\\Desktop\\LLM_api_keys\\'+file) as f:
        os.environ[file] = f.readlines()[0].strip()
    
# with open('C:\\Users\\micha\\Desktop\\LLM_api_keys\\GOOGLE_API_KEY.txt') as f:
#     os.environ['GOOGLE_API_KEY'] = f.readlines()[0].strip()
    
# with open('C:\\Users\\micha\\Desktop\\LLM_api_keys\\GOOGLE_CSE_ID.txt') as f:
#     os.environ['GOOGLE_CSE_ID'] = f.readlines()[0].strip()