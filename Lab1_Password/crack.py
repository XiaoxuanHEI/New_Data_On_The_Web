# Written with <3 by Julien Romero

import hashlib
from sys import argv
import sys
import random
import itertools
import string
if (sys.version_info > (3, 0)):
    from urllib.request import urlopen
    from urllib.parse import urlencode
else:
    from urllib2 import urlopen
    from urllib import urlencode


class Crack:
    """Crack The general method used to crack the passwords"""

    def __init__(self, filename, name):
        """__init__
        Initialize the cracking session
        :param filename: The file with the encrypted passwords
        :param name: Your name
        :return: Nothing
        """
        self.name = name.lower()
        self.passwords = get_passwords(filename)

    def check_password(self, password):
        """check_password
        Checks if the password is correct
        !! This method should not be modified !!
        :param password: A string representing the password
        :return: Whether the password is correct or not
        """
        password = str(password)
        cond = False
        if (sys.version_info > (3, 0)):
            cond = hashlib.md5(bytes(password, "utf-8")).hexdigest() in \
                self.passwords
        else:
            cond = hashlib.md5(bytearray(password)).hexdigest() in \
                self.passwords
        if cond:
            

            '''args = {"name": self.name,
                    "password": password}
            args = urlencode(args, "utf-8")
            page = urlopen('http://137.194.211.71:5000/' +
                                          'submit?' + args)
            if b'True' in page.read():''' 
            
            print("You found the password: " + password)
            return True
        return False
        
    def evaluate(self):
        """evaluate
        Retrieve the grade from the server,
        !! This method MUST not be modified !!
        """
        args = {"name": self.name }
        args = urlencode(args, "utf-8")
        page = urlopen('http://137.194.211.71:5000/' +
                                          'evaluate?' + args)
        print("Grade :=>> " + page.read().decode('ascii').strip())

    def crack(self):
        """crack
        Cracks the passwords. YOUR CODE GOES BELOW.
        
        We suggest you use one function per question. Once a password is found,
        it is memorized by the server, thus you can comment the call to the
        corresponding function once you find all the corresponding passwords.
        """
#        self.bruteforce_digits()
#        self.bruteforce_letters()
        
        self.dictionary_passwords()
        self.dictionary_passwords_leet()
        self.dictionary_words_hyphen()
        self.dictionary_words_digits()
        self.dictionary_words_diacritics()
        self.dictionary_city_diceware()

        # self.social_google()
        # self.social_jdoe()
    
    def bruteforce_digits(self):
        for n in range(9999999999):
            self.check_password(n)
#        for i in range(1,9):
#            for j in itertools.product(list(string.digits), repeat = i):
#                self.check_password(j)
        
    
    def bruteforce_letters(self):
        n = ""
        for i in range(5):
            if i == 0:
                for a in range(65,123):
                    n = chr(a)
                    self.check_password(n)
            if i == 1:
                for a in range(65,123):
                    for b in range(65,123):
                        n = chr(a)+chr(b)
                        self.check_password(n)
            if i == 2:
                for a in range(65,123):
                    for b in range(65,123):
                        for c in range(65,123):
                            n = chr(a)+chr(b)+chr(c)
                            self.check_password(n)
            if i == 3:
                for a in range(65,123):
                    for b in range(65,123):
                        for c in range(65,123):
                            for d in range(65,123):
                                n = chr(a)+chr(b)+chr(c)+chr(d)
                                self.check_password(n)
            if i == 4:
                for a in range(65,123):
                    for b in range(65,123):
                        for c in range(65,123):
                            for d in range(65,123):
                                for e in range(65,123):
                                    n = chr(a)+chr(b)+chr(c)+chr(d)+chr(e)
                                    self.check_password(n)
    
    def dictionary_passwords(self):
        with open ("10k-most-common.txt") as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            for n in content:
                print(n)
                self.check_password(n)
    
    def dictionary_passwords_leet(self):
        with open ("10k-most-common.txt") as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            for n in content:
                n = n.replace('e','3')
                n = n.replace('l','1')
                n = n.replace('a','0')
                n = n.replace('i','1')
                n = n.replace('o','0')
                self.check_password(n)
                        

    def dictionary_words_hyphen(self):
        with open ("20k.txt") as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            for n in content:
                num = random.randint(1,3)
                for i in range(1, num+1):
                    p = random.randint(0,len(n))
                    n = n[0:p] + "-" + n[p:]
                    self.check_password(n)
    
    def dictionary_words_digits(self):
        with open ("20k.txt") as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            for n in content:
                if len(n) > 5:      
                    for a in range(10):
                        for b in range(10):
                            wd = n + str(a) + str(b)
                            self.check_password(wd)

    def dictionary_words_diacritics(self):
        with open ("10kfrench.txt") as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            for n in content:
                n = n.replace('é','e')
                n = n.replace('è','e')
                n = n.replace('ê','e')
                n = n.replace('à','a')
                n = n.replace('ç','c')
                n = n.replace('ï','i')
                n = n.replace('ô','o')
                self.check_password(n)
    
    def dictionary_city_diceware(self):
        with open ("africa_capitals.txt") as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            num = random.randint(1,4)
            wd = ""
            l = []
            for n in content:
                l.append(n.lower())
           # print(l)
            for i in range(0,10000):
                for i in range(0,num):               
                    a = random.randint(0,5)
                    b = random.randint(0,5)
                    c = random.randint(0,5)
                    index = a*6*6 + b*6 + c*1
                    if index < len(n):
                        wd = wd + l[index]
                #if wd != "":
                    #print(wd)
                self.check_password(wd)
                wd = "" 
    
    # def social_google(self):
    #     pass
    
    # def social_jdoe(self):
    #     pass


def get_passwords(filename):
    """get_passwords
    Get the passwords from a file
    :param filename: The name of the file which stores the passwords
    :return: The set of passwords
    """
    passwords = set()
    with open(filename, "r") as f:
        for line in f:
            passwords.add(line.strip())
    return passwords


if __name__ == "__main__":
    name = "hei".lower()
    # This is the correct location on the moodle
    #encfile = "../passwords2019/" + name + ".enc"
    
    # If you run the script on your computer: uncomment and fill the following 
    # line. Do not forget to comment this line again when you submit your code
    # on the moodle.
    encfile = "hei.enc"
    
    # First argument is the password file, the second your name
    crack = Crack(encfile, name)
    if "--eval" in sys.argv: crack.evaluate()
    else: crack.crack()