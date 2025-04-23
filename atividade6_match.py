nota1 = float(input("Informe a 1º nota: "))
nota2 = float(input("Informe a 2º nota: "))
optativa = float(input("Informe a nota da optativa (-1 se não realizada): "))
notafinal1 = nota1
notafinal2 = nota2
match optativa:
    case -1:
        notafinal1 = nota1
        notafinal2 = nota2
    case _: 
        if nota1 < nota2:
            notafinal1 = optativa
        else:
            notafinal2 = optativa

media = (notafinal1 + notafinal2) / 2 
print (media)
match media: 
    case n if media >= 6:
        Situação = "Aprovado"
    case n if media < 3:
        Situação = "Reprovado"
    case _:
        Situação = "Exame"

print(f'Situação é {Situação}, sua média é {media}.')
    

 
