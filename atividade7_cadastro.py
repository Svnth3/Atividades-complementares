quantidade = int(input("Informe a quantidade de cadastro: "))
limite_quantidade = 10 
limite_ano = 2007
for n in range(quantidade):
    limite_quantidade -= 1 
    if limite_quantidade == 0:
        print("Limite atingido. ")
        break
    nome = input("Informe o nome: ")
    ano = int(input("Informe o ano de nascimento, Ex. 2002: "))
    ver_ano = 2025 - ano
    if ver_ano < 18:
        print("Idade inválida")
        ano = int(input("Digite uma data válida: "))
        ver_ano = 2025 - ano
    telefone = input("Informe o telefone: ")
    if len(telefone) < 11:
        print("Digite um numero válido com dd, ex. 21 x xxxx xxxx.")
        telefone = int(input("Informe o telefone: "))

    Exp = input('Informe experiência profissional ou digite Primeiro emprego: ')
    print("")
    print(f"Candidato {nome}, idade {ver_ano}, tel {telefone}.")
    print(f'Experiência Profissional {Exp}.')
    print("")
