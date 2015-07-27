import socket
h=socket.gethostbyname(socket.gethostname())
ip=socket.gethostbyname_ex(socket.gethostname())
print(h)
print(ip)
