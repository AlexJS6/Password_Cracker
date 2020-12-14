from termcolor import colored
import hashlib


def tryOpen(wordlist):
    global pass_file
    try:
        pass_file = open(wordlist, 'r')
    except:
        print("[!] No such File at that Path!")
        quit()


pass_hash = input('[*] Enter MD5 Hash Value: ')
wordlist = input("[*] Enter Path to the Password File: ")

tryOpen(wordlist)

for word in pass_file:
    print(colored("[-] Trying: " + word.strip("\n"), 'red'))
    enc_wrd = word.encode('utf-8')
    md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if md5digest == pass_hash:
        print(colored('Password found: ' + word, 'green'))
        exit(0)

print("[!] Password not in list!")