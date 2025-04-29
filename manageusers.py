import json
import csv
#variables
user_input = ''
password_input = ''
autenticado = 0
success = 0
lista_de_usuarios = []
currentUser = ''
#with open('credentials.json', 'r', encoding='utf-8') as arquivo:
    #users = json.load(arquivo)  # loads json file into a variable

def login():
    get_user_input()
    autenticado = autenticate(user_input,password_input)
    if autenticado == 0:
        select_action()

def create_user():
    with open('credentials.json', 'r', encoding='utf-8') as arquivo:
        users = json.load(arquivo)  # loads json file into a variable
    print("criar usuario")

    new_user = input('Nome de usuario: ')
    new_password = input('Senha: ')
    global lista_de_usuarios
    lista_de_usuarios = []
    if users:
        for user in users:
            lista_de_usuarios.append(user['user'])
            if user['user'] == new_user:

                print("Usuario já existe")
                return 0
            
        credentials = {"user": new_user, "password": new_password}
        users.append(credentials)
        lista_de_usuarios.append(new_user)

        with open('credentials.json', 'w', encoding='utf-8') as arquivo:
            json.dump(users, arquivo, indent =4)
            print(f'Usuário {new_user} criado com sucesso')
        with open('tabela.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(lista_de_usuarios)
        with open(f'{new_user}.csv', 'w', newline='') as csvfile2:
            print("Criando")
            csvwriter = csv.writer(csvfile2)
            csvwriter.writerow(['Saldo:', 0])
        

            

    else:
        credentials = {"user": new_user, "password": new_password}
        users.append(credentials)
        with open('credentials.json', 'w', encoding='utf-8') as arquivo:
            json.dump(users, arquivo, indent =4)
        print(f'Usuário {new_user} criado com sucesso')
        with open('tabela.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([new_user])
        with open(f'{new_user}.csv', 'w', newline='') as csvfile2:
            print("Criando")
            csvwriter = csv.writer(csvfile2)
            csvwriter.writerow(['Saldo:', 0])
        

def get_user_input():
    global user_input
    global password_input
    user_input = input("User:") 
    password_input = input("Password:")

def autenticate(userInput, passwordInput):
    with open('credentials.json', 'r', encoding='utf-8') as arquivo:
        users = json.load(arquivo)  # loads json file into a variable
    for user in users:
        if user['user'] == userInput:
            if user['password'] == passwordInput:
                global currentUser
                currentUser = user['user']
                global success
                success = 1
                return 1
            else:
                print("Senha incorreta")
                return 0
    print("Usuario nao encontrado")
    return 0

def select_action():
    global success
    print("Digite:\n1 para fazer login \n0 para criar um novo usuario\n2 para encerrar aplicação")
    action = input()
    if action == '1':
        login()
    if action == '0':
        create_user()
    if action == '2':
        exit()
    if success == 1:
        print("Conectado")

    else:
        select_action()

def get_autenticado():
    return success


def logout():
    global success
    success = 0
    return success

def get_user():
    return currentUser





