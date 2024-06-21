import pandas as pd
import numpy as np

def ahp_positivos(tabela):
    """
    Calcula a matriz normalizada dos critérios positivos para o AHP.

    Args:
    - tabela: DataFrame contendo os critérios positivos

    Returns:
    - DataFrame: matriz normalizada dos critérios positivos 
    """
    # Garantir que os dados são numéricos
    tabela = tabela.apply(pd.to_numeric, errors='coerce')
    # Normalização pela soma de cada coluna
    table_normalized = tabela.div(tabela.sum(), axis=1)
    return table_normalized

def ahp_negativos(tabela):
    """
    Calcula a matriz normalizada dos critérios negativos para o AHP.

    Args:
    - tabela: DataFrame contendo os critérios negativos

    Returns:
    - DataFrame: matriz normalizada dos critérios negativos
    """
    # Garantir que os dados são numéricos e não-zero
    tabela = tabela.apply(pd.to_numeric, errors='coerce').replace(0, np.nan)
    # Inversão e normalização pela soma de cada coluna
    table_inverse = 1 / tabela
    table_normalized = table_inverse.div(table_inverse.sum(), axis=1)
    return table_normalized

def matriz_de_decisao(tabela, fator):
    """
    Calcula a matriz de decisão ponderada pelo fator gaussiano.

    Args:
    - tabela: DataFrame contendo os critérios positivos e negativos normalizados
    - fator: DataFrame contendo o fator gaussiano calculado

    Returns:
    - DataFrame: matriz de decisão ponderada
    """
    # Multiplicação dos critérios pela matriz de fator gaussiano
    matriz_decisao = tabela.mul(fator.values)
    return matriz_decisao

def calcular_ahp_gaussiano(positivos, negativos):
    """
    Calcula o resultado do método AHP gaussiano.

    Args:
    - positivos: DataFrame contendo os critérios positivos
    - negativos: DataFrame contendo os critérios negativos

    Returns:
    - DataFrame: resultado do AHP gaussiano ordenado pela soma
    """
    # Obter matrizes normalizadas de positivos e negativos
    tabela_positivos = ahp_positivos(positivos)
    tabela_negativos = ahp_negativos(negativos)

    # Concatenar matrizes de positivos e negativos
    tabela_ahp = pd.concat([tabela_positivos, tabela_negativos], axis=1)

    # Calcular média e desvio padrão das colunas
    medias = tabela_ahp.mean()
    desvios = tabela_ahp.std().fillna(np.mean(tabela_ahp.std()))

    # Calcular fator gaussiano
    fator_gaussiano = (desvios / medias) / (desvios / medias).sum()

    # Criar DataFrame com fator gaussiano
    fator = pd.DataFrame(fator_gaussiano).T

    # Calcular matriz de decisão ponderada
    resultado_ahp = matriz_de_decisao(tabela_ahp, fator)

    # Calcular a soma das linhas e ordenar pelo resultado
    soma = resultado_ahp.sum(axis=1).sort_values(ascending=False).reset_index(drop=True)

    return soma
