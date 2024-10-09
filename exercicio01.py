# Valores para as variáveis
potencia_lampada = 60  # em watts
largura = 5  # em metros
comprimento = 4  # em metros

# Cálculos
area_comodo = largura * comprimento
potencia_necessaria = area_comodo * 3  # 3 watts por metro quadrado
bocais_necessarios = area_comodo / 3  # 1 bocal a cada 3 metros quadrados
lampadas_necessarias = potencia_necessaria / potencia_lampada

# Resultados
print("Número de lâmpadas necessárias:", int(lampadas_necessarias))
print("Número de bocais necessários:", int(bocais_necessarios))


