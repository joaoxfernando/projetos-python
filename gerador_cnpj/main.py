import funcoes

while True:
    try:
        opcao = int(input('Escolhe uma das opções\n'
                      '[ 1 - VALIDAR CNPJ ]\n'
                      '[ 2 - GERAR CNPJ ]\n'
                      '[ 999 - SAIR ]'))
    except ValueError:
        opcao = 0
        print('A opção digitada é inválida')

    if opcao == 1:
        while True:
            try:
                cnpj = input('Digite o número de CNPJ que deseja validar: ')
            except ValueError:
                print('Digite apenas números!')

            if funcoes.valida(cnpj):
                print(f'O {cnpj} é válido!')
            else:
                print(f'O {cnpj} não é válido!')

            continuar = input('Deseja validar outro CNPJ?\nPressione qualquer tecla para continuar ou N para sair.  ')

            if continuar in 'Nn':
                print('Obrigado por utilizar nosso programa. \n'
                      'Espero que tenha curtido!')
                break


    elif opcao == 2:
        cnpj = funcoes.gera()
        formatado = funcoes.formata(cnpj)
        print(formatado)

    elif opcao == 999:
        print('Obrigado por utilizar nosso programa!')
        break

    else:
        print('Digite uma das opções!\n')