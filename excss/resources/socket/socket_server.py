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

    while True:
        print('Server is Listening..')
        client_socket, addr = server_socket.accept()
        print('Client connected:', addr)

        while True:
            data = client_socket.recv(bufsiz)
            
            if not data or data.decode('utf-8') == 'END':
                break
            print("received from client: {}".format(data.decode('utf-8')))
            print("Sending data to client:{}".format(ctime()))

            try:
                client_socket.send(bytes(ctime(),'utf-8'))
            except:
                print('send failed')

        client_socket.close()

    server_socket.close()





