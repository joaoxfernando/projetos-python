# Gerador de CPF

## ETAPAS DO GERADOR
- O programa gera um número aleatório de 9 dígitos e que não seja sequencial (111.111.111 ou 555.555.555).
- Fará a validação dos digitos do CPF seguindo o algoritmo encontrado logo abaixo.
- Exibe o número do CPF gerado já com os digitos validados.
- Pergunta se deseja gerar um novo CPF. 
- Ao final, um arquivo chamado "cpfs.txt" será gerado com todos os números de CPFs gerados.

## ALGORITMO
```
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
digito_2 = 11 - (289 % 11) = 11 - 8 = 3`
````
