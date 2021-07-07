import requests as r

while True:
    cep = input('Digite o CEP que deseja consultar o endereço: ')
    cep = cep.replace('-', '')
    try:
        cep2 = int(cep)
        if type(cep2) == int and len(cep) == 8:
            break
    except:
        print('ERRO! Digite valores numéricos.')
url = 'https://cep.awesomeapi.com.br/json/'
busca_cep = f'{url}{cep}'


import requests as r

def pesquisar_cep(busca_cep):
    resp = r.get(busca_cep)
    end = resp.json()
    endereco = f'O endereço completo do CEP {cep} é:\n' \
               f'{end["address"]}\n' \
               f'Bairro: {end["district"]}\n' \
               f'Cidade: {end["city"]}\n' \
               f'Estado: {end["state"]}\n' \
               f'E o DDD da região é: {end["ddd"]}'
    print(endereco)

pesquisar_cep(busca_cep)