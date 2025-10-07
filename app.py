from flask import Flask, render_template

app = Flask(__name__)

# Dados para passar às páginas
dados = {
    
    "nome": "Julia Emanuelly da Silva Costa",
    "bio": """Oi! Eu sou a Júlia Emanuelly da Silva Costa, tenho 18 anos e gosto de aprender coisas novas todos os dias.
Gosto de criar, testar ideias e ver as coisas acontecerem na prática. Cada projeto é uma oportunidade de fazer diferente e melhorar um pouco mais.Estou começando uma nova fase e quero aproveitar cada oportunidade para aprender e criar coisas do meu jeito.""",
    "educacao": [
        {"ano": "2022 - 2024", "curso": "Ensino Médio Técnico em Energias Renováveis", "instituicao": "Senai - Civit"},
        {"ano": "2022", "curso": "Curso de AutoCAD", "instituicao": "Senai - Civit"},
        {"ano": "2024 - 2026", "curso": "Desenvolvimento de Sistemas", "instituicao": "Senai - Civit"},
        {"ano": "2025 - 2030", "curso": "Direito", "instituicao": "Faculdade Multivix"}
    ],
    "projetos": [
        {"titulo": "Sistema de Login", "descricao": "Um sistema de login para autenticação de usuários.", "imagem": "login.jpg"},
        {"titulo": "Implementação BFS", "descricao": "Algoritmo de busca em largura (BFS).", "imagem": "bfs.jpg"},
        {"titulo": "Cenário", "descricao": "Atividade de criação de cenário com elementos gráficos variados.", "imagem": "cenario.jpg"},
        {"titulo": "Jogo de Sinuca", "descricao": "Jogo de sinuca desenvolvido no Unity.", "imagem": "sinuca.jpg"}
    ]
}

@app.route("/")
def index():
    return render_template("index.html", dados=dados)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html", dados=dados)

@app.route("/projetos")
def projetos():
    return render_template("projetos.html", dados=dados)

@app.route("/contato")
def contato():
    return render_template("contato.html", dados=dados)

if __name__ == "__main__":
    app.run(debug=True)
