import socket


host = 'localhost'
port = 7070
bufsize = 4096
addr = (host, port)

if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Type hostname: ") or host
    port = input("Type portnumber: ") or port
    addr = (host, port)

    client_sock.connect(addr)
    payload = 'GET TIME'

    try:
        while True:
            client_sock.send(payload.encode('utf-8'))
            data = client_sock.recv(bufsize)
            if not data:
                break
            print(repr(data))
            more = input("Want more?(y/n) ")
            if more.lower() == "y":
                payload = input("Type Command: ")
            else:
                break
    except:
        print("Something went wrong")

    client_sock.close()
