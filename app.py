from database import db
from models.new import User
from flask import Flask, render_template, request 

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///NewUser.db'
app.config['SQLACHEMY_TRACK_NOTIFICATIONS']= False

@app.before_first_request
def create_db():
    db.create_all()


@app.route('/')
def index():
    return render_template('indexx.html')    


@app.route('/submit', methods=['POST'])
def confirmar():
    if request.method == 'POST':
        nome= request.form['nome']
        contato= request.form['contato']
        email= request.form['email']
        senha= request.form['senha']       
        #print(nome, contato, email, senha)    
        if nome == '' or email == '':
            return render_template('indexx.html')
        if db.session.query(User).filter(User.nome==nome).count() == 0:
            data= User(nome, contato, email, senha)
            db.session.add(data)
            db.session.commit()

        return render_template('confirma.html')


if __name__ == '__main__':
    from database import db
    db.init_app(app)                
    app.run()    