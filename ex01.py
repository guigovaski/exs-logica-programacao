""" DIVISÕES DE PESO DOS LUTADRES """

# Laço de repetição
while True:
    print("\nDigite seus dados para saber sua categoria.\nDigite 0 para sair.\n")
    # Dados de entrada
    nome_lutador = input("Digite seu nome: ")
    if '0' in nome_lutador:
        break
    peso_lutador = float(input("Digite seu peso (kg): "))

    # Estrutura condicional
    if peso_lutador < 65:
        categoria = 'Pena'

    elif peso_lutador >= 65 and peso_lutador < 72:
        categoria = 'Leve'

    elif peso_lutador >= 72 and peso_lutador < 79:
        categoria = 'Ligeiro'

    elif peso_lutador >= 79 and peso_lutador < 86:
        categoria = 'Meio-médio'

    elif peso_lutador >= 86 and peso_lutador < 93:
        categoria = 'Médio'

    elif peso_lutador >= 93 and peso_lutador < 100:
        categoria = 'Meio-pesado'

    else:
        categoria = 'Pesado'

    # Print formatado das informações e categoria do lutador
    print('\n' + '-'*50)
    print(f"\nNome fornecido: {nome_lutador}\nPeso fornecido: {peso_lutador}KG")
    print(f"\nO lutador {nome_lutador} pesa {peso_lutador} KG e se enquadra na categoria {categoria}\n")
    print('-'*50)