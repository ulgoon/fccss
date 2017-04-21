import socket
import sys

# Main Function
if __name__ == '__main__':
    # try to create socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Failed")
        print("Reason: %s" % str(e))
        sys.exit();

    print("socket created")
    
    # get host, port from user
    host = input("Enter host: ")
    port = input("Enter port: ")

    # try to connect to host, port and shutdown socket
    try:
        sock.connect((host, int(port)))
        print("socket connected")
        sock.shutdown(2)
    except socket.error as err:
        print("Failed")
        print("Reason: ", str(err))
        sys.exit();






