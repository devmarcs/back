from flask import request, jsonify, make_response, render_template, redirect, url_for
from app import app, db
from sqlalchemy.exc import IntegrityError
from datetime import datetime

#Importa os modelos que vamos usar
from app.models.modelos import Casa
from app.models.modelos import Atividade
#CRUD
# Create -> Cria recurso -> POST
# Read -> Ler os recursos -> GET
# Update -> Atualiza um recurso -> PUT
# Delete -> Apaga um recurso -> DELETE

@app.route("/")
def index():
    return render_template('/menu.html')
# Read
#Rota que lista todas as casas existes
@app.route("/casa", methods=['GET'])
def get_casas():
    casas = Casa.query.all()
    lista_casas = []
    for casa in casas:
        lista_casas.append({
            'id': casa.id,
            'qtdQuartos': casa.qtdQuartos,
            'qtdBanheiros': casa.qtdBanheiros,
            'rua': casa.rua
            })

    return jsonify(lista_casas)

#Create
# Cria uma casa no banco de dados
@app.route("/casa", methods=['POST'])
def create_casa():
    dados = request.json
    _qtdQuartos = dados["qtdQuartos"]
    _qtdBanheiros = dados["qtdBanheiros"]
    _rua = dados["rua"]

    casa = Casa(qtdQuartos=_qtdQuartos, qtdBanheiros=_qtdBanheiros, rua=_rua)
    db.session.add(casa)
    db.session.commit()
    return jsonify({'status': 201, 'message': 'Casa criada com sucesso'}), 201

@app.route('/novaAtividade', methods=['POST', 'GET'])
def novaAtividade():
   
    if request.method=='POST':
   
        nome = request.form['nomeAtividade']
        status = request.form['status']

        atividade = Atividade(id_atividade=5, nome =nome, status=status)
        db.session.add(atividade)
        db.session.commit()
        return redirect('/listaAtividade')
        #return jsonify({'status': 201, 'message': 'Atividade criada com sucesso'}), 201
   
    return render_template('/atividade.html')

@app.route('/listaAtividade', methods=["GET"])
def listaAtividade():
    atividades = Atividade.query.all()
    for i in atividades:
        print(i.id_atividade, i.nome, i.status)
    
    return render_template("/atividade.html", atividades=atividades)
