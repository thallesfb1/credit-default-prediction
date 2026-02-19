import pandas as pd
import numpy as np

def limpar_e_preparar_dados(df_bruto):
    """
    Consolida toda a lógica dos Notebooks 01 e 02 para dados novos.
    """
    df = df_bruto.copy()
    
    # 1. Criação das variáveis financeiras (Feature Engineering)
    df['DAYS_BIRTH_YEARS'] = df['DAYS_BIRTH'].abs() / 365
    df['ANUITY_INCOME_RATIO'] = df['AMT_ANNUITY'] / df['AMT_INCOME_TOTAL']
    df['CREDIT_INCOME_RATIO'] = df['AMT_CREDIT'] / df['AMT_INCOME_TOTAL']
    df['SOURCES_MEAN'] = df[['EXT_SOURCE_2', 'EXT_SOURCE_3']].mean(axis=1)
    df['GOODS_PRICE_RATIO'] = df['AMT_GOODS_PRICE'] / df['AMT_CREDIT']
    
    # 2. Seleção de colunas e tratamento de nulos
    # Aqui você deve manter apenas as colunas que o modelo espera
    colunas_relevantes = ['SOURCES_MEAN', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 
                          'DAYS_BIRTH_YEARS', 'ANUITY_INCOME_RATIO', ...] 
    
    # 3. One-Hot Encoding (Transformar texto em número)
    df_processado = pd.get_dummies(df).astype(float)
    
    # Garante que o DF final tenha as mesmas colunas que o modelo usou no treino
    return df_processado