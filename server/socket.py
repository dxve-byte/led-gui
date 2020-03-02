import sockets # req

# sockets = communication to server
s = socket.socket()
host = "localhost"
port = 96
s.bind((host, port))

s.listen(5)
while True:
   c, addr = s.accept()
   data = c.recv(1024)
   if data: print(data)
   c.close()
