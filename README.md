<p align=center>
<u>Welcome reverse-PYSHELL</u>
</p>

<video src="./assests/reverse-pySHELL.mp4" width="720" height="500" controls></video>


## This reverse-PYSHELL is a Python shell. I produced two files. 1.) File of the attacker 2.) Victim file: The target machine uses the victim file, while the Kali machine uses the attacker file. Configure your IP address, open both file sets containing the attackers' IP addresses, and change the default port (8080) before proceeding with this method. Once the victim file is shared with the target computer, you can begin working.

# Folder Tree


reverse-pySHELL/ <br>
├── LICENSE      <br>
├── README.md    <br>
├── assests      <br>
│   └── reverse-pySHELL.mp4 <br>
├── attacker.py <br>
└── victim.py <br>

# Testing
* Kali Linux
* Windows 11

# Installtions
```
# Clone repo
> git clone https://github.com/theNareshofficial/reverse-pySHELL.git

# Change Directory
> cd reverse-pySHELL

#open both file and set attacker IP address in Line 31
>nano attacker.py

# Execute the program
> python attacker.py

# After get shell 
SHELL> pwd
SHELL> ls

#if you want to Exit
SHELL> terminate
```