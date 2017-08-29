#!/usr/bin/env python3
import socket
from dns_generator import DNSGen

# Global variables
IP = "127.0.0.1"
PORT = 53


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, PORT))
    print("DNS Listening on {0}:{1} ...".format(IP, PORT))
    while True:
        data, address = sock.recvfrom(650)
        d = DNSGen(data)
        resp = d.make_response()
        sock.sendto(d.make_response(), address)
        print("Request from {0} for {1}".format(address, d.domain))


if __name__ == "__main__":
    main()
