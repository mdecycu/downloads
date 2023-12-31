# 目前在一般 cmsimde 或 Replit 中都沒有用到此 script, 但仍保留, 且 cmsimde 目錄中與根目錄各一份
# 當採用 git clone --recurse-submodules 取下網頁倉儲後, 使用 main.py 啟動網頁編輯時必須在根目錄提供 nocache.py
from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)
