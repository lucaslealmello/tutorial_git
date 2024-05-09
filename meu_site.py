from  flask import Flask, render_template


app = Flask (__name__)

# criar a primeira pagina do site 
# route -> hastagtreinamentos.com/
# função -> o que voçê quer exibir naquela página
# templete
@app.route("/")
def homepage():
   return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuarios>")
def usuarios(nome_usuario):
    return nome_usuario
# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) 