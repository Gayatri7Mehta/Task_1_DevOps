from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Hello World</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 50px;
                    background-color: yellow;
                }
                .footer {
                    position: fixed;
                    left: 0;
                    bottom: 0;
                    width: 100%;
                    background-color: #333;
                    color: white;
                    text-align: center;
                    padding: 10px 0;
                }
            </style>
        </head>
        <body>
            <h1>Hello, world!</h1>
            <div class="footer">Created by Gayatri Mehta</div>
        </body>
        </html>
        """

        self.wfile.write(html_content.encode('utf-8'))

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleServer)
    print('Server running at localhost:8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
