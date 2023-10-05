# %%
import pandas as pd

# %%
data = {
    'nome': ['Téo', 'Nah', 'Maria', 'José', 'Marina', 'Jéssica', 'Bino'],
    'idade': [30, 33, 2, 45, 65, 43, 40],
    'cor': ['Preto', 'Verde', 'Azul', 'Vermelho', 'Amarelo', 'Verde', 'Azul'],
    'renda': [3566, 1345, 0, 6576, 4325, 5326, 4321]
}

data['idade']

# %%

# Cria um dataframe
df = pd.DataFrame(data)
df

# %%

# Retorna apenas a coluna 'idade'
df['idade']

# %%

# Retorno: pandas.core.series.Series
type(df['idade'])

# %%

# Retorno: pandas.core.frame.DataFrame
type(df)

# %%

# Retorna a média das colunas 'idade' e 'renda'
df[['idade', 'renda']].mean()

# %%

# Retorna as primeiras 5 linhas do dataframe
df.head()

# %%

# Retorna as últimas 5 linhas do dataframe
df.tail()

# %%

# Retorna linhas aleatórias
df.sample(3)

# %%
