"""
Programa para Validar CPF

Exemplo - CPF 370.169.908-93
------------------------------
3 * 10  = 30        #   3 * 11  = 33
7 * 9   = 63        #   7 * 10  = 70
0 * 8   = 0         #   0 * 9   = 0
1 * 7   = 7         #   1 * 8   = 8
6 * 6   = 36        #   6 * 7   = 42
9 * 5   = 45        #   9 * 6   = 54
9 * 4   = 36        #   9 * 5   = 45
0 * 3   = 0         #   0 * 4   = 0
8 * 2   = 16        #   8 * 3   = 24
        = 233       #   9 * 2   = 18
                    #           = 294
"""
while True:
    try:
        cpf = int(input('Digite o número do CPF que deseja consultar: '))
        é_valido = True
    except:
        cpf = 0
        é_valido = False

    if é_valido == False:
        print('É necessário digitar apenas valores númericos.')
    else:

        cpf_digitado = str(cpf)
        cpf_validado = cpf_digitado[:-2]
        reverso = 10
        soma = 0
        tamanho_cpf = len(cpf_digitado)
        checando_se_numerico = 0
        if tamanho_cpf < 11 and é_valido:
            print(f'O número que você digitou tem {tamanho_cpf} digitos apenas.')
            print('É necessário informar 11 dígitos.\n')
        elif tamanho_cpf > 11 and é_valido:
            print(f'Você digitou um CPF com {tamanho_cpf} digitos.')
            print('É necessário informar 11 digitos.')
        else:
            for index in range(19):
                if index > 8:
                    index -= 9

                soma += int(cpf_validado[index]) * reverso
                reverso -= 1

                if reverso < 2:
                    reverso = 11
                    digito = 11 - (soma % 11)
                    if digito > 9:
                        digito = 0
                    soma = 0
                    cpf_validado += str(digito)


            # Evita sequências como 111.111.111, 555.555.555, etc.
            sequencia = cpf_validado == str(cpf_validado[0]) * len(cpf_digitado)

            # Não deixará que um CPF sequencial seja validado
            if cpf_digitado == cpf_validado and not sequencia:
                cpf_digitado = cpf_digitado[:9] + '-' + cpf_digitado[-2:]
                cpf_digitado = cpf_digitado[0:3] + '.' + cpf_digitado[3:6] + '.' + cpf_digitado[6:9] + cpf_digitado[9:]
                print(f'O CPF {cpf_digitado} é valido!')
            else:
                 print(f'O CPF {cpf_digitado} não é valido!')
            continuar = input('Deseja validar outro CPF? S/N: ').lower()

            if continuar in 'Nn':
                print('\nObrigado por utilizar nosso programa. \n'
                      'Espero que tenha curtido!')
                break
            elif continuar not in 'Ss' and 'Nn':
                continuar = input('Deseja validar outro CPF? S/N: ').lower()