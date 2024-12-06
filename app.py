import models
import services
import services.book_services
import services.user_services
import db, utils


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/listarlivros", methods=['GET']) 
def listar_livros():
        livros = db.consultar_livros()
        return jsonify(livros)

@app.route("/cadastrarlivro", methods=['POST']) 
def cadastrar():
    services.book_services.cadastra_livro()

@app.route("/listarusuarios", methods=['GET']) 
def lista_usuarios():
    usuarios = db.consultar_clientes()
    return jsonify(usuarios)

@app.route("/cadastrarusuario", methods=['POST']) 
def cadastra():
    services.user_services.cadastrar_usuario()


@app.route("/exibirlivrosemprestadosporusuario", methods=['POST'])
def listar_emprestados():
    services.book_services.lista_livros_emprestados_usuario()

@app.route("/emprestarlivro", methods=["POST"])
def empresta():
    services.book_services.emprestar_livro_para_usuario()

    

@app.route("/devolverlivro", methods=['POST']) 
def devolver():
    services.book_services.devolver_livro_emprestado()

@app.route("/buscarlivro", methods=['POST']) 
def busca():
    services.book_services.buscar_livro()

    
@app.route("/deletalivro", methods=["POST"]) 
def deleta():
    services.book_services.deleta_livro()

if __name__ == '__main__':
    app.run()