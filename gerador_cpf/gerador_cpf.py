"""
Gerador de CPFs aleatórios e matematicamente válidos.
Exemplo - CPF 325-875-343-13 (cpf gerado pelo gerador)

--------------------------------------
ALGORITMO PARA VALIDAR O DIGITO DO CPF
---------------------------------------
3 * 10  = 30        #   3 * 11  = 33
2 * 9   = 18        #   2 * 10  = 20
5 * 8   = 40        #   5 * 9   = 45
8 * 7   = 56        #   8 * 8   = 64
7 * 6   = 42        #   7 * 7   = 49
5 * 5   = 25        #   5 * 6   = 30
3 * 4   = 12        #   3 * 5   = 15
4 * 3   = 12        #   4 * 4   = 16
3 * 2   = 6         #   3 * 3   = 9
        = 241       #   1 * 2   = 2
                    #           = 283

Fórmula para cálculo de cada digito:
digito_1 = 11 - (soma % 11)
digito_1 = 11 - (10) = 1

digito_2 = 11 - (289 % 11) = 11 - 8 = 3


"""
from random import randint

while True:
    numero = randint(100000000, 999999999)
    cpf = str(numero)
    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9
        total += int(cpf[index]) * reverso
        reverso -= 1

        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)

            if digito > 9:
                digito = 0
            total = 0
            cpf += str(digito)

    # Evita sequências como 111.111.111, 555.555.555, etc.
    sequencia = cpf == str(cpf[0]) * len(cpf)


    # Não validará um número de CPF sequencial.
    if cpf and not sequencia:
        cpf_completo = cpf[:9] + '-' + cpf[-2:]
        cpf_completo = cpf_completo[0:3] + '.' + cpf_completo[3:6] + '.' + cpf_completo[6:9] + cpf_completo[9:]
        print(f'O número do CPF gerado foi: {cpf_completo}')
        continuar = input('Deseja continuar? S/N: ')
        if continuar in 'Nn':
            print('\nObrigado por utilizar nosso programa. \nEspero que tenha gostado')
            break