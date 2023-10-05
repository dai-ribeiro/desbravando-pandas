# %%
import pandas as pd

# %%
df = pd.read_csv('../data\pedido.csv')

df.head()

# %%
df[['idPedido', 'descUF']].head()

# %%
df.columns

# %%
colunas = [
    'idPedido',
    'descUF',
    'flKetchup', 
    'txtRecado',
    'dtPedido'     
]

df = df[colunas]
df.head()

# %%

# Cria uma dataframe novo com 100 registros aleatórios do df antigo
df_sample = df.sample(100)
df_sample

# %%

# iloc retorna a posição
df_sample.iloc[0] # posição zero (linha 0)

# %%

# loc retorna o índice do dataframe
# retorna erro se o índice não existir
df_sample.loc[0] # index=0


# %%

# Retorna as linhas de 0 a 10 das colunas indicadas
df_sample.iloc[0:10][['idPedido', 'dtPedido']]

# %%
