from airflow import DAG # type: ignore
from airflow.operators.python import PythonOperator # type: ignore
from datetime import datetime
import pandas as pd # type: ignore
import yfinance as yf # type: ignore
import os
import matplotlib.pyplot as plt # type: ignore

DATA_PATH = '/opt/airflow/dags/data/'
REPORT_PATH = '/opt/airflow/dags/reports/'

os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(REPORT_PATH, exist_ok=True)

def extrair():
    df = yf.download('USDBRL=X', start='2023-01-01', end='2023-12-31')
    df.to_csv(f"{DATA_PATH}/dolar_raw.csv")

def transformar():
    df = pd.read_csv(f"{DATA_PATH}/dolar_raw.csv", index_col=0)
    df = df.dropna()
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df['Media_Movel_10'] = df['Close'].rolling(window=10).mean()
    df.to_csv(f"{DATA_PATH}/dolar_tratado.csv")

def gerar_relatorio():
    df = pd.read_csv(f"{DATA_PATH}/dolar_tratado.csv")
    plt.figure(figsize=(10, 6))
    plt.plot(df['Close'], label='Fechamento')
    plt.plot(df['Media_Movel_10'], label='Média Móvel 10 dias')
    plt.legend()
    plt.title('USDBRL - Fechamento vs Média Móvel 10 dias')
    plt.savefig(f"{REPORT_PATH}/relatorio_dolar.png")

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False
}

with DAG("etl_dolar_brl",
         schedule_interval="@daily",
         default_args=default_args,
         description="Pipeline da cotação do dólar (USDBRL) com média móvel",
         tags=["etl", "dolar", "financeiro"]) as dag:

    t1 = PythonOperator(
        task_id="extrair_dados",
        python_callable=extrair
    )

    t2 = PythonOperator(
        task_id="transformar_dados",
        python_callable=transformar
    )

    t3 = PythonOperator(
        task_id="gerar_relatorio",
        python_callable=gerar_relatorio
    )

    t1 >> t2 >> t3