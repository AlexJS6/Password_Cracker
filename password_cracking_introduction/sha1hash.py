from urllib.request import urlopen
import hashlib
from termcolor import colored

sha1hash = input('[*] Enter sha1 Hash Value: ')

passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

for i in passlist.split('\n'):
    hashguess = hashlib.sha1(bytes(i, 'utf-8')).hexdigest()
    if sha1hash == hashguess:
        print(colored('[+] The password is: ' + str(i), 'green'))
        quit()
    else:
        print(colored('[-] Password guess: ' + str(i) + ' Does not match, trying next...', 'red'))

print('Password not in password list.')