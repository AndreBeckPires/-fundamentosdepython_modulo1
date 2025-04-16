import csv
def atSaldo(file, data):
    with open(file, 'r', newline='') as csvfile:
        new = []
        reader = csv.reader(csvfile)
        for row in reader:
            new.append(row)
    print(new[0])
    new[0] = data
    print(new[0])
    with open(file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in new:
            csvwriter.writerow(row)

def registraSaque(file,value):
    operacao = ['Saque',value]
    with open(file, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(operacao)

def registrarDeposito(file,value):
    operacao = ['Deposito',value]
    with open(file, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(operacao)  
