import hashlib
import time
import sys
import os
import random
from tqdm import tqdm

# Neon RGB Colors
G = '\033[92m'; R = '\033[91m'; Y = '\033[93m'; B = '\033[94m'
C = '\033[96m'; P = '\033[95m'; W = '\033[97m'; RESET = '\033[0m'
RAINBOW = [G, R, Y, B, C, P]

def god_banner():
    os.system('clear')
    c = random.choice(RAINBOW)
    # আপনার নতুন ব্যানার "TAMIM-313"
    banner = f"""{c}
    ████████╗ █████╗ ███╗   ███╗██╗███╗   ███╗      ██████╗  ██╗██████╗ 
    ╚══██╔══╝██╔══██╗████╗ ████║██║████╗ ████║      ╚════██╗███║╚════██╗
       ██║   ███████║██╔████╔██║██║██╔████╔██║  ███╗ █████╔╝╚██║ █████╔╝
       ██║   ██╔══██║██║╚██╔╝██║██║██║╚██╔╝██║  ╚══╝ ╚═══██╗ ██║ ╚═══██╗
       ██║   ██║  ██║██║ ╚═╝ ██║██║██║ ╚═╝ ██║      ██████╔╝ ██║██████╔╝
       ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝     ╚═╝      ╚═════╝  ╚═╝╚═════╝ 
    {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {Y}       [+] 3 CR+ WORDLIST COMPATIBLE | TAMIM-313 EDITION [+]
    {C}       [+] SUPPORT: MD5, SHA1, SHA256, SHA512, ETC.
    {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}"""
    print(banner)

def start_god_crack():
    god_banner()
    t_hash = input(f"{G}[+] Target Hash: {W}").strip()
    w_file = input(f"{G}[+] Wordlist (rockyou.txt/wordlist_3cr): {W}").strip()
    
    print(f"\n{Y}[!] Select Algorithm Level:{RESET}")
    print(f"1. MD5  2. SHA1  3. SHA256  4. SHA512")
    ch = input(f"{G}[+] Choice: {W}")
    
    algos = {'1':'md5', '2':'sha1', '3':'sha256', '4':'sha512'}
    mode = algos.get(ch, 'md5')

    if not os.path.exists(w_file):
        print(f"{R}[!] File Not Found! Check filename.{RESET}")
        return

    print(f"{C}[*] Analyzing Wordlist Passwords...{RESET}")
    print(f"\n{R}[!!!] TAMIM-313 ATTACK INITIATED [!!!]{RESET}\n")
    time.sleep(1.5)

    try:
        # buffering ব্যবহার করা হয়েছে যাতে বড় ফাইল দ্রুত প্রসেস হয়
        with open(w_file, 'r', encoding='utf-8', errors='ignore', buffering=100000) as f:
            for password in tqdm(f, unit=" p/s", desc=f"{P}CRACKING{RESET}", colour="magenta"):
                password = password.strip()
                hashed = hashlib.new(mode, password.encode()).hexdigest()

                if hashed == t_hash:
                    print(f"\n{G}╔════════════════════════════════════════╗")
                    print(f"║  {W}PASSWORD FOUND: {Y}{password}")
                    print(f"{G}╚════════════════════════════════════════╝{RESET}")
                    return
            print(f"\n{R}[-] Exhausted wordlist. No match found.{RESET}")
    except KeyboardInterrupt:
        print(f"\n{R}[!] Attack Terminated by User.{RESET}")

if __name__ == "__main__":
    start_god_crack()
