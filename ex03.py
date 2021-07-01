""" NOTAS DAS PROVAS E RESULTADO FINAL """

# Informações, status, e notas dos alunos
alunos = {}

n_aluno = 1
while True:
    print("\nCADASTRO DE NOTAS:")
    nome = input("\nDigite seu nome ou digite 'N' para encerrar: ")
    if nome in 'nN':
        break
       
    # Lê todas as notas do aluno
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    n3 = float(input("Digite a nota 3: "))
    n4 = float(input("Digite a nota 4: "))

    # Cálculo da média do aluno e situação do mesmo
    status = (n1 + n2 + n3 + n4) / 4
    if status > 7:
        status = 'Aprovado'
    else:
        status = 'Reprovado'

    # Guarda as informações e o resultado das notas do aluno no dicionário 'alunos'
    alunos[n_aluno] = (nome, [n1,n2,n3,n4], status)
    print("\nCadastro de notas realizado com sucesso!")
    print('-'*45)

    n_aluno += 1

print('-'*40)
print("NOTAS DOS ALUNOS:\n")

# Print formatado das informações, notas, e status dos alunos
for n_aluno, dados in alunos.items():
    print(f"Aluno: {n_aluno}")
    print(f"Nome do aluno: {dados[0]}")
    print(f"Notas do aluno: {dados[1]}")
    print(f"Status: {dados[2]}")
    print('-'*40)