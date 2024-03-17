#!/usr/bin/env python3
import sys
import socket


def get_accessible_ports(address, min_port, max_port):
    found_ports = []
    for port in range(min_port,max_port):
    s = socket.socket()

    try:
        # tries to connect to host using that port
        s.connect((host, port))
    except:
        # cannot connect, port is closed
        # return false
        #return False
    else:
        # the connection was established, port is open!
        #print(f"{port}")
        return port

    # write code here

    return found_ports


def main(argv):
    address = sys.argv[1]
    min_port = int(sys.argv[2])
    max_port = int(sys.argv[3])
    ports = get_accessible_ports(address, min_port, max_port)
    for p in ports:
        print(p)

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('usage: python %s address min_port max_port' % sys.argv[0])
    else:
        main(sys.argv)