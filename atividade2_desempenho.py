vendas = int(input("Informe a quantidade de vendas: "))

if vendas < 30:
    print("Insuficiente.")
elif vendas >= 30 and vendas <= 69:
    print("Regular.")
elif vendas >= 70 and vendas <= 99: 
    print("Bom.")
else:
    print("Excelente.")
