#write a program to take the lenght of the password from the user and generate and print a password that contains charaters and basic 
#symbols & numbers. Next save that genrated password the that the password is being genrated to a txt file. and check if charaters, symbols and letters
#are in the passwor

from backend.password_service import create_pass, fetch

print('Enter 1 to create new password')
print('Enter 2 to recall password')
print('Enter 0 to exit the program')
options = int(input('Choose option: '))

while options != 0:
    if options == 1:
        password_lenght = int(input('How long do you want the password to be: '))
        site_input = input('What webiste are you genrating this password for? ')
        create_pass(password_lenght, site_input)
        print('Choose options 0-2.')
        options = int(input('Choose option: '))

    elif options == 2:
        pass_recall = input('What website? ').lower()
        fetched = fetch(pass_recall)
        print(fetched)
        print('Choose options 0-2.')
        options = int(input('Choose option: '))

    elif options == 0:
        print('Program escaped.')
        exit()

    else:
        print('Please input either 0 - 2')
        options = int(input('Choose option: '))


