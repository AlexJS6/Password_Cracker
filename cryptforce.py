import crypt # decript with salt
from termcolor import colored as c

def crackPass(cryptWord):
    salt = cryptWord[:2]
    dictionary = open("dictionary.txt", 'r')
    for word in dictionary.readlines():
        word = word.strip('\n')
        cryptPass = crypt.crypt(word, salt)
        if cryptWord == cryptPass:
            print(c("[+] Found password: " + word, 'green'))
            return True

def main():
    passFile = open('password.txt', 'r')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptWord = line.split(':')[1].strip(' ').strip('\n')
            print(c("[*] Cracking Password For: " + user, 'blue'))
            crackPass(cryptWord)
            if crackPass(cryptWord):
                quit()
            else:
                print(c('[-]Password not found!', 'red'))
    
main()