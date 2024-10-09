# Valores fixos para as dimensões da cozinha
comprimento = 6  # em metros
largura = 4  # em metros
altura = 3  # em metros

# Cálculo da área das paredes
area_parede1 = comprimento * altura * 2  # Duas paredes de comprimento
area_parede2 = largura * altura * 2      # Duas paredes de largura
area_total_paredes = area_parede1 + area_parede2

# Cálculo da quantidade de caixas de azulejos
caixas_necessarias = area_total_paredes / 1.5

print("Área total das paredes:", area_total_paredes, "m²")
print("Número de caixas de azulejos necessárias:", int(caixas_necessarias))
