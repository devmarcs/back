from app import db
from flask import render_template, Blueprint;

# ####################
# Cada classe é uma tabela no banco de dados
# ####################

#Casa herda todas as características de db.Model
class Casa(db.Model):

    #Propriedades de Casa
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qtdQuartos = db.Column(db.Integer)
    qtdBanheiros = db.Column(db.Integer)
    rua = db.Column(db.String(100))

    #Construtor, recebendo os parâmetros para adicionar ao objeto
    def __init__(self, qtdQuartos, qtdBanheiros, rua):
        self.qtdQuartos = qtdQuartos
        self.qtdBanheiros = qtdBanheiros
        self.rua = rua

class Atividade(db.Model):
    id_atividade = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    status = db.Column(db.String)

    def __init__(self, id_atividade, nome, status):
        self.id_atividade=id_atividade
        self.nome=nome
        self.status=status

