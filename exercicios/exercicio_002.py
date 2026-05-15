idade = int(input("Digite a idade (ex.: 35): "))

if idade < 0:
    print("Número inválido.")
else:
    if idade <= 12:
        categoria = "Criança"
    elif idade <= 17:
        categoria = "Adolescente"
    elif idade <= 59:
        categoria = "Adulto"
    else:
        categoria = "Idoso"

    print(f"Categoria: {categoria}")