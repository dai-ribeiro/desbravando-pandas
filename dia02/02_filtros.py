# %%
import pandas as pd

# %%
df = pd.read_csv('../data\pedido.csv')
df.head()

# %%
idade = [ 20, 14, 13, 67, 54, 19, 24]

idade_20 = []
for i in idade:
    if i > 20:
        idade_20.append(i)

idade_20

# %%
idade = pd.Series([ 20, 14, 13, 67, 54, 19, 24])

filtro = idade > 20

idade[filtro]

# %%
filtro_uf = df['descUF'] == 'São Paulo'
df[filtro_uf]

# %%
# É de SP e pediu ketchup

filtro_sp_ketchup = (df['descUF'] == 'São Paulo') & (df['flKetchup'])
df[filtro_sp_ketchup]

# %%

filtro_ufs_ketchup = ((df['descUF'] == 'São Paulo') | (df['descUF'] == 'Rio de Janeiro') | (df['descUF'] == 'Paraná')) & (df['flKetchup'])

df[filtro_ufs_ketchup]['descUF'].unique()

# %%
uf_recortes = ['São Paulo', 'Rio de Janeiro', 'Paraná']

filtro_ufs_ketchup = df['descUF'].isin(uf_recortes) & df['flKetchup']

df[filtro_ufs_ketchup]

# %%
filtro_txt_na = df['txtRecado'].isna()
df[filtro_txt_na]

# %%
