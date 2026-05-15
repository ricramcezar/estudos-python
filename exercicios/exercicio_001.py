nome = input("Digite o nome: ").strip().title()
idade = int(input("Digite a idade (ex.: 35): "))
cidade = input("Digite a cidade: ").strip().title()
estado = input("Digite o estado com duas letras (ex.: SP): ").strip().upper()

print(f"{nome} tem {idade} anos e mora em {cidade}-{estado}.")