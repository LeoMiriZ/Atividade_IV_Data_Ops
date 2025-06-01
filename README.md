# Atividade_IV_Data_Ops

## Requisitos
Construa uma DAG no Apache Airflow para coletar dados da cotação do dólar comercial (USD/BRL), processar os dados com média móvel de 10 dias e gerar um gráfico comparativo da variação cambial.

### Objetivos
- Aplicar princípios de DataOps: modularidade, agendamento e automação

- Utilizar Python e bibliotecas de análise de dados

- Criar uma DAG funcional no Airflow com controle de dependências

- Utilizar yfinance ou pandas_datareader para coleta de dados externos

### Descrição da Tarefa

- Implemente uma DAG chamada etl_dolar_brl com as seguintes etapas:

1. Extração

    - Coletar dados históricos da cotação do dólar americano em relação ao real brasileiro (USDBRL=X) entre 01/01/2023 e 31/12/2023

    - Salvar os dados brutos em dags/data/dolar_raw.csv

2. Transformação

    - Remover valores nulos

    - Converter o campo de fechamento para numérico

    - Calcular a média móvel de 10 dias

    - Salvar o arquivo como dags/data/dolar_tratado.csv

3. Visualização

    - Gerar gráfico da cotação do dólar e da média móvel de 10 dias

    - Salvar o gráfico em dags/reports/relatorio_dolar.png

### Requisitos Técnicos

- Utilizar PythonOperator para cada tarefa

- Utilizar yfinance ou pandas_datareader para extração

- Utilizar pandas e matplotlib nas etapas de transformação e visualização

- O pipeline deve estar agendado com @daily, mas ser testado via Trigger DAG

### Estrutura Esperada

```text
airflow_custom_project/
├── dags/
│   └── etl_dolar_brl.py
├── docker-compose.yaml
├── Dockerfile
├── requirements.txt
```

### Entregáveis

- Arquivo etl_dolar_brl.py funcionando na interface do Airflow

- Screenshot da DAG executada com sucesso

- Arquivo relatorio_dolar.png gerado
