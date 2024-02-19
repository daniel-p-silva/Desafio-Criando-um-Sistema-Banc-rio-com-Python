
from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def valor_deposito():
    while True:
        valor = float(input('Informe o valor a ser depositado: '))
        if valor <= 0:
            print('Informe um valor valido!')
        else:
            return valor

saques_por_dia = {}

def quantidade_de_saques(valor_do_saque):
    global saques_por_dia
    global saldo
    
    dia = datetime.now().date()
    if dia in saques_por_dia:
        if saques_por_dia[dia] >=3:
            print('Você já realizou o número máximo de saques hoje.')
            return False
        elif saldo < valor_do_saque:
            print('Saldo insuficiente')
            return False
        elif valor_do_saque > 500.00:
            print('Valor limite do saque é de R$ 500,00 ')
            return False
        else:
            saques_por_dia[dia] += 1
            saldo -= valor_do_saque
            data = datetime.now()
            registro_de_lancamento('Saque', data, valor)
            return True
        
    else:
        if saldo < valor_do_saque:
            print('Saldo insuficiente.')
            return False
        elif valor_do_saque > 500.00:
            print('Valor limite do saque é de R$ 500,00.')
            return False
        else:
            saques_por_dia[dia] = 1
            saldo -= valor_do_saque
            data = datetime.now()
            registro_de_lancamento('Saque', data, valor)
            return True
    
lancamentos = []

def registro_de_lancamento(data, tipo, valor):
    lancamentos.append((data, tipo, valor))



while True:
    opcao = input(menu)
    
    if opcao == "d":
        print("Depositar")
        valor = valor_deposito()
        print(f'Valor depositado: R$ {valor:.2f}')
        saldo += valor
        print(f'Saldo Atual: R$ {saldo:.2f}')
        data = datetime.now()   
        registro_de_lancamento('Deposito', data, valor)
        #novo_deposito()
        

    if opcao == "s":
        print("Saque")
        valor_do_saque = float(input('Informe o valor para saque: '))
        if quantidade_de_saques(valor_do_saque):
            print(f'Valor do Saque: R$ {valor_do_saque:.2f}')
            print(f'Saldo Atual: R$ {saldo:.2f}')
        else:
            print('Não foi possível realizar o saque.')
        

    elif opcao == "e":
        print('Extrato')
        for lancamento in lancamentos:
            data, tipo, valor = lancamento
            print(f'Data: {data}, {tipo}, R$: {valor}')
    elif opcao == 'q': 
        break   
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')


