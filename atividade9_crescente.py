
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1

if num1 == num2 or num2 == num3 or num1 == num3:
    print("Alguns números são iguais.")
else:
    print("Todos os números são diferentes.")

print("Números em ordem crescente:", num1, num2, num3)