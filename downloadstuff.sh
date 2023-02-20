if [ $EUID -ne 0 ]; then
   echo "This script must be executed with sudo"
   exit 1
else
   echo "i hope you are sudo, otherwise stuff wont work"
fi

# rest of the script if executed as sudo
# Prompt the user with a yes/no question
read -p "Requirements for this script are gunzip, wget and apt, do you have all of those programms? (y/n) " response

# Check if the response is "y" or "Y" (yes)
if [[ "$response" =~ ^[Yy]$ ]]; then
   # Perform the action
   # Add your code here
else
   # Do not perform the action
   echo "Install those first"
   exit 1
fi

read -p "Do you want to download tools? (y/n) " response

# Check if the response is "y" or "Y" (yes)
if [[ "$response" =~ ^[Yy]$ ]]; then
   # Perform the action
   echo "Performing the action..."
   apt update
   apt install nmap hydra sqlmap gobuster john
   # Add your code here
else
   # Do not perform the action
   echo "Action cancelled."
fi
read -p "Do you want to download wordlists? (y/n) " response

# Check if the response is "y" or "Y" (yes)
if [[ "$response" =~ ^[Yy]$ ]]; then
   # Perform the action
   echo "Performing the action..."
   wget https://github.com/danielmiessler/SecLists/raw/master/Discovery/DNS/bitquark-subdomains-top100000.txt > Subdomains.txt
   wget https://github.com/praetorian-inc/Hob0Rules/raw/master/wordlists/rockyou.txt.gz
   gunzip rockyou.txt.gz
   wget https://raw.githubusercontent.com/v0re/dirb/master/wordlists/big.txt
   # Add your code here
else
   # Do not perform the action
   echo "Action cancelled."
fi
read -p "Do you want to download enumerationscripts? (y/n) " response

# Check if the response is "y" or "Y" (yes)
if [[ "$response" =~ ^[Yy]$ ]]; then
   # Perform the action
   echo "Performing the action..."
   # Add your code here
   wget https://github.com/carlospolop/PEASS-ng/releases/download/20220911/linpeas.sh
   wget https://github.com/carlospolop/PEASS-ng/releases/download/20220821/winPEASx64.exe
   wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh > ./linenum.sh
else
   # Do not perform the action
   echo "Action cancelled."
fi
