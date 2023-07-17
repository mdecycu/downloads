# 這個檔案用於 Replit, 以下的 cp 為網頁倉儲對應的目錄名稱
# 此 main.py 適用於並非以 import 導入 Replit 的網頁倉儲
from cp.cmsimde import flaskapp
from gevent.pywsgi import WSGIServer

#flaskapp.app.run(host="0.0.0.0", debug=True)
http_server = WSGIServer(('0.0.0.0', 8080), flaskapp.app)
http_server.serve_forever()
