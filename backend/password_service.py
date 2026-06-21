import os 
import random
import string
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('KEY').encode('utf-8')
cyspher = Fernet(key)


def create_pass(pass_len, site_input):
    
    variables = (string.ascii_letters + string.digits) + '!#$%&'
    password_output = ''

    def is_strong(password_output):
            alpha = any(char.isalpha() for char in password_output) 
            has_number = any(char.isdigit() for char in password_output)
            has_symbol = any(char in '!#$%&' for char in password_output)
            return alpha and has_number and has_symbol
    while True:
        output_list = random.choices(variables, k=pass_len)
        password_output = ''.join(output_list)
        if is_strong(password_output):
            break
        
    encrypted_password = (cyspher.encrypt(password_output.encode('utf-8')))    


    with open('password.txt', 'a') as file:
        file.write(f'{site_input} : {encrypted_password} \n')
    print(f'Here is you random password generated {password_output}')
    return password_output


def fetch(pass_recall):
    with open('password.txt', 'r') as file:
        for line in file:
            password_array = (line.strip().split(' : ') )
            web_name = password_array[0]
            if web_name == pass_recall:
                web_pass = password_array[1][2:-1]
                try:
                    decripted_password = (cyspher.decrypt(web_pass.encode('utf-8')))
                    return decripted_password.decode()
                except:
                    return 'Error Occoured'
    return 'Password not found.'
    


def fetch_all():
    websites=[]
    with open('password.txt', 'r') as file:
        for line in file:
            password_array = (line.strip().split(' : ') )
            websites.append(password_array[0])
    return websites