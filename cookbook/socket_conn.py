"""
LazyConnection
"""
from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:

    def __init__(self, sock_address, sock_family=AF_INET,
                 sock_type=SOCK_STREAM):
        self.sock_address = sock_address
        self.sock_family = sock_family
        self.sock_type = sock_type
        # self.sock = None
        self.connections = []

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError("Already connected.")
        self.sock = socket(self.sock_family, self.sock_type)
        self.sock.connect(self.sock_address)
        return self.sock

    def __exit__(self, exe_ty, exe_val, tab):
        # self.sock.close()
        # self.sock = None
        self.connections.pop().close()


from functools import partial


conn = LazyConnection(("www.python.org", 443))
with conn as s:
    s.send(b"GET /index.html HTTP/1.0\r\n")
    s.send(b"Host: www.python.org\r\n")
    s.send("\r\n")
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)

