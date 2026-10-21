# ----------------------------------------------------------------------------------
# Disciplina: DGT2823 - Tecnologias para Desenv. de Soluções de Big Data
# Trabalho Prático | Aluno: Gláucio Marques Nogueira
# Ambiente de Desenvolvimento: Visual Studio Code (VS Code) com Python 3.14 e biblioteca Pandas
# ----------------------------------------------------------------------------------


# Microatividade 1: Descrever como ler um arquivo CSV usando a biblioteca Pandas (Python)
import pandas as pd

# Lendo o arquivo CSV com o separador ';' conforme solicitado
df = pd.read_csv('dados.csv', sep=';', engine='python')

# Exibindo os dados do arquivo dados.csv na tela
print("--- MICROATIVIDADE 1 ---")
print(df)


# Microatividade 2: Descrever como criar um subconjunto de dados
# a partir de um conjunto existente usando a biblioteca Pandas (Python)

# Criando um subconjunto com apenas 3 colunas do dataframe original
df_subset = df[['Duration', 'Pulse', 'Calories']]
print("\n--- MICROATIVIDADE 2 ---")
print(df_subset.head())


# Microatividade 3: Descrever como configurar o número máximo de linhas a serem exibidas na
# visualização de um conjunto de dados usando a biblioteca Pandas (Python)

# Configurando o pandas para exibir até 9999 linhas
pd.options.display.max_rows = 9999
print("\n--- MICROATIVIDADE 3 ---")
print(df.to_string())


# Microatividade 4: Descrever como exibir as primeiras e últimas “N” linhas 
# de um conjunto de dados usando a biblioteca Pandas (Python)
print("\n--- MICROATIVIDADE 4 (Primeiras 10 linhas) ---")
print(df.head(10))
print("\n--- MICROATIVIDADE 4 (Últimas 10 linhas) ---")
print(df.tail(10))


# Microatividade 5: Descrever como exibir informações gerais sobre as colunas, linhas e
# dados de um conjunto de dados usando a biblioteca Pandas (Python)

print("==================================================")
print("MICROATIVIDADE 5: Informações Gerais do Dataset")
print("==================================================\n")

# Procedimento 2.1: Imprimir informações gerais sobre o conjunto
print("--- Saída do comando df.info(): ---")
df.info()
print("\n--- Procedimento 2.3: Respostas detalhadas ---")

total_linhas = df.shape[0]
print(f"1. Total de linhas: {total_linhas}")

total_colunas = df.shape[1]
print(f"2. Total de colunas: {total_colunas}")

print("\n3. Quantidade de dados nulos por coluna:")
print(df.isnull().sum())

print("\n4. Tipo de dado de cada coluna:")
print(df.dtypes)

memoria_usada = df.memory_usage(deep=True).sum()
print(f"\n5. Memória utilizada: {memoria_usada} bytes ({memoria_usada / 1024:.2f} KB)")