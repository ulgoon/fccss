import socket
from time import ctime


host = 'localhost'
port = 12345
bufsize = 1024

addr = (host, port)

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addr)
    server_socket.listen(5)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while True:
        print("Server is waiting for connection...")
        client_socket, addr = server_socket.accept()
        print("Client connected from: ", addr)

        while True:
            data = client_socket.recv(bufsize)
            if not data or data.decode('utf-8') == "END":
                break
            print("Received from client: %s" % data.decode('utf-8'))
            print("Sending server time to client: %s" % ctime())

            try:
                client_socket.send(bytes(ctime(), 'utf-8'))
            except KeyboardInterrupt:
                print("Exited by KBDInterrupt")

        client_socket.close()
    server_socket.close()
