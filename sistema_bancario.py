menu = '''

================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
================

->'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        print("Saldo atual:")
        print(saldo)
        valor = float(input("digite o valor a ser depositado:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        print("Saque")
        print("Saldo atual:")
        print(saldo)
        valor = float(input("digite o valor a ser sacado:"))

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        excedeu_limite = valor > limite

        if excedeu_limite:
            print("Você ultrapassou seu limite de saque!")

        elif excedeu_saques:
            print("Você chegou ao limite de saques diários!")

        elif valor <= saldo:
            saldo -= valor
            extrato += f"Saque R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("Você não tem saldo suficiente para esta operação")
    
    elif opcao == "3":
        print("======= Extrato ========")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=========================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, porfavor selecione novamente a operação desejada.")