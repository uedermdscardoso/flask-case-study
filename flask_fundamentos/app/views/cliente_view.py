from flask import render_template, redirect, url_for, request

from app.forms import cliente_form

from app import app, db  #diretório do projeto
from app.models import cliente_model


@app.route("/")
def default():
    return "Página raiz"

@app.route("/ola")
def ola():
    return "Olá, mundo em flask!!"

@app.route("/outro")
def other():
    return "Outro"

@app.route("/show", defaults={'name': None}, methods={"POST","GET"})
@app.route("/show/<string:name>") #string, int, float, path, uuid
def showUserName(name):
    if name:
        return f"Olá, {name}"
    else:
        return "Olá, usuário"

@app.route("/page", defaults={'name':None}, methods={"GET"})
@app.route("/page/<string:name>", methods={"GET"})
def showPage(name):
    return render_template("clientes/teste.html", nome_usuario=name)


#Forms
@app.route('/cadastrar_cliente', methods={'GET','POST'})
def cadastrar_cliente():
    form = cliente_form.ClienteForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        genero = form.genero.data

        cliente = cliente_model.Cliente(nome=nome, email=email, data_nascimento=data_nascimento, profissao=profissao, genero=genero)
        try:
            db.session.add(cliente) #Adicionando na sessão
            db.session.commit()
            return redirect('listar_clientes') #url_for('listar_clientes')
        except IndexError as e:
            print('Cliente não cadastrado')

    return render_template('clientes/form.html', form=form)

@app.route('/listar_clientes', methods={'GET'})
def listarClientes():
    clientes = cliente_model.Cliente.query.all()
    return render_template('clientes/lista_clientes.html', clientes=clientes)

@app.route('/listar_cliente/<int:id>', methods={'GET'})
def listarCliente(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    return render_template('clientes/lista_cliente.html', cliente=cliente)

@app.route('/editar_cliente/<int:id>', methods={'GET','POST'})
def editarCliente(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    form = cliente_form.ClienteForm(obj=cliente)
    form.genero.data = cliente.genero
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        genero = form.genero.data

        cliente.nome = nome
        cliente.email = email
        cliente.data_nascimento = data_nascimento
        cliente.profissao = profissao
        cliente.genero = genero

        try:
            db.session.commit()
            return redirect('/listar_clientes')  # url_for('listar_clientes')
        except:
            print('O cliente não foi editado')
    return render_template('clientes/form.html', form=form)

@app.route('/remover_cliente/<int:id>', methods={'GET','POST'})
def removerCliente(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    if request.method == 'POST':
        try:
            db.session.delete(cliente)
            db.session.commit()
            return redirect('/listar_clientes')
        except:
            print('Erro ao remover o cliente')
    return render_template('clientes/remover_cliente.html', cliente=cliente)
