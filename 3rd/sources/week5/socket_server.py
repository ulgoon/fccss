import socket
from time import ctime

host = 'localhost'
port = 12345
bufsiz = 1024
addr = (host, port)

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addr)
    server_socket.listen(5)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 3)
    
    while True:
        print("Server is listening..")
        client_sock, addr = server_socket.accept()
        print("Client connected from: ", addr)

        while True:
            data = client_sock.recv(bufsiz)
            if not data or data.decode("utf-8") == 'END':
                break

            print("received data from client: %s" % data.decode("utf-8"))
            print("Sending Server time: %s" % ctime())

            try:
                client_sock.send(bytes(ctime(), 'utf-8'))
            except KeyboardInterrupt:
                print("Exited by user")
        client_sock.close()
    server_socket.close()

