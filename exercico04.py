# # Leitura do código de origem do produto
# codigo_origem = int(input("Digite o código de origem do produto: "))

# # Verificação da região de procedência
# if codigo_origem == 1:
#     regiao = "Região Sul"
# elif codigo_origem == 2:
#     regiao = "Região Norte"
# elif codigo_origem == 3:
#     regiao = "Região Leste"
# elif codigo_origem == 4:
#     regiao = "Região Oeste"
# elif codigo_origem == 5 or codigo_origem == 6:
#     regiao = "Região Nordeste"
# elif codigo_origem in [7, 8, 9]:
#     regiao = "Região Sudeste"
# elif codigo_origem == 10:
#     regiao = "Região Centro-oeste"
# elif codigo_origem == 11:
#     regiao = "Região Noroeste"
# else:
#     regiao = "Importado"

# # Impressão da região de procedência
# print("A região de procedência do produto é:", regiao)

## if/else e switch/case:##

# Leitura do código de origem do produto
codigo_origem = int(input("Digite o código de origem do produto: "))

# Verificação da região de procedência usando dicionário
regioes = {
    1: "Região Sul",
    2: "Região Norte",
    3: "Região Leste",
    4: "Região Oeste",
    5: "Região Nordeste",
    6: "Região Nordeste",
    7: "Região Sudeste",
    8: "Região Sudeste",
    9: "Região Sudeste",
    10: "Região Centro-oeste",
    11: "Região Noroeste"
}

# Obtenção da região de procedência
if codigo_origem in regioes:
    regiao = regioes[codigo_origem]
else:
    regiao = "Importado"

# Impressão da região de procedência
print("A região de procedência do produto é:", regiao)
