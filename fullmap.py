import os

def ask(string):
    answer = str(input(string))
    return answer

def enumerate(target):
    # TODO
    target = ask("What is your target?")
    print(f"Attacking {target}")




kali = str(input("do you use a kali linux? (y/N)"))
if(kali == "y" or kali == "Y"):
    e


tools = str(input("do you need to install tools? (y/N)"))
if(tools == 'y' or tools == 'Y'):
    cmd = 'sudo apt update'
    os.system(cmd)
    cmd = "sudo apt install nmap hydra gobuster john sqlmap"
    os.system(cmd)

wordlists = str(input("do you need to install wordlists?

