import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd
import os 


SNOWFLAKE_USER = "JOAO"
SNOWFLAKE_PASSWORD = "#Hans3030@8802"
SNOWFLAKE_ACCOUNT = "NQCMSZC-FNB67628"  # exemplo: abcd-xy12345
SNOWFLAKE_WAREHOUSE = "COMPUTE_WH"
SNOWFLAKE_DATABASE = "DATASUS"
SNOWFLAKE_SCHEMA = "PUBLIC"
STAGE_NAME = "DO_DATA"
CSV_DIR = "Csv_files"


conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA
)


cur = conn.cursor()

#testando a conexao 
try:
    cur.execute("SELECT CURRENT_VERSION()")
    version = cur.fetchone()[0]
    print(f"Conexão OK! Versão do Snowflake: {version}")
    
except Exception as e:
    print("Erro na conexão:", e)


try:
    # Lista todos os arquivos csv no diretório
    arquivos_csv = [f for f in os.listdir(CSV_DIR) if f.endswith(".csv")]
    if not arquivos_csv:
        print("Nenhum arquivo .csv encontrado.")
    else:
        for arquivo in arquivos_csv:
            caminho_arquivo = os.path.join(CSV_DIR, arquivo)
            print(f"Enviando {caminho_arquivo} para o stage {STAGE_NAME}...")
            
            #Comando PUT para enviar o arquivo para o stage
            cur.execute(f"PUT file://{caminho_arquivo} @{STAGE_NAME}")

        print("Upload concluído com sucesso.")


finally:
    cur.close()
    conn.close()

