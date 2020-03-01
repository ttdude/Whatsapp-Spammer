import selenium
from selenium import webdriver
import sys
import time

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

def banner():
    print(bcolors.GREEN + '''
__      ___  _     ___    _____    ___     ___      ___     ___            ___      ___    ___   __  __  
\ \    / / || |   /   \  |_   _|  / __|   /   \    | _ \   | _ \   ___    / __|    | _ \  /   \ |  \/  | 
 \ \/\/ /| __ |   | - |    | |    \__ \   | - |    |  _/   |  _/  |___|   \__ \    |  _/  | - | | |\/| | 
  \_/\_/ |_||_|   |_|_|   _|_|_   |___/   |_|_|   _|_|_   _|_|_   _____   |___/   _|_|_   |_|_| |_|__|_| 
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_| """ |_| """ |_|     |_|"""""|_| """ |_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
   by tt_dude    

''')

class bomber:
    def __init__(self):
        super().__init__()
        self.message = input(bcolors.YELLOW + '[~] Enter Message |> ')
        try:
            self.amount = int(input(bcolors.YELLOW + '[~] Enter amount of Messages |> '))
        except Exception as e:
            print(bcolors.RED + f'[-] Error {e}, Goodbye')
            sys.exit(1)
        self.bot = webdriver.Firefox()
    def connect(self):
        print(bcolors.YELLOW + '-_-_- Starting Browser -_-_-')
        try:
            self.bot.get('https://web.whatsapp.com/')
            print(bcolors.GREEN + '[+] Browser Started\n')
        except KeyboardInterrupt:
            print('Goodbye')
            sys.exit(1)
        except Exception as e:
            print(bcolors.RED + f'[-] Error {e}, Goodbye')
            sys.exit(1)
        temp = input(bcolors.YELLOW + '[~] Scan the QR code in Whatsapp and select a contact, press ENTER to continue |> ')
    def send(self):
        print(bcolors.GREEN + '[+] Flooding')
        starttime = time.time()
        try:
            for i in range(self.amount):
                self.bot.find_element_by_class_name('_3u328').send_keys(self.message)
                self.bot.find_element_by_class_name('_3M-N-').click()
        except KeyboardInterrupt:
            print('Goodbye')
            sys.exit(1)
        except Exception as e:
            print(bcolors.RED + f'[-] Error {e}, Goodbye')
            sys.exit(1)
        print(bcolors.YELLOW + f'Finished in {time.time() - starttime}')
if __name__ == "__main__":
    banner()
    bomber = bomber()
    bomber.connect()
    bomber.send()
