import os

chaves = ['Nome', 'CPF', 'Telefone', 'E-mail', 'Profissão', 'Empresa']
dados = [
        {
            chaves[0]: input('Informe o seu nome:'),
            chaves[1]: int(input('Informe o seu CPF:')),
            chaves[2]: int(input('Informe o seu telefone:')),
            chaves[3]: input('Informe o seu E-mail:'),
            chaves[4]: input('Informe a sua profissão:'),
            chaves[5]: input('Informe a sua empresa:')
        },
    ]

os.system('cls')
dados.append(chaves)
  
for i in range(len(chaves)):
    print(f'Índice {i + 1}:')
    print(f'Nome: {dados[i][chaves[0]]}')
    print(f'CPF: {dados[i][chaves[1]]}')
    print(f'Telefone: {dados[i][chaves[2]]}')
    print(f'E-mail: {dados[i][chaves[3]]}')
    print(f'Profissão: {dados[i][chaves[4]]}')
    print(f'Empresa: {dados[i][chaves[5]]}\n')


    
            



