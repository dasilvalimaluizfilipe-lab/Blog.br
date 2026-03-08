from flask import Flask

app = Flask(__name__)

posts = [
    {"titulo": "Meu primeiro post", "conteudo": "Este é meu primeiro blog em Python."},
    {"titulo": "Aprendendo Python", "conteudo": "Python é uma linguagem muito poderosa."},
]

@app.route("/")
def home():
    html = "<h1>Meu Blog</h1>"

    for post in posts:
        html += f"<h2>{post['titulo']}</h2>"
        html += f"<p>{post['conteudo']}</p>"
        html += "<hr>"

    return html

app.run(debug=True)
