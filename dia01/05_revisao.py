# %%
import pandas as pd

# %%
idade = pd.Series([30, 34, 56, 23])
idade.describe()

# %%
df = pd.DataFrame({
    'nome': [ 'teo', 'nah', 'maria'],
    'idade': [30, 33, 2]
})

df

# %%
df_pedido = pd.read_csv('../data/pedido.csv')
df_pedido.head()

# %%
df.info(memory_usage='deep')

# %%
df_pedido.dtypes

# %%
df_pedido[['descUF', 'flKetchup']]

# %%
df_pedido.iloc[0:10]

# %%
df_pedido.loc[892]
