# %%
import pandas as pd

# %%
df = pd.read_csv('../data/produto.csv')
df.head()

# %%
df = df.rename(columns={'vlPreco': 'vlPrecoReal'})
df.head()

# %%
filtro = df['vlPrecoReal'] > 10
df[filtro]

# %%
queijos_premium = ['queijo brie', 'queijo coalho', 'ricota']
filtro_queijos = df['descItem'].isin(queijos_premium)
df[filtro_queijos]

# %%
df['vlPrecoInflacao'] = (df['vlPrecoReal'] * 1.09).round(2)
df.head()

# %%
df['vlPrecoInflracaoLog'] = np.log(df['vlPrecoInflacao'])
df.head()
