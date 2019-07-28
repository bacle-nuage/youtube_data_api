# coding: UTF-8

import requests
import json

YOUTUBE_API_URL = 'https://www.googleapis.com'
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# ベースURL
def get_base_url():
    return YOUTUBE_API_URL + '/' + YOUTUBE_API_SERVICE_NAME + '/' + YOUTUBE_API_VERSION

# HTTPリクエスト
def request(method:str, query:str, api_key:str):
    url = get_base_url() + '/' + method + query + '&key=' + api_key
    res = requests.get(url)
    return json.dumps(res.json())

# チャンネルIDで情報取得
def channel(args):
    channel_id = args.channel_id
    api_key    = args.api_key
    res = request('channels', '?part=statistics&id=' + channel_id, api_key)
    return res

