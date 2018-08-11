import socket


host = 'localhost'
port = 12345
bufsiz = 1024
addr = (host, port)

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(addr)

    payload = 'get time'
    
    while True:
        try:
            client_socket.send(payload.encode('utf-8'))
            data = client_socket.recv(bufsiz)
            print(data)
            if input("want more?(y/n)") == 'y':
                payload = input("type payload: ")
            else:
                break
        except:
            pass

    client_socket.close()
