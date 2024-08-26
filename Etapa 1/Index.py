import requests
from bs4 import BeautifulSoup
import pandas as pd
import yfinance as yf
import logging
import os

def setup_logging(log_filename):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )

def extract_sp500_companies(url):
    req = requests.get(url)
    if req.status_code == 200:
        print("Solicitud exitosa.")
        soup = BeautifulSoup(req.text, 'html.parser')
        data = soup.find_all("table")[0]
        df_sp500 = pd.read_html(str(data))[0]
        return df_sp500
    else:
        print(f"Error en la solicitud: {req.status_code}")
        return None

def extract_data(ticker, start_date, end_date):
    try:
        logging.info(f'Extrayendo datos para {ticker} desde {start_date} hasta {end_date}')
        data = yf.download(ticker, start=start_date, end=end_date)
        logging.info(f'Datos extraídos exitosamente para {ticker}')
        return data
    except Exception as e:
        logging.error(f'Error extrayendo datos para {ticker}: {e}')
        return None

def transform_data(data):
    try:
        logging.info('Transformando datos')
        df = data[['Adj Close']].reset_index()
        df.rename(columns={'Date': 'ds', 'Adj Close': 'y'}, inplace=True)
        logging.info('Datos transformados exitosamente')
        return df
    except Exception as e:
        logging.error(f'Error transformando datos: {e}')
        return None

def load_data(df, ticker):
    try:
        filename = os.path.join(data_dir, f'{ticker}_processed.csv')
        logging.info(f'Guardando datos transformados en {filename}')
        df.to_csv(filename, index=False)
        logging.info('Datos guardados exitosamente')
    except Exception as e:
        logging.error(f'Error guardando datos: {e}')

def etl_process(ticker, start_date, end_date):
    data = extract_data(ticker, start_date, end_date)
    if data is not None:
        transformed_data = transform_data(data)
        if transformed_data is not None:
            load_data(transformed_data, ticker)
            return transformed_data
    return None

log_dir = 'logs'
data_dir = 'data'
os.makedirs(log_dir, exist_ok=True)
os.makedirs(data_dir, exist_ok=True)

log_filename = os.path.join(log_dir, 'etl_process.log')
setup_logging(log_filename)

url = "https://es.wikipedia.org/wiki/Anexo:Compa%C3%B1%C3%ADas_del_S%26P_500"

df_sp500 = extract_sp500_companies(url)
if df_sp500 is not None:
    csv_filename = os.path.join(data_dir, 'SP500.csv')
    df_sp500.to_csv(csv_filename, index=None, header=True)
    csv_filepath = os.path.abspath(csv_filename)
    print(f'La tabla ha sido extraída y guardada como: {csv_filepath}')
    print(df_sp500.head())
    print(df_sp500.columns)

start_date = '2022-11-01'
end_date = '2023-02-28'

if df_sp500 is not None:
    tickers = df_sp500['Símbolo'].tolist()
    for ticker in tickers[:5]:
        print(f'Procesando {ticker}')
        data = etl_process(ticker, start_date, end_date)
