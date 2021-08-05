from flask import Flask, render_template, url_for, redirect
import names
from random import choice, randint
import string
import datetime

app = Flask(__name__)

def generate_random_person():
  
  paises = ['China', 'India', 'Estados Unidos', 'Indonesia', 'Paquistao', 'Brasil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico']
  opt = ['Empregado(a)', 'Desempregado(a)']
  empregado_ou_desempregado = choice(opt) 
  nome = names.get_full_name()
  estado_civil = ['Casado(a)', 'Solteiro(a)']
  idade_max = randint(60, 70)
  idade = randint(18, idade_max)
  profissão_ou_estudo = ['Medicina', 'Direito', 'Engenharia Civil', 'Arquitetura e Urbanismo', 'Relacoes Internacionais', 'Publicidade e Propaganda', 'Fisioterapia', 'Psicologia', 'Ciencia da Computacao', 'Nutricao', 'Historia', 'Matematica', 'Fisica', 'Ciencia']

  def data_de_nascimento():

    ano_atual = datetime.date.today()
    data = ano_atual.year - idade

    return f'Ano de nascimento: {str(data)}'

  def generate_email():
    
    extensões_de_email = ['@gmail.com', '@outlook.com', '@hotmail.com']
    email = ''
    email += nome
    opt2 = ['-', '.']
    email += choice(opt2)
    caracteres = string.ascii_letters
    caracteres += string.digits
    for i in range(randint(1, 5)):
      email += choice(caracteres)
    email += choice(extensões_de_email)

    return email.replace(' ', '.')
  
  def generate_password():
    
    senha = ''
    senha_chars = string.ascii_letters
    senha_chars += string.digits
    senha_chars += '!@#$%¨&*()_+{}?:><[].,;'
    for g in range(randint(8, 12)):
      senha += choice(senha_chars)
    
    return senha

  resposta_pronta = { 'nome': nome, 'email': generate_email(), 'idade': idade, 'senha': generate_password(), 'estado_civil': choice(estado_civil), 'trabalha_ou_estuda_com': choice(profissão_ou_estudo), 'empregado_ou_desempregado': empregado_ou_desempregado, 'localizacao': choice(paises), 'ano_de_nascimento': data_de_nascimento() }


  if empregado_ou_desempregado == 'Desempregado(a)':
    resposta_pronta = { 'nome': nome, 'email': generate_email(), 'idade': idade, 'senha': generate_password(), 'estado_civil': choice(estado_civil), 'trabalha_ou_estuda_com': None, 'empregado_ou_desempregado': empregado_ou_desempregado, 'localizacao': choice(paises), 'ano_de_nascimento': data_de_nascimento() }
  
  return resposta_pronta

@app.route('/')
def index():
  try:
    return render_template('index.html')
  except:
    return redirect('/error')

@app.route('/api', methods=['GET'])
def api():
  return generate_random_person()

@app.route('/main')
def goto_index():
  return redirect('/')

@app.route('/error')
def error():
  return render_template('error.html')

app.run(host='0.0.0.0', port=8080, debug=True)