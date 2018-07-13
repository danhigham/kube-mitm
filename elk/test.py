import socket
import json
import sys

HOST = '10.0.0.54'
PORT = 32698

try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
  sys.exit(1)

msg = {'@message': 'python test message', '@tags': ['python', 'test']}

sock.sendto(bytes(json.dumps(msg), "utf-8"), (HOST, PORT))

sock.close()
sys.exit(0)
