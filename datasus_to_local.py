import pandas as pd
from pysus import SIM
from pysus.preprocessing.decoders import translate_variables_SIM
#from pysus.preprocessing.decoders import decodifica_sim
from pysus.online_data.SIM import get_CID9_table, get_CID10_table, get_municipios, get_ocupations
#from pysus.online_data.SIM import ge
sim = SIM().load()
import pandas as pd


lista_de_arquivos = sim.get_files("CID10", uf="BR")
print(len(lista_de_arquivos))
total_de_arquivos_baixados = 0


for ftp_file in lista_de_arquivos:
    try:
        sim.download(ftp_file, local_dir='/home/joao/pysus/projeto/Parquet_files')
        total_de_arquivos_baixados += 1
    except Exception as e:
        print(f"Erro ao baixar {ftp_file}: {e}")
        continue

print(f"Total de arquivos: {len(lista_de_arquivos)}")
print(f"Total de arquivos baixados: {total_de_arquivos_baixados}")

