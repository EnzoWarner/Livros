# Chatbot Assistente de Livros
Este projeto é um chatbot em Python que utiliza a API do GroqCloud para buscar informações sobre livros. Ele permite que o usuário faça até três perguntas sobre livros e, ao final, exibe um resumo das respostas.

# Requisitos
Antes de executar o chatbot, certifique-se de ter o seguinte instalado:
- Python 3.7 ou superior
- Bibliotecas necessárias:
- requests
- python-dotenv

# Instalação
Clone este repositório ou baixe os arquivos do projeto.
- Instale as dependências executando os seguintes comandos no terminal:
- pip install requests
- pip install python-dotenv

# Configuração da API
Crie uma conta no GroqCloud e gere uma chave de API.
https://console.groq.com/keys
- No diretório do projeto, crie um arquivo .env e cole o seguinte conteúdo:
- GROQCLOUD_API_KEY=Colar a chave aqui

# Execução do Chatbot
- Após configurar o ambiente, execute o seguinte comando no terminal para iniciar o chatbot:
- python chatbot.py

# Funcionamento
O chatbot solicitará que o usuário informe o título de um livro.
Ele buscará informações sobre o livro e retornará um resumo.
Após três interações, um resumo final com os títulos, autores e gêneros será exibido.

# Exemplo de Uso

Assistente de Livros
Assistente: Olá, sou um assistente bibliotecário e posso ajudar fazendo resumos de livros para você :).
Informe o título de um livro se desejar.

Usuário: 1984
Assistente: 1984, de George Orwell, é um romance distópico que explora temas de vigilância e controle governamental.

Usuário: Dom Casmurro
Assistente: Dom Casmurro, de Machado de Assis, é um clássico da literatura brasileira que narra a história de Bentinho e seu ciúme por Capitu.

Usuário: O Pequeno Príncipe
Assistente: O Pequeno Príncipe, de Antoine de Saint-Exupéry, é uma fábula filosófica sobre amizade e amor.

Resumo das suas perguntas:
Assistente:
 1. Título: 1984, Autor: George Orwell, Gênero: Distopia
 2. Título: Dom Casmurro, Autor: Machado de Assis, Gênero: Romance
 3. Título: O Pequeno Príncipe, Autor: Antoine de Saint-Exupéry, Gênero: Fábula




