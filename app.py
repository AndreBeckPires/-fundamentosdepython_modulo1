import manageusers

while manageusers.success != 1:
    manageusers.selectAction()

#loop principal

while manageusers.getAutenticado() == 1:
    print(f'Conectado como {manageusers.getUser()}. Digite 1 para fazer logout ou 2 para encerrar aplicação: ')
    action = input()
    if action == '1':
        manageusers.logout()
        manageusers.selectAction()
    if action == '2':
        exit()
    
    