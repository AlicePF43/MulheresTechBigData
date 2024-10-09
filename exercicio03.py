# Valores fixos para as variáveis
odometro_inicio = 1000  # km no início do dia
odometro_fim = 1200  # km no final do dia
litros_gastos = 20  # litros de combustível gastos
valor_recebido = 300  # valor total recebido dos passageiros em R$

preco_combustivel = 4.87  # R$ por litro

# Cálculos
km_percorridos = odometro_fim - odometro_inicio
media_consumo = km_percorridos / litros_gastos
custo_combustivel = litros_gastos * preco_combustivel
lucro_liquido = valor_recebido - custo_combustivel

print("Média de consumo (km/L):", media_consumo)
print("Lucro líquido do dia (R$):", lucro_liquido)
