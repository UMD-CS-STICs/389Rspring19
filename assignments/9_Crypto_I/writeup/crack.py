#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = [l.rstrip() for l in open('hashes.txt')] # open and read hashes.txt
    passwords = open('passwords.txt')  # open and read passwords.txt
    characters = string.ascii_lowercase
    
    for p in passwords:
        for c in characters:
            # crack hashes
            val = c + p.rstrip()
            #print(val)
            h = hashlib.sha256(val.encode('ascii'))
            #print(h.hexdigest())
            if h.hexdigest() in hashes:
                print(val +' : ' + h.hexdigest())
            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
