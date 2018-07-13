import socket
import json
import sys

class LogRequests:
    def __init__(self):
        self.host = '10.0.0.54'
        self.port = 32698


    def request(self, flow):
        msg = {'@request': flow.request}

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error:
            sys.exit(1)

        sock.sendto(bytes(json.dumps(msg), "utf-8"), (self.host, self.port))

        sock.close()

addons = [
    LogRequests()
]
