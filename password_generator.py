#write a program to take the lenght of the password from the user and generate and print a password that contains charaters and basic 
#symbols & numbers. Next save that genrated password the that the password is being genrated to a txt file. and check if charaters, symbols and letters
#are in the passwor

import os 
import random
import string
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()


print('Enter 1 to create new password')
print('Enter 2 to recall password')
print('Enter 0 to exit the program')
options = int(input('Choose option: '))
my_passwords = dict()
key = os.getenv('KEY').encode('utf-8')
cyspher = Fernet(key)


while options != 0:
    if options == 1:
        variables = (string.ascii_letters + string.digits) + '!#$%&'
        password_lenght = int(input('How long do you want the password to be: '))
        site_input = input('What webiste are you genrating this password for? ')
        password_output = ''

        output_list = random.choices(variables,k=password_lenght)
        password_output = ''.join(output_list)

        def is_strong(password_output):
                alpha = any(char.isalpha() for char in password_output) 
                has_number = any(char.isdigit() for char in password_output)
                has_symbol = any(char in '!#$%&' for char in password_output)
                return alpha and has_number and has_symbol
        while True:
            output_list = random.choices(variables, k=password_lenght)
            password_output = ''.join(output_list)
            if is_strong(password_output):
                break
            
        encrypted_password = (cyspher.encrypt(password_output.encode('utf-8')))    


        with open('password.txt', 'a') as file:
            file.write(f'{site_input} : {encrypted_password} \n')
        print(f'Here is you random password generated {password_output}')
        print('Choose options 0-2.')
        options = int(input('Choose option: '))


    elif options == 2:
        #recall previously saved 
        with open('password.txt', 'r') as file:
            print(f'Here is a list of website you have saved')
            for line in file:
                password_array = (line.strip().split(' : ') )
                web_name = password_array[0]
                print(web_name)
                web_pass = password_array[1][2:-1]
                my_passwords[web_name.lower()] = web_pass
        pass_recall = input('What website? ').lower()
        try:
            decripted_password = (cyspher.decrypt(my_passwords[pass_recall].encode('utf-8')))
            print(decripted_password.decode())

            
        except:
            print('Error Occoured')
        print('Choose options 0-2.')
        options = int(input('Choose option: '))

    elif options == 0:
        print('Program escaped.')
        exit()

    else:
        print('Please input either 0 - 2')
        options = int(input('Choose option: '))

