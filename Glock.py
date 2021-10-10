from colorama import *
import instaloader
import os
import time
textglock = "GlockInstaDownloader"
def clear():
  os.system('clear')

clear()
banner = f"""
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O {Fore.RED + textglock + Fore.BLUE}
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /' 
    / XXXXXX /  `\    /' 
   / XXXXXX /`-------'
  / XXXXXX /                 
 / XXXXXX /
(________(                
 `------'    """

redbanner = f"""
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O {Fore.BLUE + textglock + Fore.RED}
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /' 
    / XXXXXX /  `\    /' 
   / XXXXXX /`-------'
  / XXXXXX /                 
 / XXXXXX /
(________(                
 `------'    """

moi = """
ses moi Toumai qui l'as créer trou de balle.
"""


def redmenu():
    print(Fore.RED+redbanner+Fore.RESET)
    print()
    intputt = input(Fore.RED+"Glock"+Fore.RESET+" > ")

    if intputt == "change colors, blue":
          try:
            clear()
            menu()
          except:
            return redmenu

    elif intputt == "qui à crée sa ?":        
          print(moi)
          time.sleep(5)
          clear()
          redmenu()

      
    try:
      print()
      print(Fore.RED+'[+]'+Fore.RESET+" Starting")
      print('')
      ig = instaloader.Instaloader()
      ig.download_profile(intputt, profile_pic_only=False)
      print(Fore.RED+'[+]'+Fore.RESET+" Finish")
      time.sleep(5)
    except:
      print(Fore.BLUE+'[/]'+Fore.RESET+f" Glock Can't download picture from {intputt}")
      clear()
      menu()
      
      

def menu():
      
    print(Fore.BLUE+banner+Fore.RESET)
    print()
    intputt = input(Fore.BLUE+"Glock"+Fore.RESET+" > ")

    if intputt == "change colors, red":
          try:
            clear()
            redmenu()
          except:
            return menu

    elif intputt == "qui à crée sa ?":
          print(moi)
          time.sleep(5)
          clear()
          menu()


    try:
      print()
      print(Fore.BLUE+'[+]'+Fore.RESET+" Starting")
      print('')
      ig = instaloader.Instaloader()
      ig.download_profile(intputt, profile_pic_only=False)
      print(Fore.BLUE+'[+]'+Fore.RESET+" Finish")
      time.sleep(5)
    except:
      print(Fore.RED+'[/]'+Fore.RESET+f" Glock Can't download picture from {intputt}")
      clear()
      menu()
      
menu()
