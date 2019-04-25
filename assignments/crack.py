import hashlib
import string

def crack():
    hashes = open("hashes.txt", 'r').read().split('\n')
    passwords = open("password.txt", 'r')
    character = string.ascii_lowercase
    for p in passwords:
        for c in character:
            p = p.strip()
            hsh = hashlib.sha256(c.encode()+p.encode()).hexdigest()
            if hsh in hashes:
                print("pass: "+c+p)



if __name__ == '__main__':
    crack()

