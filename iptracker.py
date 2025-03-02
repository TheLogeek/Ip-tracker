import requests
from pathlib import Path
import os, colorama, time, sys

colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.BLUE
lb = colorama.Fore.LIGHTBLUE_EX
lr = colorama.Fore.LIGHTRED_EX
RED = colorama.Fore.RED

def ip_tracker(ip_address):
	#info = requests.get(f"https://api.ip2location.io/?ip={ip_address}")
	info = requests.get(f"https://api.ip2location.io/?key=75A4D7D2B75B4DB7E97D3DFEE5B6060A&ip={ip_address}&format=json")

	data=info.json()
	return f"""IP Address: {data['ip']}
Country Code: {data['country_code']}
Country : {data['country_name']}
Region: {data['region_name']}
City: {data['city_name']}
Latitude: {data['latitude']}
Longitude: {data['longitude']}
Zip Code: {data['zip_code']}
Time Zone: {data['time_zone']}
Autonomous System Number(ASN): {data['asn']}
Organisation: {data['as']}
"""
def sd1(string):
     for c in string + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0 / 100)

def program_intro():
	os.system("clear")
	print(f"""
	
██╗██████╗░
██║██╔══██╗
██║██████╔╝
██║██╔═══╝░
██║██║░░░░░
╚═╝╚═╝░░░░░

████████╗██████╗░░█████╗░░█████╗░██╗░░██╗
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░
░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░
░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
	""")
	print(f"""{GREEN}
[+] Program name: IP Tracker
[+] Created by Solomon Adenuga
[+] Version: 1.0
[+] Github: https://github.com/SoloTech01
[+] Whatsapp: +2348023710562
""")
	print("xxxxxx" * 11)
	ip_address = input(f"{YELLOW}Enter IP Address:{RESET} ")
	print(f"\n{GREEN}Getting info.....{RESET}")
	information = ip_tracker(ip_address)
	print("\n")
	sd1(f"{GREEN}{information}{RESET}")
	try:
		path = Path("/storage/emulated/0/Ip Tracker")
		path.mkdir(exist_ok=True)
	except:
		pass

	try:
		with open("Ip Address info", "w") as file:
			file.write(information)
		print(f"{YELLOW}\n[✓] FILE SAVED SUCCESSFULLY!: {Path.cwd()}/Ip Address info{RESET}")
	except:
		pass
	res = input(f"{YELLOW}Do you want to continue (y/n){RESET}: ")
	if res.lower().strip() == "y":
		program_intro()
	elif res.lower().strip() == "n":
                print(RED)
                print("TERMINATING....")
                print(RESET)
                time.sleep(3)
                sys.exit()

program_intro()