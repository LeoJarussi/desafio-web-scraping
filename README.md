Desafio de Web Scraping

Descrição

Este projeto é um desafio técnico para realizar Web Scraping e manipulação de arquivos. O código acessa um site do governo, baixa documentos PDF específicos e os compacta em um arquivo ZIP.

Tecnologias Utilizadas

Python 3.x

Requests

BeautifulSoup4

Zipfile

Como Rodar o Projeto

Clonar o repositório:

git clone https://github.com/seu_usuario/desafio-web-scraping.git
cd desafio-web-scraping

Criar um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

Instalar as dependências:

pip install -r requirements.txt

Executar o script:

python scraper.py

Estrutura do Projeto

/
├── downloads/         # Pasta onde serão salvos os PDFs e o ZIP
├── scraper.py         # Script principal
├── README.md          # Documentação do projeto
└── requirements.txt   # Lista de dependências

Resultado

Ao rodar o script, os arquivos "Anexo I" e "Anexo II" serão baixados e compactados dentro da pasta downloads/anexos.zip.

Contato

Caso tenha alguma dúvida, entre em contato pelo meu linkedin https://www.linkedin.com/in/leonardo-jarussi-03b0b32b7/.