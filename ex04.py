""" CONTATOS TELEFÔNICOS """

# Informações de todos os contatos
informacoes = {}

while True:
    contato = {}

    print('-'*40)
    print("\n|CADASTRO DE CONTATOS|")
    print("Pressione 'enter' vazio para sair.")

    nome = input("\nDigite seu nome: ")
    if nome == '':
        print("Fim do programa.")
        break

    idade = int(input("\nDigite sua idade: "))
    if idade <= 0:
        print("Idade inválida! Digite uma idade correspondente.")
        continue

    # Adiciona a idade do contato à 'contato'
    contato['idade'] = idade

    telefone = int(input("\nDigite seu telefone: "))
    if telefone <= 0:
        print("Número inválido!")
        continue

    # Adiciona o telefone do contato à 'contato'
    contato['telefone'] = telefone

    # Adiciona todas as informações do contato à 'informacoes'
    informacoes[nome] = contato

# Print dos contatos ordenados em ordem alfabética
print('\n' + '-'*40)
print(f"Contatos em ordem alfabética:\n {sorted(informacoes.items())}")

# Divide os contatos em menores e maiores de 18
maior18 = {'maiores de 18':[]}
menor18 = {'menores de 18':[]}

# Captura todos os contatos e verifica se são maiores de 18 anos ou não, e os adiciona em 'maior18' ou 'menor18'
for chave, valor in informacoes.items():
    if valor['idade'] >= 18:
        maior18['maiores de 18'].append(chave)
        maior18['maiores de 18'].append(valor)
    else:
        menor18['menores de 18'].append(chave)
        menor18['menores de 18'].append(valor)

# Print dos contatos maiores e menores de 18 anos
print('\n' + '-'*40)
print(f"\nMaiores de 18 anos: {maior18}")
print(f"\nMenores de 18 anos: {menor18}")
print('-'*40 + '\n')