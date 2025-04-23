valor = float(input('Informe o valor: '))

match valor:
    case n if n >= 0:
        print(f'{valor} é positivo')
    case _:
        print(f'{valor} é negativo.')
