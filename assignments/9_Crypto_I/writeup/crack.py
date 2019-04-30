#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = open('hashes.txt') # open and read hashes.txt
    passwords = open('passwords.txt')  # open and read passwords.txt
    characters = string.ascii_lowercase
    
    for p in passwords:
        for c in characters:
            # crack hashes
            val = c + p
            #print(val)
            h = hashlib.sha256(val.encode('ascii'))
            po = 'dbec1495345f5a1573a0dd437c207cacc844f74b8a7b030c858f4f660bf9484f'
            #print(h.hexdigest())
            if h.hexdigest() == po:
                print(val +' : ' + h.hexdigest())
            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
