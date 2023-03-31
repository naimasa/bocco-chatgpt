import os
import json
import http.server
from emo_platform import Client, WebHook, EmoPlatformError
import openai

# Please replace "OPENAI_API_KEY" with your API key.
# Account API Keys - OpenAI API https://platform.openai.com/account/api-keys
OPENAI_API_KEY = ""
openai.api_key = OPENAI_API_KEY

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
client = Client(token_file_path=CURRENT_DIR)

# Please replace "YOUR_WEBHOOK_URL" with the URL forwarded to http://localhost:8000
YOUR_WEBHOOK_URL = ""
client.create_webhook_setting(WebHook(YOUR_WEBHOOK_URL))

room_id_list = client.get_rooms_id()
room_client = client.create_room_client(room_id_list[0])
my_nickname = client.get_account_info().name


@client.event('message.received')
def message_callback(data):
    print("message received from " + data.data.message.user.nickname)

    # To avoid infinite callback loop
    if data.data.message.user.nickname == my_nickname:
        return

    # ALRIGHT_H_1
    room_client.send_motion("790de5c1-0a7e-47c1-861d-04df16cda7de")

    query = data.data.message.message.ja
    print("Query: " + query)

    messages = [
        {"role": "system", "content": "あなたの名前はエモちゃんです。質問に幼稚園のお友達でもわかる表現で3つの文以内で答えてくれる先生です。"},
        {"role": "user", "content": query}
    ]

    # ALRIGHT_H_2
    room_client.send_motion("117867c0-3668-407b-bf8d-ad7858c6bff2")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Bonbori_short
    room_client.send_motion("fa0beb73-ce8f-4786-9c0b-05ea5da9f125")

    response = completion.choices[0].message.content
    print("Response: " + response)

    room_client.send_msg(response)


@client.event('illuminance.changed')
def illuminance_callback(data):
    print("illuminance changed")
    print(data)


secret_key = client.start_webhook_event()


# localserver
class Handler(http.server.BaseHTTPRequestHandler):
    def _send_status(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

    def do_POST(self):
        # check secret_key
        if not secret_key == self.headers["X-Platform-Api-Secret"]:
            self._send_status(401)
            return

        content_len = int(self.headers['content-length'])
        request_body = json.loads(self.rfile.read(content_len).decode('utf-8'))

        try:
            cb_func, emo_webhook_body = client.get_cb_func(request_body)
        except EmoPlatformError:
            self._send_status(501)
            return

        cb_func(emo_webhook_body)

        self._send_status(200)


with http.server.HTTPServer(('', 8000), Handler) as httpd:
    httpd.serve_forever()
