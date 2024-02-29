import pandas as pd
import os
import logging

# Configuração para suprimir avisos da biblioteca openpyxl
logging.getLogger('openpyxl').setLevel(logging.ERROR)

def verifica_imagens(arquivo_relatorio):
    # Verifica se o arquivo é CSV ou XLSX
    if arquivo_relatorio.endswith('.csv'):
        try:
            df = pd.read_csv(arquivo_relatorio)
        except FileNotFoundError:
            print(f"Arquivo CSV '{arquivo_relatorio}' não encontrado.")
            return
    elif arquivo_relatorio.endswith('.xlsx'):
        try:
            df = pd.read_excel(arquivo_relatorio)
        except FileNotFoundError:
            print(f"Arquivo XLSX '{arquivo_relatorio}' não encontrado.")
            return
    else:
        print(f"Formato de arquivo '{arquivo_relatorio}' não suportado.")
        return

    # Adiciona uma coluna para indicar se a imagem existe ou não
    df['Imagem Existe'] = df['Caminho da Imagem'].apply(lambda path: os.path.exists(path))

    # Salva o arquivo modificado
    novo_arquivo = f"verificado_{arquivo_relatorio}"
    if arquivo_relatorio.endswith('.csv'):
        df.to_csv(novo_arquivo, index=False)
    elif arquivo_relatorio.endswith('.xlsx'):
        df.to_excel(novo_arquivo, index=False)

    print(f"As informações sobre a existência das imagens foram adicionadas ao arquivo '{novo_arquivo}'.")

# Diretório onde estão localizados os relatórios
diretorio_relatorios = 'caminho/para/seu/diretorio'

# Itera sobre os arquivos no diretório
for arquivo in os.listdir(diretorio_relatorios):
    if arquivo.endswith('.csv') or arquivo.endswith('.xlsx'):
        caminho_arquivo = os.path.join(diretorio_relatorios, arquivo)
        verifica_imagens(caminho_arquivo)
