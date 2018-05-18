import string

import random

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
        Choices :
                [1] - Uppercase     [2] - Lowercase
                [3] - Digits        [4] - Punctuation

          [a] - 1     [b] - 2     [c] - 3     [d] - 4     [e] - 1,2
          [f] - 1,3   [g] - 1,4   [h] - 2,3   [i] - 2,4   [j] - 3,4
          [k] - 1,2,3 [l] - 2,3,4 [m] - 1,3,4 [n] - 4,2,1 [o] - 1,2,3,4
"""

class PasswordGenerator(object):
    def __init__(self, password_size, note, choice_input):
        self.password_size = password_size
        self.note = note
        self.choice_input = choice_input

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

        a = string.ascii_uppercase
        b = string.ascii_lowercase
        c = string.digits
        d = string.punctuation

        if choice_input == 'a':
            chars = a
            print("Uppercase")
        elif choice_input == 'b':
            chars = b
            print("Lowercase")
        elif choice_input == 'c':
            chars = c
            print("Digits")
        elif choice_input == 'd':
            chars = d
            print("Punctuation")
        elif choice_input == 'e':
            chars = a + b
            print("Uppercase and Lowercase")
        elif choice_input == 'f':
            chars = a + c
            print("Uppercase and Digits")
        elif choice_input == 'g':
            chars = a + d
            print("Uppercase and Punctuation")
        elif choice_input == 'h':
            chars = b + c
            print("Lowercase and Digits")
        elif choice_input == 'i':
            chars = b + d
            print("Lowercase and Punctuation")
        elif choice_input == 'j':
            chars = c + d
            print("Digits, Punctuation")
        elif choice_input == 'k':
            chars = a + b + c
            print("Uppercase, Lowercase, and Digits")
        elif choice_input == 'l':
            chars = b + c + d
            print("Lowercase, Digits, and Punctuation")
        elif choice_input == 'm':
            chars = a + c + d
            print("Uppercase, Digits, and Punctuation")
        elif choice_input == 'n':
            chars = a + b + d
            print("Uppercase, Lowercase, and Punctuation")
        elif choice_input == 'o':
            chars = a + b + c + d
            print("Uppercase, Lowercase, Digits, and Punctuation")
        else:
            print("Invalid input")

        password = ''.join(random.choice(chars) for i in range(size))
        print("This is your password : {}".format(password))
        
        self.save(password, note)

if __name__ == "__main__":

    password_size = 1
    note = ""
    choice_input = ""

    password = PasswordGenerator(password_size, note, choice_input)

    a = "0"

    print(instruction)

    while a == "0":
        menu = input("Select: ")

        if menu == "1":
            print(passcom)
            try:
                choice_input = input("Select password combination: ")
                password_size = input("Password size: ")
                while password_size == "0":
                    print("error")
                    password_size = input("Password size: ")
                note = input("Note: ")
                password.random_string_generator()
            except ValueError:
                print("Ti ma ano ka!? ka sayup sa imong gi butang.")
            print(instruction)
        elif menu == "2":
            password.list()
            print(instruction)
        elif menu == "0":
            break
            print("Bye")