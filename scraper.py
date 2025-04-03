import os
import requests
from bs4 import BeautifulSoup
import zipfile

print("O código começou a rodar")

def baixar_pdfs_e_zipar():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    
    resposta = requests.get(url)
    resposta.raise_for_status() 
    soup = BeautifulSoup(resposta.text, 'html.parser')
    links = soup.find_all('a', href=True)
    
    pdf_links = []
    for link in links:
        href = link['href']
        if "Anexo-I" in href or "Anexo-II" in href:
            pdf_links.append(href)
    
    os.makedirs("downloads", exist_ok=True)
    
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

    zip_path = "downloads/anexos.zip"
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for pdf in pdf_paths:
            zipf.write(pdf, os.path.basename(pdf))
    
    print("Download e compactação concluídos! Arquivo salvo em:", zip_path)

baixar_pdfs_e_zipar()
