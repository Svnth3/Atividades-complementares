temp_limite1 = float(15)
temp_limite2 = float(25)
temperatura = float(input("Informe a temperatura: "))

if temperatura <= temp_limite1:
    print("Temperatura dentro de faixa segura.")
elif temperatura <= temp_limite2:
    print("Verificar o sistema de refrigeração.")
else:
    print("Desligar o sistema de refrigeração imediatamente.")