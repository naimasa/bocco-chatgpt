import os
from emo_platform import Client, Tokens, Head

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

# You can get ACCESS_TOKEN and REFRESH_TOKEN from the following URL.
# BOCCO emo Platform API https://platform-api.bocco.me/dashboard/login
ACCESS_TOKEN = ""
REFRESH_TOKEN = ""

client = Client(tokens=Tokens(access_token=ACCESS_TOKEN,
                refresh_token=REFRESH_TOKEN), token_file_path=CURRENT_DIR)
