#!/usr/bin/env python3

import hashlib
import string
import socket 
import time

def crack( data, passwords, characters, s):
    for p in passwords:
        for c in characters:
            # crack hashes
            val = c + p.rstrip()
            #print(val)
            h = hashlib.sha256(val.encode('ascii'))
            #print(h.hexdigest())
            hd = hashlib.new('sha256', data)
            #print(hd.hexdigest())
            if h.hexdigest() == hd.hexdigest():
                s.send((val +'\n').encode())

def server_crack():
    passwords = open('passwords.txt')  # open and read passwords.txt
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    # parse data
    # crack 3 times

    data = s.recv(1024)
    crack(data, passwords, characters, s)
    time.sleep(1)
    data = s.recv(1024)
    crack(data, passwords, characters, s)
    time.sleep(1)
    data = s.recv(1024)
    crack(data, passwords, characters, s)
    time.sleep(1)
    
if __name__ == "__main__":
    server_crack()
