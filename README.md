🏦 Previsão de Risco de Crédito (Credit Default Prediction)
Este projeto aplica técnicas avançadas de Data Science e Machine Learning para solucionar um dos maiores desafios do setor bancário: a inadimplência. O objetivo é prever a probabilidade de um cliente não honrar seus pagamentos, permitindo uma concessão de crédito mais segura e rentável.

📊 Principais Resultados do Modelo
O desempenho técnico e os marcos de negócio alcançados foram:

Métrica Principal (AUC-ROC): O modelo final atingiu 0.7432. Essa nota indica uma excelente capacidade de distinguir entre bons e maus pagadores.

Threshold de Decisão: Adotamos um ponto de corte conservador de 12% (0.12).

Lógica de Negócio: Preferimos ser mais rigorosos para proteger o capital do banco, identificando o máximo possível de inadimplentes potenciais.

Feature de Maior Impacto: A variável criada SOURCES_MEAN (média dos bureaus de crédito externos) consolidou-se como a informação mais relevante para o "cérebro" do modelo.

🧠 Ciclo de Desenvolvimento Tecnológico
O projeto foi dividido em três etapas críticas, documentadas detalhadamente nos notebooks:

1️⃣ Análise Exploratória de Dados (EDA)
Arquivo: 01_eda.ipynb

Limpeza de dados brutos e tratamento de nulos (remoção de colunas com >50% de ausência).

Análise de correlação e distribuição da variável alvo (TARGET).

Identificação de padrões de risco por idade, gênero e tipo de contrato.

2️⃣ Engenharia de Variáveis (Feature Engineering)
Arquivo: 02_feature_engineering.ipynb

Criação de Razões Financeiras:

ANUITY_INCOME_RATIO: Percentual da renda comprometido com a parcela.

CREDIT_INCOME_RATIO: Relação entre o crédito solicitado e a renda total.

GOODS_PRICE_RATIO: Proporção entre o valor do bem e o crédito concedido.

Consolidação de Scores: Criação da SOURCES_MEAN a partir das fontes externas 2 e 3.

Processamento Categórico: Aplicação de One-Hot Encoding para converter texto em dados numéricos processáveis.

3️⃣ Modelagem e Otimização
Arquivo: 03_modeling.ipynb

Algoritmo: Utilização do Random Forest Classifier com 200 árvores.

Tuning de Hiperparâmetros: (Opcional/Executado via GridSearchCV para encontrar a melhor combinação de profundidade e estimadores).

Avaliação Visual: Geração da Matriz de Confusão e da Curva ROC para validar a performance.

🛠️ Tecnologias e Ferramentas
Linguagem: Python 3.10

Processamento: Pandas e Numpy

Machine Learning: Scikit-Learn

Visualização: Matplotlib e Seaborn

Persistência do Modelo: Joblib

📂 Organização do Repositório
A estrutura segue as melhores práticas de organização de projetos de IA:

Plaintext
├── data/               # Bases de dados (Raw e Processed)
├── models/             # Modelo treinado (.pkl) pronto para uso
├── notebooks/          # Passo a passo da análise (01, 02 e 03)
├── src/                # Scripts Python para produção
│   ├── preprocessing.py # Funções de limpeza automática
│   └── modeling.py      # Funções de carga e predição
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação principal
🚀 Como Executar o Projeto
Clone o repositório:

Bash
git clone https://github.com/thallesfb1/credit-default-prediction.git
Instale as dependências:

Bash
pip install -r requirements.txt
Para predição em novos dados:
Utilize as funções presentes na pasta src/ para carregar o modelo em models/modelo_random_forest.pkl e processar novos arquivos CSV de clientes.