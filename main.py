import pandas as pd
import os
import warnings

# Suprimindo avisos da biblioteca openpyxl
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

def verifica_imagens(arquivo_relatorio, diretorio_saida):
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

    # Cria o diretório de saída se não existir
    os.makedirs(diretorio_saida, exist_ok=True)

    # Salva o arquivo modificado
    novo_arquivo = f"verificado_{os.path.basename(arquivo_relatorio)}"
    caminho_saida = os.path.join(diretorio_saida, novo_arquivo)
    if arquivo_relatorio.endswith('.csv'):
        df.to_csv(caminho_saida, index=False)
    elif arquivo_relatorio.endswith('.xlsx'):
        df.to_excel(caminho_saida, index=False)

    print(f"As informações sobre a existência das imagens foram adicionadas ao arquivo '{caminho_saida}'.")

# Diretório onde estão localizados os relatórios
diretorio_relatorios = 'caminho/para/seu/diretorio'
diretorio_saida = 'caminho/para/seu/diretorio/de/saida'

# Itera sobre os arquivos no diretório
for arquivo in os.listdir(diretorio_relatorios):
    if arquivo.endswith('.csv') or arquivo.endswith('.xlsx'):
        caminho_arquivo = os.path.join(diretorio_relatorios, arquivo)
        verifica_imagens(caminho_arquivo, diretorio_saida)
