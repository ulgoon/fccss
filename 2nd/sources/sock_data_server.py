import socket
from time import ctime

# set host, port, buffer size, addr
host = 'localhost'
port = 12345
bufsiz = 1024
addr = (host, port)

# Main function
if __name__ == '__main__':
    # Create socket, bind with addr, listening
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addr)
    server_socket.listen(5)
    server_socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # when client connected
    while True:
        print("Server is listening...")
        client_sock, addr = server_socket.accept()
        print("Client connected")

        # receive data from client and send server time to client
        while True:
            data = client_sock.recv(bufsiz)
            if not data or data.decode('utf-8') == 'END':
                break

            print("received from client")
            print("sending the server time to client: ", ctime())

            try:
                client_sock.send(bytes(ctime(), 'utf-8'))
            except KeyboardInterrupt:
                print("Exited by user")

        # client socket close
        client_sock.close()
    # server socket close
    server_socket.close()










