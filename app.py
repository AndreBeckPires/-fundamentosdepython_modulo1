import json

#variaveis
userInput = ''
passwordInput = ''
autenticado = 0

with open('credentials.json', 'r', encoding='utf-8') as arquivo:
    users = json.load(arquivo)  # salva o json em uma variavel

def getUserInput():
    global userInput
    global passwordInput
    userInput = input("User:") 
    passwordInput = input("Password:")

def autenticate(userInput, passwordInput):
    for user in users:
        if user['user'] == userInput:
            if user['password'] == passwordInput:
                print("Conectado")
                return 1
            else:
                print("Senha incorreta")
                return 0
    print("Usuario nao encontrado")
    return 0


while autenticado == 0:
    getUserInput()
    autenticado = autenticate(userInput,passwordInput)
