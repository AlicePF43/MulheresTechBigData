"""ATIVIDADE - aula 07
Crie um código que seja capaz de ler e armazenar
uma sequência de 20 números pares e 20 números ímpares.
Obs: utilize estruturas de repetição para fechar esse conjunto
 de números.
"""

# Inicialize as listas vazias
numeros_pares = []
numeros_impares = []

# Solicite 20 números pares ao usuário
"""Estamos imprimindo uma mensagem e iniciando um loop que irá rodar 20 vezes.
Estamos solicitando ao usuário que digite um número par, convertendo a entrada inteira. 
Se o número for par (ou seja, se o resto da divisão por 2 for zero), 
adicionamos-o à lista numeros_pares. Caso contrário, mostraremos uma mensagem de erro."""
for i in range(20):
    numero = int(input('Digite um número par: ')) 
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        print("Esse número não é par. Tente novamente.")

# Solicite 20 números ímpares ao usuário
# Semelhante ao anterior usando números ímpares
print("Digite 20 números ímpares:")
for _ in range(20):
    numero = int(input('Digite um número ímpar: '))
    if numero % 2 != 0:
        numeros_impares.append(numero)
    else:
        print("Esse número não é ímpar. Tente novamente.")

# Exiba os resultados
print('Números pares:', numeros_pares)
print('Números ímpares:', numeros_impares)
