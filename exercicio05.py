# Leitura das notas
nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
nota_optativa = float(input("Digite a nota da avaliação optativa (ou -1 se não fez): "))

# Substituição da nota mais baixa pela optativa, se aplicável
if nota_optativa != -1:
    if nota1 < nota2:
        if nota_optativa > nota1:
            nota1 = nota_optativa
    else:
        if nota_optativa > nota2:
            nota2 = nota_optativa

media = (nota1 + nota2) / 2

# Determinação do status do estudante
if media >= 6.0:
    resultado = "Aprovado"
elif media < 3.0:
    resultado = "Reprovado"
else:
    resultado = "Exame"

# Resultados
print("Média do semestre:", media)
print("Status do estudante:", resultado)

