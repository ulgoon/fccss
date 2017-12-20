import socket


host = 'localhost'
port = 12345
bufsize = 4096
# addr = (host, port)

if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Enter the hostname:[%s] " % host) or host
    port = input("Enter the portname:[%s] " % port) or port

    sock_addr = (host, int(port))
    client_sock.connect(sock_addr)

    payload = "GET TIME"

    try:
        while True:
            client_sock.send(payload.encode('utf-8'))
            data = client_sock.recv(bufsize)
            if not data:
                break
            print(repr(data))
            more = input("Want more? [y/n]")
            if more.lower() == "y":
                payload = input("Type Payload: ")
            else:
                break
    except KeyboardInterrupt:
        print("Exited by user")

    client_sock.close()
