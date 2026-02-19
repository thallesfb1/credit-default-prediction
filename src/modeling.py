# import necessário para carregar o modelo e fazer previsões
import joblib
import pandas as pd
import numpy as np

def carregar_modelo(caminho_modelo='../models/modelo_random_forest.pkl'):
    """
    Carrega o modelo Random Forest treinado a partir de um arquivo .pkl.
    """
    try:
        modelo = joblib.load(caminho_modelo)
        print(f"Modelo carregado com sucesso de: {caminho_modelo}")
        return modelo
    except FileNotFoundError:
        print(f"Erro: O arquivo do modelo não foi encontrado em {caminho_modelo}")
        return None

def prever_risco(modelo, df_processado, threshold=0.12):
    """
    Recebe o modelo, os dados já limpos/preparados e o ponto de corte (threshold).
    Retorna as probabilidades e a decisão final do banco.
    """
    # 1. Pegar as probabilidades da classe 1 (inadimplente)
    probabilidades = modelo.predict_proba(df_processado)[:, 1]
    
    # 2. Aplicar o threshold rigoroso de 12% que definimos no projeto
    decisoes = (probabilidades >= threshold).astype(int)
    
    return probabilidades, decisoes

def exportar_resultados(df_original, probabilidades, decisoes, caminho_csv='../data/processed/previsoes.csv'):
    """
    Concatena os resultados ao dataframe original e salva um arquivo final.
    """
    df_final = df_original.copy()
    df_final['SCORE_RISCO'] = probabilidades
    df_final['APROVACAO_NEGADA'] = decisoes  # 1 significa que o banco barrou o crédito
    
    df_final.to_csv(caminho_csv, index=False)
    print(f"Predições exportadas para: {caminho_csv}")
    return df_final