import pandas as pd

# Criando um DataFrame
dados = {
    'Nome': ['Alice', 'Bob', 'Carlos'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

df = pd.DataFrame(dados)

# Exibindo o DataFrame
print(df)

# Calculando a média das idades
media_idade = df['Idade'].mean()
print(f"A média das idades é {media_idade}.")
