#Criando o dicionário

dados = {
    'Nome':'',
    'CPF':'',
    'RG':'',
    'Data de nascimento':'',
    'Gênero':'',
    'E-mail':'',
    'Telefone':'',
    'Tipo Sanguíneo':'',
    'Profissão':'',
    'Empresa':'',
}

#Informando os dados

print(f'{'-'*30} FORMULÁRIO DE CADASTRO {'-'*30}\n')

dados['Nome'] = input('Informe o Nome: ')
dados['CPF'] = input('Informe o CPF: ')
dados['RG'] = input('Informe o RG: ')
dados['Data de nascimento'] = input('Informe a data de nascimento: ')
dados['Gênero'] = input('Informe o gênero: ')
dados['E-mail'] = input('Informe o email: ')
dados['Telefome'] = input('Informe o telefone: ')
dados['Tipo Sanguíneo'] = input('Informe o tipo sanguíneo: ')
dados['Profissão'] = input('Informe a sua profissão: ')
dados['Empresa'] = input('Informe a empresa: ')

print('')
print(f'{'-'*30} FORMULÁRIO PREENCHIDO {'-'*30}\n')

#Mostra os dados na tela

for dado in dados:
    print(f'{dado}: {dados.get(dado)}')