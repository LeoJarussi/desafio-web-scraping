import os
import requests
from bs4 import BeautifulSoup
import zipfile

print("O código começou a rodar...")

def baixar_pdfs_e_zipar():
    # URL da página onde estão os PDFs
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    
    # Faz a requisição para pegar o conteúdo da página
    resposta = requests.get(url)
    resposta.raise_for_status() 
    
    # Analisa o HTML da página
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # Encontra todos os links da página
    links = soup.find_all('a', href=True)
    
    # Filtra os links que contêm "Anexo I" e "Anexo II"
    pdf_links = []
    for link in links:
        href = link['href']
        if "Anexo-I" in href or "Anexo-II" in href:
            pdf_links.append(href)
    
    # Criar pasta para salvar os PDFs
    os.makedirs("downloads", exist_ok=True)
    
    # Baixar os PDFs
    pdf_paths = []
    for pdf_link in pdf_links:
        pdf_url = pdf_link if pdf_link.startswith("http") else url + pdf_link
        pdf_nome = pdf_url.split("/")[-1]
        pdf_caminho = os.path.join("downloads", pdf_nome)
        
        print(f"Baixando {pdf_nome}...")
        pdf_resposta = requests.get(pdf_url)
        pdf_resposta.raise_for_status()
        
        with open(pdf_caminho, "wb") as pdf:
            pdf.write(pdf_resposta.content)
        
        pdf_paths.append(pdf_caminho)
    
    # Criar um arquivo ZIP com os PDFs
    zip_path = "downloads/anexos.zip"
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for pdf in pdf_paths:
            zipf.write(pdf, os.path.basename(pdf))
    
    print("Download e compactação concluídos! Arquivo salvo em:", zip_path)

# Executar a função
baixar_pdfs_e_zipar()