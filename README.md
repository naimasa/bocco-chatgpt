# Bocco Emo - ChatGPT

## References
* GitHub - YUKAI/emo-platform-api-python https://github.com/YUKAI/emo-platform-api-python


## Prerequisite
* Install `ngrok`
```
brew install ngrok/ngrok/ngrok
```
* Install the required packages
```
pip install -r requirements.txt
```
* Generate Bocco API Token
    * Fill out `ACCESS_TOKEN` and `REFRESH_TOKEN` in the `generate-token.py` file.
    * Run `generate-token.py`
    * You'll get `emo-platform-api_previous.json` and `emo-platform-api.json` files.
```
python3 generate-token.py
```

## Usage
1. Run `ngrok` and get a Webhook URL
```
ngrok http 8000
```
2. Modify `bocco-chatgpt.py` with the obtained Webhook URL
3. Modify `bocco-chatgpt.py` with the OpenAI API Key, which is available at Account API Keys - OpenAI API https://platform.openai.com/account/api-keys
4. Run `bocco-chatgpt.py`
```
python3 bocco-chatgpt.py
```