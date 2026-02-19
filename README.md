# 🏦 Credit Default Prediction

Projeto de **Machine Learning aplicado ao setor bancário**, com foco em
previsão de inadimplência para apoiar decisões de concessão de crédito
mais seguras e rentáveis.

------------------------------------------------------------------------

## 🎯 Objetivo do Projeto

Desenvolver um modelo preditivo capaz de estimar a probabilidade de um
cliente se tornar inadimplente, utilizando dados históricos e técnicas
avançadas de Data Science.

O modelo permite:

-   ✔ Redução do risco de crédito\
-   ✔ Melhor alocação de capital\
-   ✔ Decisões orientadas por dados\
-   ✔ Aumento da rentabilidade da carteira

------------------------------------------------------------------------

## 📊 Principais Resultados

### 🏆 Performance do Modelo

-   **Métrica Principal (AUC-ROC):** `0.7432`\
    \> Excelente capacidade de distinção entre bons e maus pagadores.

-   **Threshold de decisão:** `0.12 (12%)`\
    \> Estratégia conservadora para proteger o capital do banco.

------------------------------------------------------------------------

### 🧠 Lógica de Negócio Aplicada

Optamos por um threshold mais baixo para:

-   Maximizar a identificação de inadimplentes
-   Reduzir perdas financeiras
-   Priorizar segurança da carteira

------------------------------------------------------------------------

### ⭐ Feature de Maior Impacto

-   **SOURCES_MEAN**\
    Média dos scores externos (bureaus de crédito).

------------------------------------------------------------------------

# 🔄 Ciclo de Desenvolvimento

## 1️⃣ Análise Exploratória de Dados (EDA)

📁 `01_eda.ipynb`

-   Limpeza de dados
-   Remoção de colunas com \>50% de valores nulos
-   Análise da variável alvo (`TARGET`)
-   Correlação entre variáveis
-   Análise de risco por idade, gênero e tipo de contrato

------------------------------------------------------------------------

## 2️⃣ Engenharia de Variáveis

📁 `02_feature_engineering.ipynb`

### 📈 Criação de Razões Financeiras

-   `ANUITY_INCOME_RATIO`
-   `CREDIT_INCOME_RATIO`
-   `GOODS_PRICE_RATIO`

### 📊 Consolidação de Scores

-   `SOURCES_MEAN` (média das fontes externas 2 e 3)

### 🔠 Processamento Categórico

-   One-Hot Encoding

------------------------------------------------------------------------

## 3️⃣ Modelagem e Otimização

📁 `03_modeling.ipynb`

-   Algoritmo: **Random Forest Classifier**
-   200 árvores
-   Ajuste opcional com `GridSearchCV`
-   Avaliação com:
    -   Matriz de Confusão
    -   Curva ROC
    -   AUC Score

------------------------------------------------------------------------

# 🛠️ Tecnologias Utilizadas

  Categoria              Ferramenta
  ---------------------- ---------------------
  Linguagem              Python 3.10
  Manipulação de Dados   Pandas, NumPy
  Machine Learning       Scikit-Learn
  Visualização           Matplotlib, Seaborn
  Persistência           Joblib

------------------------------------------------------------------------

# 📂 Estrutura do Projeto

    credit-default-prediction/
    │
    ├── data/
    │   ├── raw/
    │   └── processed/
    │
    ├── models/
    │   └── modelo_random_forest.pkl
    │
    ├── notebooks/
    │   ├── 01_eda.ipynb
    │   ├── 02_feature_engineering.ipynb
    │   └── 03_modeling.ipynb
    │
    ├── src/
    │   ├── preprocessing.py
    │   └── modeling.py
    │
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# 🚀 Como Executar o Projeto

## 1️⃣ Clone o repositório

``` bash
git clone https://github.com/thallesfb1/credit-default-prediction.git
```

## 2️⃣ Instale as dependências

``` bash
pip install -r requirements.txt
```

## 3️⃣ Realizar nova predição

Utilize os scripts da pasta `src/` para:

-   Carregar o modelo salvo em `models/modelo_random_forest.pkl`
-   Processar novos dados CSV
-   Gerar probabilidades de inadimplência
