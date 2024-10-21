
# Definindo o número de alunos
# num_alunos = 20

# # Estrutura de repetição para processar as notas de cada aluno
# for i in range(1, num_alunos + 1):
#     print(f"Aluno {i}:")
    
#     # Entrada de dados
#     nota1 = float(input("Digite a nota da primeira avaliação: "))
#     nota2 = float(input("Digite a nota da segunda avaliação: "))
#     nota_optativa = float(input("Digite a nota da avaliação optativa (ou -1 se não fez): "))

#     # Substituir a menor nota pela optativa, se ela for maior
#     if nota_optativa != -1:
#         menor_nota = min(nota1, nota2)
#         if nota_optativa > menor_nota:
#             if nota1 == menor_nota:
#                 nota1 = nota_optativa
#             else:
#                 nota2 = nota_optativa

#     # Cálculo da média
#     media = (nota1 + nota2) / 2

#     # Exibindo resultado e status
#     print(f"Média do semestre: {media:.2f}")
    
#     if media >= 6.0:
#         print("Aprovado")
#     elif media < 3.0:
#         print("Reprovado")
#     else:
#         print("Exame")

#RESOLUÇÃO:

# Variável para armazenar os candidatos válidos
candidatos = []
contador = 0  # Contador para garantir que 10 candidatos sejam processados

# # Enquanto não atingirmos 10 candidatos válidos
# while contador < 10:
#     nome = input("Digite o nome do candidato: ")
#     idade = int(input("Digite a idade do candidato: "))
    
#     # Verificar se o candidato tem idade mínima de 18 anos
#     if idade < 18:
#         print("Candidato menor de idade. Não pode participar.")
#     else:
#         telefone = input("Digite o telefone: ")
#         email = input("Digite o e-mail: ")
#         formacao = input("Digite a formação acadêmica: ")
#         experiencia = input("Digite a experiência profissional: ")
        
#         # Armazenar os dados do candidato
#         candidatos.append({
#             'nome': nome,
#             'idade': idade,
#             'telefone': telefone,
#             'email': email,
#             'formacao': formacao,
#             'experiencia': experiencia
#         })
        
#         contador += 1  # Incrementa o contador para processar o próximo candidato

# # Exibe a quantidade de candidatos válidos cadastrados
# print(f"{len(candidatos)} candidatos cadastrados com sucesso.")


# ESTRUTURA DE ARMAZENAMENTO

#[] VAZIO ()VAZIA {}VAZIO
