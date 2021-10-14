import socket
import sys

address = "<IP ADDRESS>"

def routeInput(self, input, output):
  input -= 1
  output -= 1
  return "VIDEO OUTPUT ROUTING:\n%s %d\n\n" %(output, input)

BUFFER_SIZE = 2048

# print(routeInput(sys.argv[0], int(sys.argv[1]), int(sys.argv[2])))

smarthubSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
smarthubSocket.connect(("192.168.1." + address, 9990))
smarthubSocket.send(routeInput(sys.argv[0], int(sys.argv[1]), int(sys.argv[2])))
data = smarthubSocket.recv(BUFFER_SIZE)
smarthubSocket.close

#print "Received data:\n\n", data
