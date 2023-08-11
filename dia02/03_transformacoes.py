# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv('../data\produto.csv')
df.head()

# %%
df.info()

# %%
df['precoAjustado'] = df['vlPreco'] * 1.09
# df['precoAjustado'] = df['precoAjustado'].round(2)
df['precoAjustado'] = (df['vlPreco'] * 1.09).round(2)

df.head()

# %%
df['txAjuste'] = df['precoAjustado'] / df['vlPreco']

df.head()
# %%
df['txAjuste'] = ((df['precoAjustado'] / df['vlPreco'] - 1) * 100).round(2)
df.head()

# %%
df['txAjuste(%)'] = ((df['precoAjustado'] / df['vlPreco'] - 1) * 100).round(2)
df.head()

# %%
df = df.drop(columns='txAjuste')

# %%
del df['txAjuste']
df.head()

# %%
df['logTxAjuste'] = np.log(df['txAjuste(%)'])
df.head()

# %%
df['expTxAjuste']= np.exp(df['txAjuste(%)'])
df.head()

# %%
def teozinho(x):
    total = 1
    for i in range(2, int(x)+1):
        total *= i
    return total

# %%
df['precoAjustado'].apply(teozinho)
