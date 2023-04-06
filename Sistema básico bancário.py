# Definição do menu de opções
menu = """

[d] Depositar
[s] Sacar
[e] Extrato 
[q] Sair

=>"""

# Definição das variáveis iniciais
saldo = 0 
limite = 500
extrato = " "
numero_saque = 0
LIMITE_SAQUES = 3 

# Laço de repetição para apresentar o menu e realizar as operações selecionadas
while True:

    # Apresentação do menu e leitura da opção selecionada pelo usuário
    opcao = input(menu)

    # Operação de depósito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0: # Verifica se o valor informado é maior que zero
            saldo += valor # Adiciona o valor informado ao saldo
            extrato += f"Depósito: R$ {valor:.2f}\n" # Adiciona a descrição do depósito ao extrato

        else: # Caso o valor informado seja menor ou igual a zero
            print("Operação falhou! O valor informado não é valido") # Apresenta mensagem de erro

    # Operação de saque
    elif opcao == "s":
        valor = float(input("Ubforme o valor do saque: "))

        excedeu_saldo = valor > saldo # Verifica se o valor do saque excede o saldo disponível
        excedeu_limite = valor > limite # Verifica se o valor do saque excede o limite de saque
        excedeu_saques = numero_saque >= LIMITE_SAQUES # Verifica se o número de saques já excedeu o limite permitido

        if excedeu_saldo: # Caso o valor do saque exceda o saldo disponível
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite: # Caso o valor do saque exceda o limite de saque
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques: # Caso o número de saques já exceda o limite permitido
            print("Operação falhou! Número máximo de saques excedidos.")

        elif valor > 0: # Caso o valor informado seja maior que zero
            saldo -= valor # Subtrai o valor informado do saldo
            extrato += f"Saque: R$ {valor:.2f}\n" # Adiciona a descrição do saque ao extrato
            numero_saque += 1 # Adiciona 1 ao contador de saques realizados

        else: # Caso o valor informado seja menor ou igual a zero
            print("Operação falhou!  O valor informado é invalido.") # Apresenta mensagem de erro

    # Operação de apresentação do extrato
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("não foram realizadas movimentações." if not extrato else extrato) # Verifica se há movimentações no extrato para apresentá-las
        print(f"\nSaldo: R$ {saldo:.2f}") # Apresenta o saldo atual
        print("===========================================")

    elif opcao == "q":
    # se a opção selecionada for "q" (sair), interrompe o loop while com o comando "break"
        break

    else:
    # caso contrário, a opção é inválida e exibe uma mensagem pedindo para selecionar novamente
        print("Operação inválida, por favor selecione novamente a operação desejada.")

