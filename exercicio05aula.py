# Número de alunos
num_alunos = int(input("Digite o número de alunos: "))

# Este loop for itera sobre cada aluno, de 0 até num_alunos - 1. O print exibe o número do aluno atual.
for i in range(num_alunos):
    print(f"\nAluno {i + 1}:")  
    nota1 = float(input("Digite a nota da primeira avaliação: "))
    nota2 = float(input("Digite a nota da segunda avaliação: "))
    nota_optativa = float(input("Digite a nota da avaliação optativa (ou -1 se não fez): "))
# Para cada aluno, as notas das duas avaliações principais e a nota da avaliação optativa (se houver).
    
###Se o aluno fez a avaliação optativa (nota_optativa != -1), 
###o programa verifica qual das duas notas principais é a menor e a substitui pela nota optativa, caso esta seja maior.  
   
    if nota_optativa != -1:
        if nota1 < nota2:
            if nota_optativa > nota1:
             nota1 = nota_optativa
    else:
        if nota_optativa > nota2:
            nota2 = nota_optativa

##A média das duas notas (após a possível substituição) é calculada.##
    media = (nota1 + nota2) / 2

    # Determinação do status do estudante comm base na média
    if media >= 6.0:
        resultado = "Aprovado"
    elif media < 3.0:
        resultado = "Reprovado"
    else:
        resultado = "Exame"

    # O programa imprime o status do estudante
    print("Média do semestre:", media)
    print("Status do estudante:", resultado)
