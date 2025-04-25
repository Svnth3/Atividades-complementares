Quantidade = int(input("Informe a quantidade de estudantes: "))

for n in range (Quantidade):
    nome = input('Informe o nome do aluno: ')
    nota1 = float(input("Informe a 1° nota: "))
    nota2 = float(input("Informe a 2° nota: "))
    nota3 = float(input("Informe a 3° nota: "))
    nota4 = float(input("Informe a 4° nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 7:
        print(f"{nome}está aprovado.")
    elif media < 5:
        print(f"{nome}está reprovado.")
    else:
        print(f"{nome} em recuperação.")