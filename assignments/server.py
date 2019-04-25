import hashlib
import string
import socket
import time

def serve(s, data, passwords, character):
    for p in passwords:
        for c in character:
            p = p.strip()
            hsh = hashlib.sha256(c.encode() + p.encode()).hexdigest()
            val = data.decode().split()
            x = len(val)
            if hsh == val[x - 2]:
                s.send(c.encode() + p.encode() + "\n".encode())
                print(s.recv(1024).decode())
                return
def server_crack():
    server_ip = '134.209.128.58'
    server_port = 1337
    passwords = open("password.txt", 'r')
    character = string.ascii_lowercase
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    i = 0
    while i < 3:
        data = s.recv(1024)
        serve(s, data, passwords, character)
        time.sleep(2)
        i += 1


if __name__ == "__main__":
    server_crack()