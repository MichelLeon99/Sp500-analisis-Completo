from sqlalchemy import create_engine
import pyodbc
import pandas as pd

server = 'MIKE\\SQLEXPRESS'
database = 'SP500'
username = 'Mleon'
password = 'MLWHSw99?'
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'


engine = create_engine(connection_string)


companies_df = pd.read_csv(r'D:\Bootcamp\proyecto\Etapa 1\data\Precios de las empresas')
company_profiles_df = pd.read_csv(r'D:\Bootcamp\Proyecto\Etapa 1\data\Lista de empresas')


companies_df.to_sql('Companies', engine, if_exists='replace', index=False)
company_profiles_df.to_sql('CompanyProfiles', engine, if_exists='replace', index=False)


conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
cursor = conn.cursor()

cursor.close()
conn.close()
