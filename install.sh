#!/bin/bash
#Author: Nathaniel Elderson

if (( EUID != 0 ));
then
	echo -e "\033[31m[!] \033[01m\033[04mThis script must be ran as root.\033[0m"
	exit
else
	clear
	echo -e "\033[32m[+] \033[01mInstalling Requirements...\033[0m"
	echo ""
	echo -e "    \033[01m\033[04m\033[93mPython3\033[0m"
	sleep 1
	if [ "$(which python3)" == "" ];
	then
		echo -e "\033[31m[!] \033[01mPython3 is not installed.\033[0m"
		echo -e "\033[32m[+] \033[01mInstalling Python3...\033[0m"
		echo -e "    \033[34mPlease be patient this may take a few minutes.\033[0m"
		apt-get update
		apt-get install -y python3

	else
		echo -e "\033[34m[+] \033[01mPython3 is already installed.\033[0m"
		echo ""
	fi
	echo -e "    \033[93m\033[04m\033[01mMetasploit-Framework\033[0m"
	sleep 1
	if [ "$(which msfconsole)" == "" ];
	then
		echo -e "\033[31m[!] \033[01mMetasploit-Framework is not installed.\033[0m"
		echo -e "\033[32m[+] \033[01mInstalling msfconsole...\033[0m"
		echo -e "    \033[34mPlease be patient this may take a few minutes.\033[0m"
		curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall
		echo ""
	else
		echo -e "\033[34m[+] \033[01mMetasploit-Framework is already installed.\033[0m"
		echo ""
	fi
	echo "randmac" >> requirements.txt
	echo "colorama" >> requirements.txt
	echo "zipfile"
	echo -e "\033[32m[+] \033[01mInstalling Python libraries...\033[0m"
	echo ""
	pip install -r requirements.txt > install.log
	echo ""
	sleep 2
	echo -e "\033[34m[+] Requirements installed. \033[32m\033[01mDONE!\033[0m"
	rm requirements.txt
	rm -rf install.log
	echo ""
	echo -e "\033[37m[+] Opening HellShell for the first time after installing the dependencies...\033[0m"
	sleep 2
	clear
	python3 HellShell.py
fi


