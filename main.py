import pandas as pd
import os

def verifica_imagens(arquivo_relatorio, pasta_relatorio):
    # Verifica se o arquivo é CSV ou XLSX
    if arquivo_relatorio.endswith('.csv'):
        try:
            df = pd.read_csv(os.path.join(pasta_relatorio, arquivo_relatorio))
        except FileNotFoundError:
            print("Arquivo CSV não encontrado.")
            return
    elif arquivo_relatorio.endswith('.xlsx'):
        try:
            df = pd.read_excel(os.path.join(pasta_relatorio, arquivo_relatorio))
        except FileNotFoundError:
            print("Arquivo XLSX não encontrado.")
            return
    else:
        print("Formato de arquivo não suportado.")
        return

    # Adiciona uma coluna para indicar se a imagem existe ou não
    df['Imagem Existe'] = df['Caminho da Imagem'].apply(lambda path: os.path.exists(path))

    # Salva o arquivo modificado
    novo_arquivo = f"verificado_{arquivo_relatorio}"
    if arquivo_relatorio.endswith('.csv'):
        df.to_csv(os.path.join(pasta_relatorio, novo_arquivo), index=False)
    elif arquivo_relatorio.endswith('.xlsx'):
        df.to_excel(os.path.join(pasta_relatorio, novo_arquivo), index=False)

    print(f"As informações sobre a existência das imagens foram adicionadas ao arquivo '{novo_arquivo}'.")

# Exemplo de uso
nome_arquivo_relatorio = input("Digite o nome do arquivo CSV ou XLSX do relatório: ")
pasta_relatorio = input("Digite o caminho da pasta do relatório: ")
verifica_imagens(nome_arquivo_relatorio, pasta_relatorio)
