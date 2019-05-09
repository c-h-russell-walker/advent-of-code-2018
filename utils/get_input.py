import os

import requests


def get_from_url(url):
    session_cookie = os.environ.get('SESSION_COOKIE')
    resp = requests.get(url, cookies={'session': session_cookie})

    return resp.text
