# Perguntar ao usuario se ele quer criar um senha ou não
#Se sim, gerar uma senha
#Gerar senha
#Imprimir a senha no terminal
#Se a resposta no começo for 'não', sair do programa

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&*()_+=")

def createPassword():
    lengthPassword = int(input('How long would you like your password to be? '))
    
    random.shuffle(characters)

    password = []

    for i in range(lengthPassword):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)
    print(password)

option = input('Do you want to generate a password? ').upper()

if option == "YES" or option == 'Y':
    createPassword()
elif option == "NO" or option == 'N':
    print('Okay, Bye! :)')
    quit()
else:
    print('Invalid option, please run the script again and write Yes or No this time.')
    quit()