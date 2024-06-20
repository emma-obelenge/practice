#!/usr/bin/python3

import socket

def list_open_ports():
    open_ports = []
    for port in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    open_ports = list_open_ports()
    print("Open ports:")
    for port in open_ports:
        print(port)

