""" CÓDIGOS DE PRODUTOS DE UMA LOJA """

# Função para verificar se o número está entre o intervalo
def validar(dados):
    if dados >= 10000 and dados <= 30000:
        return dados
    else:
        print("O valor não está entre o intervalo")

# Função que retorna o dígito verificador do código:
def calcular(numero):
    l = []

    i = 2
    for digito in numero:
        multiplica = int(digito) * i
        l.append(int(multiplica))
        i += 1

    soma = sum(l)
    total = soma % 7 

    return total

# Programa
while True:
    codigo = int(input("\nDigite aqui o código do produto [10000, 30000]: "))

    # Verifica se o código respeita o invervalo solicitado [10000, 30000]
    test = validar(codigo)
    if test:
        print('\n' + '-'*50)
        print(f"\nCódigo do produto: {codigo}")
        break
    else:
        print("O codigo não está no intervalo solicitado [10000, 30000]")
        continue

# Resultado final do código já formatado
codigo_final = calcular(str(codigo))

print(f"Código final do produto: {codigo}-{codigo_final}\n")