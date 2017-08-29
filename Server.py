#!/usr/bin/env python3
import socket

from dns_generator import ClientHandler

# Global variables
IP = "127.0.0.1"
PORT = 53


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, PORT))
    print("DNS Listening on {0}:{1} ...".format(IP, PORT))
    while True:
        data, address = sock.recvfrom(650)
        client = ClientHandler(address, data, sock)
        client.run()


if __name__ == "__main__":
    main()
