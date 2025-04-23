quant = int(input("Informe a quantidade de avaliações feitas: "))
soma = 0
num= 0
for n in range(quant):
    num = num+1
    nota = float(input(f"Informe a nota da {num}° avaliação: "))
    soma += nota
media = soma / quant

if media < 5:
    print("Reprovado.")
elif media <= 7:
    print("Recuperação.")
else:
    print("Aprovado.")