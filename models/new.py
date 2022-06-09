from database import db

class User(db.Model):
    __tablename__='NewUser'
    id= db.Column(db.Integer, primary_key=True)
    nome= db.Column(db.String(200))
    email= db.Column(db.String(200))
    contato= db.Column(db.String(12))
    senha= db.Column(db.String(50))
    

    def __init__(self, nome, contato, email, senha):
        self.nome= nome
        self.email= email
        self.contato= contato
        self.senha= senha
        
