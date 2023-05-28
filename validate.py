import re
import sys

def validar_cpf(cpf):
    cpf_numerico = re.sub(r'[^0-9]', '', cpf)

    if cpf == cpf[0] * len(cpf):
        print('Você enviou dados sequenciais.')
        sys.exit()

    nove_digitos = cpf_numerico[:9]
    contador_ponderacao_1 = 10

    soma_digito_1 = 0
    for digito in nove_digitos:
        soma_digito_1 += int(digito) * contador_ponderacao_1
        contador_ponderacao_1 -= 1
    digito_1 = (soma_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_ponderacao_2 = 11

    soma_digito_2 = 0
    for digito in dez_digitos:
        soma_digito_2 += int(digito) * contador_ponderacao_2
        contador_ponderacao_2 -= 1
    digito_2 = (soma_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

    if cpf_numerico == cpf_gerado:
        print(f'{cpf_numerico} é válido')
    else:
        print('CPF inválido')

cpf = input('CPF: ')
validar_cpf(cpf)
