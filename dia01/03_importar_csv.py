# %%
import pandas as pd

# %%

# Importa um arquivo csv como dataframe
df = pd.read_csv('../data/pedido.csv')

df.head()

# %%

# Retorna o nome das colunas dos dataframe
df.columns

# %%

# Retorna a quantidade de linhas e colunas do dataframe
df.shape

# %%

# Retorna o range de index (RangeIndex(start=0, stop=1106, step=1))
df.index

# %%

# Retorna informações do dataframe
# memory_usage -> indica o uso da memória
df.info(memory_usage='deep')

# %%

# Retorna o tipo da dado de cada coluna
df.dtypes

# %%
