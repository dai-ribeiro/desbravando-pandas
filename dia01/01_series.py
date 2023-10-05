# %%
import pandas as pd

# %%
idade = [31, 33, 2, 29, 60, 58, 31, 45, 24]

# %%

# Cria uma série a partir da lista "idade"
s_idade = pd.Series(idade)
s_idade

# %%

# Métodos das séries
media = s_idade.mean()          # média
variancia = s_idade.var()       # variância    
des_pad = s_idade.std()         # desvio padrão
describe = s_idade.describe()   # descrição estatística
describe

# %%
nova_idade = []
for i in idade:
    if i >= 30:
        nova_idade.append(i)

nova_idade

# %%

# Filtra a série s_idade (maior ou igual que 30)
filtro = s_idade >= 30
s_idade[filtro]


# %%

# Filtra a série s_idade (menor que 30)
s_idade[~filtro]

# %%

# Filtro: traz apenas os dados com True
s_idade[[True, False, False, True, False, False, True, True, False]]

# %%
