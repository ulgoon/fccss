import socket
import sys


if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Failed")
        print("Reason: %s" % str(e))
        sys.exit();

    print("socket created")
    
    host = input("Enter host: ")
    port = input("Enter port: ")

    try:
        sock.connect((host, int(port)))
        print("socket connected")
        sock.shutdown(2)
    except socket.error as err:
        print("Failed")
        print("Reason: ", str(err))
        sys.exit();






