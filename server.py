from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST = '127.0.0.1'
PORT = 8000

class NoCacheRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, NoCacheRequestHandler)
    print(f'Serving HTTP on http://{HOST}:{PORT}/')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')
