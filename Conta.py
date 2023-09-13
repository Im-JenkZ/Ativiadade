# Função para criar uma conta
def cria_conta(numero, titular, saldo, limite):
    conta = {
        'numero': numero,
        'titular': titular,
        'saldo': saldo,
        'limite': limite
    }
    return conta

# Função para realizar um depósito em uma conta
def deposita(conta, valor):
    conta['saldo'] += valor

# Função para realizar um saque em uma conta
def saca(conta, tipo_conta, valor):
    if tipo_conta == 'saldo':
        if valor <= conta['saldo']:
            conta['saldo'] -= valor
        else:
            print('Saldo insuficiente para saque.')
    elif tipo_conta == 'limite':
        if valor <= conta['limite']:
            conta['limite'] -= valor
        else:
            print('Limite insuficiente para saque.')
    else:
        print('Tipo de conta inválido.')

# Função para exibir o extrato de uma conta
def extrato(conta):
    print(f'Número da conta: {conta["numero"]}')
    print(f'Saldo: {conta["saldo"]}')

# Exemplo de uso das funções
minha_conta = cria_conta('12345-6', 'João', 1000.0, 2000.0)
extrato(minha_conta)
deposita(minha_conta, 500.0)
extrato(minha_conta)
saca(minha_conta, 'saldo', 200.0)
extrato(minha_conta)
saca(minha_conta, 'limite', 3000.0)
extrato(minha_conta)
