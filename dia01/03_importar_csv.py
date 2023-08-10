# %%
import pandas as pd

# %%
df = pd.read_csv('../data/pedido.csv')

df.head()

# %%
df.columns

# %%
df.shape

# %%
df.index

# %%
df.info(memory_usage='deep')

# %%
df.dtypes
