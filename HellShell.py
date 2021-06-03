#!/usr/bin/python3
#Author: Nathaniel Elderson


import os
import time
import banners
import subprocess


def rootUserCheck():
	if os.geteuid() != 0:
		print("Not running as root...")
		time.sleep(0.5)
		print("\n" + banners.welcomeBanner, banners.credits)
		print("\nExiting the HellShell...")
		exit()
	elif os.geteuid() == 0:
		pass


def checkTools():
	tool1 = os.path.exists("/usr/bin/msfconsole")
	tool2 = os.path.exists("/usr/bin/msfvenom")
	if tool1 == False:
		if tool2 == True:
			print("metasploit-framework is not installed or not in path.")
			return False
	if tool1 == False and tool2 == False:
		print("metasploit-framework is not installed or not in path.")
		print("msfvenom is not installed or not in path.")
		return False
	return True


def main():
	print(banners.credits, banners.welcomeBanner, banners.cowsayHelp)
	time.sleep(1)
	while True:
		cmnd = input("""\033[31m┌─[\033[01mroot\033[93m@\033[0m\033[96mHellShell\033[0m\033[31m]-[\033[32m/\033[31m]\n└──╼ \033[93m#\033[0m\033[37m""").strip()
		if cmnd == "":
			continue
		if cmnd == "q" or cmnd == "0" or cmnd == "exit" or cmnd == "quit":
			print("\nThank You for using the HellShell.\nBye.\n")
			exit()
		if cmnd == "clear":
			os.system("clear")
		elif "$" in cmnd:
			bashCmnd = cmnd.strip("$")
			os.system(bashCmnd)
		elif cmnd == "help":
			print(banners.menu)
		elif cmnd == "banner":
			print(banners.shuffle())
		elif cmnd == "1" or cmnd == "droid":
			try:
				subprocess.call("python3 Scripts/AutomatedAndroidStuff.py", shell=True)
			except KeyboardInterrupt:
				pass
			except EOFError:
				pass
		elif cmnd == "2" or cmnd == "mac":
			try:
				subprocess.call("python3 Scripts/MACspoofer.py", shell=True)
			except KeyboardInterrupt:
				pass
			except EOFError:
				pass
		elif cmnd == "3" or cmnd == "phish":
			print("It ain't workin' right now. Workin' on it.")
		elif cmnd == "4" or cmnd == "brutemail":
			try:
 				subprocess.call("python3 Scripts/mail.py", shell=True)
			except KeyboardInterrupt:
				pass
			except EOFError:
				pass
		elif cmnd == "5" or cmnd == "brutezip":
			try:
				subprocess.call("python2 Scripts/ZIPBrute.py", shell=True)
			except KeyboardInterrupt:
				pass
			except EOFError:
				pass
		else:
			print(f"{cmnd}:command not found")


rootUserCheck()
subprocess.call("rm -rf __pycache__", shell=True)
check = checkTools()
if check == False:
	print("Requirements not satisfied...")
	exit()
else:
	try:
		main()
	except KeyboardInterrupt:
		print("\nThank You for using the HellShell.\nBye.\n")
	except EOFError:
		print("\nThank You for using the HellShell.\nBye.\n")


