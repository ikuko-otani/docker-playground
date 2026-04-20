# D-03: Build, Tag, and Run Images — sample application
# 日本語訳：D-03 演習用サンプルアプリケーション
# TODO: Fill this file following the lesson guide.

# A minimal HTTP server to verify the container is running.
# コンテナが起動していることを確認するための最小限のHTTPサーバー。
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        # TODO: Change this message in Step 2 and rebuild to observe layer cache behaviour.
        # ヒント：Step 2 でこのメッセージを変更して再ビルドし、レイヤーキャッシュの動作を観察してください。
        self.wfile.write(b"Hello from D-03!")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Listening on port 8080...")
    server.serve_forever()
