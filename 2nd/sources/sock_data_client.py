import socket

# set host, port, buffer size, address
host = 'localhost'
port = 12345
bufsiz = 4096
addr = (host, port)

# main function
if __name__ == '__main__':
    # create socket and connect with addr
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(addr)

    # send data and get response
    while True:
        data = 'GET / HTTP/1.0\r\n\r\n'
        if not data:
            break
        client_sock.send(data.encode('utf-8'))
        data = client_sock.recv(bufsiz)

        if not data:
            break
        print(data.decode('utf-8'))

    # socket close
    client_sock.close()
