Saldo = 0
LIMITE_SAQUES = 3
extrato = ""
limite = 500
saques = 0




while True:

    print("""
    ========== MENU ==========
    Escolha uma operação:
    [1]Saque

    [2]Depósito

    [3]Extrato

    [4]Sair
    =========================
    """)

    opção = float(input())

    if opção == 1:
        Valor = float(input("Escolha o valor a sacar: "))

        if saques >= LIMITE_SAQUES:
            print("Operação inválida! Número máximo de saques excedido!")

        elif Valor > limite:
            print("Operação inválida! Valor excedente ao limite disponível para saque!")

        elif Saldo < Valor:
            print("Operação inválida! Saldo insuficiente para saque!")

        elif Valor < 0:
            print("Operação inválida! Valor Inválido para saque!")

        else:
            Saldo -= Valor
            extrato += f"Saque: R${Valor:.2f}\n"
            saques += 1
    
    elif opção == 2:
        Dep = float(input("Escolha o Valor do a Depositar: "))
        if Dep < 0:
            print("Operação inválida! o valor selecionado é inválido!")
        
        else:
            Saldo += Dep
            extrato += f"Depósito: R$ {Dep:.2f}\n"

    elif opção == 3:
        print("\n========== EXTRATO ==========")
        print("Não houveram movimentações nesta conta até o momento!" if not extrato else extrato)
        print(f"\n Saldo: R$ {Saldo:.2f}")
        print("\n=============================")

    elif opção == 4:
        break

    else:
        print("Insira uma operação Válida!")