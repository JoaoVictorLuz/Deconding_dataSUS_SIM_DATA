import snowflake.connector
import os
import pandas as pd

DIRETORIO = "Csv_files"
SNOWFLAKE_USER = "JOAO"
SNOWFLAKE_PASSWORD = "#Hans3030@8802"
SNOWFLAKE_ACCOUNT = "NQCMSZC-FNB67628"
SNOWFLAKE_WAREHOUSE = "COMPUTE_WH"
SNOWFLAKE_DATABASE = "DATASUS"
SNOWFLAKE_SCHEMA = "PUBLIC"
SNOWFLAKE_ROLE = "ACCOUNTADMIN"



# Conexão Snowflake
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA,
    role=SNOWFLAKE_ROLE
)
cur = conn.cursor()

# Testando conexão
try:
    cur.execute("SELECT CURRENT_VERSION()")
    version = cur.fetchone()[0]
    print(f"Conexão OK! Versão do Snowflake: {version}")
except Exception as e:
    print("Erro na conexão:", e)



nomes_e_dfs = []

# Lista arquivos CSV
arquivos_csv = [f for f in os.listdir(DIRETORIO) if f.lower().endswith(".csv")]
print("Arquivos encontrados:", arquivos_csv)


for nome_arquivo in arquivos_csv:
    caminho_arquivo = os.path.join(DIRETORIO, nome_arquivo)
    
    df = pd.read_csv(caminho_arquivo, nrows=1)  # lê apenas o cabeçalho
    nome_tabela = os.path.splitext(nome_arquivo)[0]
    
    colunas_sql = ", ".join([f"{col} VARCHAR(50)" for col in df.columns])
    query = f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({colunas_sql})"
    cur.execute(query)
    print(f"Tabela '{nome_tabela}' criada com sucesso")
    

cur.close()
conn.close()


