import socket
from time import ctime


host = 'localhost'
port = 7070 #1024 over
bufsize = 1024
addr = (host, port)

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addr)
    server_socket.listen(5)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while True:
       print("Server is listening on {}:{}".format(host, port))
       client_socket, addr = server_socket.accept()
       print("Client connected: {}".format(addr))

       while True:
            data = client_socket.recv(bufsize)
            if not data or data.decode('utf-8') == '' or data.decode('utf-8') == 'END':
                break
            print("Client Payload: {}".format(data.decode('utf-8')))
            print("Sending Client time to Client: {}".format(ctime()))

            try:
                client_socket.send(bytes(ctime(), 'utf-8'))
            except KeyboardInterrupt:
                print("Exited by KeyboardInterrupt")

       client_socket.close()
    server_socket.close()
