import string

import os

import random

from choices import Option

instruction = """
                 ---------------------------------
                 |                               |
                 | Password generator / Stash    |
                 |                               |
                 ---------------------------------

        Menu:
            [1] - Generate password 
            [2] - List of passwords
            [0] - Exit program
"""

passcom = """
                [1] - Uppercase     [2] - Lowercase
                [3] - Digits        [4] - Punctuation

        Choices :

          [a] - 1     [b] - 2     [c] - 3     [d] - 4     [e] - 1,2
          [f] - 1,3   [g] - 1,4   [h] - 2,3   [i] - 2,4   [j] - 3,4
          [k] - 1,2,3 [l] - 2,3,4 [m] - 1,3,4 [n] - 4,2,1 [o] - 1,2,3,4
"""

class PasswordGenerator(Option):
    def __init__(self, password_size, note,):
        self.password_size = password_size
        self.note = note

    def list(self):
        with open("password.txt", "r") as output:
            lists = output.read()
            print (lists)
            output.close()

    def save(self, password, note):
        with open("password.txt", "a+") as output:
            output.write("Password: " + password + "\nNote:" + note +"\n\n")
            output.read()
            output.close()

    def random_string_generator(self):
        size = int(password_size)

        chars = {
            "a" : self.uppercase,
            "b" : self.lowercase,
            "c" : self.digits,
            "d" : self.punctuation,
            "e" : self.comb1,
            "f" : self.comb2,
            "g" : self.comb3,
            "h" : self.comb4,
            "i" : self.comb5,
            "j" : self.comb6,
            "k" : self.comb7,
            "l" : self.comb8,
            "m" : self.comb9,
            "n" : self.comb10,
            "o" : self.comb11,
        }

        password = ''.join(random.choice(chars[num]()) for i in range(size))
        print("This is your password : {}".format(password))
        self.save(password, note)

if __name__ == "__main__":
    password_size = 1
    note = ""
    pwd = PasswordGenerator(password_size, note)
    menu = ""
    print(instruction)
    while menu != "0":
        menu = input("Select: ")
        if menu == "1":
            print(passcom)
            try:
                num = input("Select password combination:")
                password_size = input("Password size: ")
                while password_size == "0":
                    print("error")
                    password_size = input("Password size: ")
                note = input("Note: ")
                pwd.random_string_generator()
            except ValueError:
                print("Ti ma ano ka!? ka sayup sa imong gi butang.")
            print(instruction)
        elif menu == "2":
            os.system('clear')
            pwd.list()
            print(instruction)
            
    print("Bye")
    os.system('clear')