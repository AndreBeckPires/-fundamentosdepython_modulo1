import json

#variables
userInput = ''
passwordInput = ''
autenticado = 0
success = 0
with open('credentials.json', 'r', encoding='utf-8') as arquivo:
    users = json.load(arquivo)  # loads json file into a variable


def login():
    getUserInput()
    autenticado = autenticate(userInput,passwordInput)
    if autenticado == 0:
        login()

def createUser():
    print("criar usuario")
    new_user = input('Nome de usuario: ')
    new_password = input('Senha: ')
    for user in users:
        if user['user'] == new_user:
            print("Usuario já existe")
            return 0
        else:
            credentials = {"user": new_user, "password": new_password}
            users.append(credentials)
            with open('credentials.json', 'w', encoding='utf-8') as arquivo:
                json.dump(users, arquivo, indent =4)
            print(f'Usuário {new_user} criado com sucesso')
            break 

def getUserInput():
    global userInput
    global passwordInput
    userInput = input("User:") 
    passwordInput = input("Password:")

def autenticate(userInput, passwordInput):
    for user in users:
        if user['user'] == userInput:
            if user['password'] == passwordInput:
                global success
                success = 1
                return 1
            else:
                print("Senha incorreta")
                return 0
    print("Usuario nao encontrado")
    return 0

def selectAction():
    global success
    print("Digite 1 para fazer login ou 0 para criar um novo usuario:")
    action = input()
    if action == '1':
        login()
    if action == '0':
        createUser()
    if success == 1:
        print("Conectado")
    else:
        selectAction()




selectAction()


