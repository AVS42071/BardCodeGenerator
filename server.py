from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/editor":
            self.path = "/GitHubCodeEditor.py"

        super().do_GET()

if __name__ == "__main__":
    server = HTTPServer(("", 5000), MyHandler)
    server.serve_forever()
