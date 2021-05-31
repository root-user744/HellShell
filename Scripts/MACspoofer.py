#!/usr/bin/python3
#Author: Nathaniel Elderson


import os, time, random, subprocess
from colorama import Fore
from randmac import RandMac


def rootCheck():
	if os.getuid() != 0:
		return False
	return True


def randMac():
	randomMAC = RandMac()
	return randomMAC


def spoofMAC(interface, mac):
	print(Fore.BLUE + f"[+] \033[01mChanging MAC address of {interface} to {mac}\033[0m")
	time.sleep(1)
	try:
		command = subprocess.check_output(f"ifconfig {interface} down", shell=True)
	except Exception:
		print(Fore.RED + "[+] \033[01mERROR!\033[0m\n")
		exit()
	else:
		subprocess.call(f"ifconfig {interface} hw ether {mac}", shell=True)
		subprocess.call(f"ifconfig {interface} up", shell=True)
		print(Fore.GREEN + "[+] \033[01mDONE!\033[0m\n")


if rootCheck() == False:
	print(Fore.RED + "[✗] \033[01mRun as root.\033[0m")
	exit()
else:
	pass


interface = input(Fore.YELLOW + "\n[+] \033[01mEnter the interface's name: \033[0m")
if interface == "":
	print(Fore.RED + "[✗] \033[01mNo input\033[0m\n")
	exit()
else:
	pass


macType = input(Fore.MAGENTA + "[+] \033[01mWant a custom MAC or random MAC(c/R): \033[0m")
if macType == "r" or macType == "R":
	spoofMAC(interface, randMac())
elif macType == "c" or macType == "C":
	customMac = input(Fore.CYAN + "[+] \033[01mEnter the custom MAC address: \033[0m")
	if customMac == "":
		print(Fore.RED + "[✗] \033[01mNo input\033[0m\n")
		exit()
	else:
		spoofMAC(interface, customMac)
else:
	print(Fore.RED + "[✗] \033[01mNot a valid option.\033[0m\033[0m\n")

