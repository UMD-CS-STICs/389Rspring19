#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    hashes = # open and read hashes.txt
    passwords = # open and read passwords.txt
    characters = string.ascii_lowercase
    server_ip = 'put_your_ip_here'
    server_port = 00000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024)
    # parse data
    # crack 3 times

if __name__ == "__main__":
    server_crack()
