# concluir programa

import pandas as pd

# Dados de vendas
vendas_data = [
    {"id": 1, "data": '2023-01-05', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
    {"id": 2, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 1, "preco_unitario": 200.00, "cliente_id": 113},
  
]

# Criando o DataFrame de vendas
df_vendas = pd.DataFrame(vendas_data)

# Calculando estatísticas descritivas básicas
estatisticas_descritivas = df_vendas.describe()

# Mostrando as estatísticas descritivas
print("Estatísticas descritivas básicas para as colunas numéricas do DataFrame de vendas:")
print(estatisticas_descritivas)

