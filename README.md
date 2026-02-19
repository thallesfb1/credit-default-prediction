🏦 Previsão de Risco de Crédito (Credit Default Prediction)
Este projeto utiliza técnicas de Machine Learning para prever a probabilidade de inadimplência de clientes em operações de crédito bancário. O objetivo principal é auxiliar na tomada de decisão, reduzindo prejuízos financeiros ao identificar perfis de alto risco antes da concessão do empréstimo.

📊 Principais Resultados
Performance do Modelo: O modelo final alcançou um AUC-ROC de 0.7432, demonstrando uma sólida capacidade de distinção entre bons e maus pagadores.

Visão de Negócio: Foi adotado um ponto de corte (threshold) rigoroso de 12%, priorizando a segurança do banco ao identificar uma maior quantidade de potenciais inadimplentes.

Variáveis Decisivas: A engenharia de variáveis foi fundamental, com destaque para o SOURCES_MEAN (média de scores externos), que se tornou a característica mais importante para as previsões do modelo.

🧠 Ciclo de Desenvolvimento
1. Análise Exploratória (EDA)
Realizada a limpeza de dados brutos, tratamento de valores nulos e análise de correlação. Identificamos que variáveis de bureaux de crédito externos possuem o maior impacto no risco.

2. Engenharia de Variáveis (Feature Engineering)
Criamos métricas de negócio personalizadas para enriquecer o modelo:

ANUITY_INCOME_RATIO: Comprometimento da renda mensal com a parcela.

CREDIT_INCOME_RATIO: Relação entre o crédito total solicitado e a renda total.

SOURCES_MEAN: Média consolidada das fontes de crédito externas.

GOODS_PRICE_RATIO: Proporção entre o valor do bem e o valor financiado.

3. Modelagem e Otimização
Algoritmo: Random Forest Classifier.

Otimização: Uso de GridSearchCV para ajuste fino de hiperparâmetros como profundidade das árvores e número de estimadores.

Avaliação: Validação baseada em Matriz de Confusão e Curva ROC.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.10.

Bibliotecas: Pandas, Scikit-Learn, Matplotlib, Seaborn e Joblib.

IDE: VS Code com Jupyter Notebooks.

📂 Estrutura do Repositório
notebooks/: Passo a passo da análise, desde a exploração até o modelo final.

src/: Scripts Python com funções prontas para produção (limpeza e predição).

models/: O arquivo .pkl do modelo treinado e pronto para uso.

data/: Armazenamento dos dados brutos e processados (conforme regras do .gitignore).

🚀 Como Executar
Instale as dependências:

Bash
pip install -r requirements.txt
Utilize as funções em src/ para processar novos arquivos de dados ou explore os notebooks na pasta notebooks/ para entender a lógica de construção.