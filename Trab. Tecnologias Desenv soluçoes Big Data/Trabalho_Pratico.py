# ----------------------------------------------------------------------------------
# Disciplina: DGT2823 - Tecnologias para Desenv. de Soluções de Big Data
# Trabalho Prático | Aluno: Gláucio Marques Nogueira
# Ambiente de Desenvolvimento: Visual Studio Code (VS Code) com Python 3.14 e biblioteca Pandas
# ----------------------------------------------------------------------------------


# ===============================================================================
# TRABALHO PRÁTICO E MICROATIVIDADES - TRATAMENTO E LIMPEZA DE DADOS COM PANDAS
# ================================================================================

# --------------------------------------------------------------------------------
# OBJETIVOS DO TRABALHO:
#--------------------------------------------------------------------------------
# 1. Ler e importar conjuntos de dados no formato CSV utilizando a biblioteca Pandas.
# 2. Manipular DataFrames, criando subconjuntos de dados e ajustando configurações
#    de exibição (como max_rows).
# 3. Inspecionar a estrutura dos dados (linhas, colunas, tipos de dados, valores 
#    nulos e uso de memória) utilizando métodos nativos como info(), head() e tail().
# 4. Realizar a limpeza e o tratamento de inconsistências em conjuntos de dados:
#    - Substituição de valores nulos na coluna 'Calories' por zero.
#    - Tratamento de valores ausentes e inconsistências na coluna 'Date'.
#    - Normalização e padronização de strings de datas (ex: remoção de aspas e 
#      correção do formato 'YYYYMMDD' para 'YYYY/MM/DD').
#    - Conversão do tipo de dados da coluna 'Date' para o tipo datetime.##
#    - Remoção de registros contendo dados nulos/inválidos remanescentes.
# --------------------------------------------------------------------------------
# DESCRIÇÃO DO CÓDIGO E ESTRUTURA:
# --------------------------------------------------------------------------------

# O script está estruturado em duas etapas principais:
# - Bloco 1 (Microatividades 1 a 5): Demonstração das rotinas básicas de leitura,
#   subconjuntos, configuração de visualização e extração de metadados do DataFrame.
# - Bloco 2 (Trabalho Prático): Execução sequencial dos passos de limpeza e 
#   sanitização do dataset 'dados_treino.csv', deixando os dados higienizados e 
#   prontos para análises estatísticas e mineração de dados.
# ================================================================================

import pandas as pd

print("==========================================================")
print("             TRABALHO PRÁTICO - TRATAMENTO DE DADOS       ")
print("==========================================================\n")

# -------------------------------------------------------------------
# Ler o arquivo CSV fornecido e atribuir a uma variável
# -------------------------------------------------------------------
# Utiliza-se sep=';' devido ao delimitador do CSV e engine='python' para leitura consistente
df_original = pd.read_csv('dados.csv', sep=';', engine='python')

# -------------------------------------------------------------------
# Verificar se os dados foram importados adequadamente
# -------------------------------------------------------------------
print("--- Informações Gerais do Dataset Original ---")
df_original.info()

print("\n--- Primeiras 5 linhas ---")
print(df_original.head())

print("\n--- Últimas 5 linhas ---")
print(df_original.tail())

# -------------------------------------------------------------------
# Cria uma nova variável e atribuir a cópia dos dados
# -------------------------------------------------------------------
df_tratado = df_original.copy()

# -------------------------------------------------------------------
# Substitui todos os valores nulos da coluna 'Calories' por 0
# -------------------------------------------------------------------
df_tratado['Calories'] = df_tratado['Calories'].fillna(0)
print("\n--- Nulos da coluna 'Calories' substituídos por 0 ---")
print(df_tratado[['ID', 'Date', 'Calories']])

# -------------------------------------------------------------------
# Substitui valores nulos da coluna 'Date' por '1900/01/01'
# -------------------------------------------------------------------
df_tratado['Date'] = df_tratado['Date'].fillna("'1900/01/01'")
print("\n--- Nulos da coluna 'Date' substituídos por '1900/01/01' ---")
print(df_tratado[['ID', 'Date']])

# -------------------------------------------------------------------
# Trata erro de conversão de data
# O valor '1900/01/01' gera erro no to_datetime se não tratado como NaN.
# Substitui-se '1900/01/01' por NaN (pd.NA)
# -------------------------------------------------------------------
df_tratado['Date'] = df_tratado['Date'].replace(["'1900/01/01'", "1900/01/01"], pd.NA)

# -------------------------------------------------------------------
# Trata valor sem formatação/aspas ("20201226")
# Limpa aspas simples e corrige a string "20201226" para o formato "2020/12/26"
# -------------------------------------------------------------------
df_tratado['Date'] = df_tratado['Date'].astype(str).str.replace("'", "")
df_tratado['Date'] = df_tratado['Date'].replace('20201226', '2020/12/26')

# -------------------------------------------------------------------
# Converte a coluna 'Date' para datetime
# -------------------------------------------------------------------
df_tratado['Date'] = pd.to_datetime(df_tratado['Date'], format='%Y/%m/%d', errors='coerce')
print("\n--- Coluna 'Date' convertida para Datetime ---")
print(df_tratado[['ID', 'Date']])

# -------------------------------------------------------------------
# Remove registros contendo valores nulos
# Apenas a coluna 'Date' possui um registro nulo (antiga linha 22)
# -------------------------------------------------------------------

df_tratado = df_tratado.dropna(subset=['Date'])

# -------------------------------------------------------------------
# Imprime o DataFrame final tratado e verificar alterações
# -------------------------------------------------------------------
print("\n==========================================================")
print("               DATAFRAME FINAL LIMPO E TRATADO            ")
print("==========================================================")
print(df_tratado.to_string())

print("\n--- Informações Finais da Estrutura dos Dados ---")
df_tratado.info()