from wsgiref.simple_server import make_server
from lithe.server import server


def run_server():
    httpd = make_server('', 8000, server)
    httpd.serve_forever()
