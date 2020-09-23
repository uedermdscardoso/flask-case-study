from flask import render_template, redirect, url_for, request

from app.forms import cliente_form

from app import app, db  #diretório do projeto
from app.models import cliente_model
from app.entidades import cliente
from app.services import cliente_service

#Refatorado

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
            cliente_service.cadastrarCliente(cliente)
            return redirect('listar_clientes') #url_for('listar_clientes')
        except IndexError as e:
            print('Cliente não cadastrado')

    return render_template('clientes/form.html', form=form)

@app.route('/listar_clientes', methods={'GET'})
def listarClientes():
    clientes = cliente_service.listarClientes()
    return render_template('clientes/lista_clientes.html', clientes=clientes)

@app.route('/listar_cliente/<int:id>', methods={'GET'})
def listarCliente(id):
    cliente = cliente_service.listarClientePorId(id)
    return render_template('clientes/lista_cliente.html', cliente=cliente)

@app.route('/editar_cliente/<int:id>', methods={'GET','POST'})
def editarCliente(id):
    cliente_bd = cliente_service.listarClientePorId(id)
    form = cliente_form.ClienteForm(obj=cliente_bd)
    form.genero.data = cliente_bd.genero
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        genero = form.genero.data

        cliente_novo = cliente.Cliente(nome=nome, email=email, data_nascimento=data_nascimento, profissao=profissao,
                                       genero=genero)

        try:
            cliente_service.editarCliente(cliente_bd, cliente_novo)
            return redirect('/listar_clientes')  # url_for('listar_clientes')
        except:
            print('O cliente não foi editado')
    return render_template('clientes/form.html', form=form)

@app.route('/remover_cliente/<int:id>', methods={'GET','POST'})
def removerCliente(id):
    cliente = cliente_service.listarClientePorId(id)
    if request.method == 'POST':
        try:
            cliente_service.removerCliente(cliente)
            return redirect('/listar_clientes')
        except:
            print('Erro ao remover o cliente')
    return render_template('clientes/remover_cliente.html', cliente=cliente)
