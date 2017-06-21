#!/usr/bin/env python3
import socket
import json

# Global variables
IP = "127.0.0.1"
PORT = 53


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, PORT))
    print("DNS Listening on {0}:{1} ...".format(IP, PORT))
    while True:
        data, addr = sock.recv_into(650)
        print("Request from {0}".format(addr))

if __name__ == "__main__":
    main()
    