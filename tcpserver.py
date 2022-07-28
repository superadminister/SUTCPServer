""" From socketserver.py program is had assembled """

import socketserver


class RequestsHandler(socketserver.BaseRequestHandler):

    def setup(self) -> None:
        self.conn, self.addr = self.server.get_request()
        self.data = None

    def handle(self) -> None:
        self.conn.send(b'from server is connecting ..')
        print(self.conn.recv(1024))

    def finish(self) -> None:
        self.server.close_request(request=self.conn)
        self.server.shutdown_request(request=self.conn)
        self.server.process_request(
            request=self.request,
            client_address=self.client_address
        )


class TCP(socketserver.TCPServer, socketserver.ThreadingMixIn):
    daemon_threads = True

    def service_actions(self) -> None:
        self.RequestHandlerClass(
            self.socket,
            self.server_address,
            self
        )
