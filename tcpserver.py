""" From socketserver.py program is had assembled """

from socketserver import *


class RequestHandler(BaseRequestHandler):
    """ Class is for request handler a data, all operations of BaseServer class is here (operators) """

    def __init__(self, request, client_address, server):
        super(RequestHandler, self).__init__(request, client_address, server)
        self.data = None
        self.conn, self.addr = (None, None)

    def handle(self) -> None:
        data = self.conn.recv(5000)
        self.data = data.decode()
        self.conn.send(f'{self.addr} \n {self.conn}'.encode())

    def setup(self) -> None:
        self.conn, self.addr = self.server.get_request()

    def finish(self) -> None:
        self.server.service_actions()


class SUTCPServer(TCPServer, ThreadingMixIn):
    """ This class calling a BaseRequestHandler-RequestHandler is class (getter necessary program) """

    daemon_threads = True

    def service_actions(self):
        self.process_request(
            request=self.socket,
            client_address=self.server_address
        )


TCPServer = SUTCPServer(
        server_address=('127.0.0.1', 65000),
        RequestHandlerClass=RequestHandler,
        bind_and_activate=True
    )

TCPServer.serve_forever()
