import requests
import time
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

API_KEY = os.getenv('GROQCLOUD_API_KEY')
API_URL = 'https://api.groq.com/openai/v1/chat/completions'  # Atualize a URL conforme a documentação

# Verificar se a chave de API foi carregada corretamente
if not API_KEY:
    print("Erro: Chave de API não encontrada. Verifique o arquivo .env.")
    exit()

def obter_informacoes_livro(nome_livro, tipo="completo"):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    prompt = (f"Me dê informações sobre o livro {nome_livro} em no máximo três linhas" 
             if tipo == "completo" 
             else f"Me dê apenas o título, autor e gênero do livro {nome_livro}.")
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if 'choices' in data and len(data['choices']) > 0:
                resposta = data['choices'][0]['message']['content']
                # Adiciona quebras de linha após pontos finais para melhorar a formatação
                resposta_formatada = resposta.replace('. ', '.\n')
                return resposta_formatada.strip()
            else:
                return "Nenhuma informação encontrada."
        else:
            print(f"Erro: {response.text}")
            return "Erro ao acessar a API do GroqCloud."
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return "Erro de conexão ao acessar a API do GroqCloud."

def main():
    print("Assistente de Livros")
    print("Assistente: Olá, sou um assistente bibliotecário e posso ajudar fazendo resumos de livros para você :). \n Informe o título de um livro se desejar.")
    
    respostas = []
    resumos = []
    
    for i in range(3):
        nome_livro = input(f"Usuário: ")
        # Obtém resposta completa
        informacoes = obter_informacoes_livro(nome_livro, "completo")
        respostas.append(informacoes)
        print(f"\nAssistente: {informacoes}\n")  # Adicionada quebra de linha antes e depois
        
        # Obtém informações resumidas para o resumo final
        info_resumida = obter_informacoes_livro(nome_livro, "resumido")
        detalhes = info_resumida.split('\n')
        
        # Procura pelas informações relevantes nas linhas
        titulo = ""
        autor = ""
        genero = ""
        
        for linha in detalhes:
            linha = linha.strip().lower()
            if "título:" in linha:
                titulo = linha.split(":", 1)[1].strip()
            elif "autor:" in linha:
                autor = linha.split(":", 1)[1].strip()
            elif "gênero:" in linha:
                genero = linha.split(":", 1)[1].strip()
        
        # Remove possíveis textos extras
        titulo = titulo.replace('"', '').replace('- ', '')
        autor = autor.replace('autor: ', '')
        genero = genero.replace('gênero: ', '')
        
        if titulo and autor and genero:
            resumos.append(f"Título: {titulo}, Autor: {autor}, Gênero: {genero}")
        time.sleep(1)
    
    print("\nResumo das suas perguntas:")
    print("\nAssistente:")
    if resumos:
        for idx, resumo in enumerate(resumos, 1):
            print(f" {idx}. {resumo}")

if __name__ == "__main__":
    main()

