from flask import Flask, render_template, url_for
import names
from random import choice, randint
import string

app = Flask('random-person-api')

def generate_random_person():
  
  opt = ['Empregado(a)', 'Desempregado(a)']
  empregado_ou_desempregado = choice(opt) 
  nome = names.get_full_name()
  estado_civil = ['Casado(a)', 'Solteiro(a)']
  idade = randint(13, 101)
  profissão_ou_estudo = ['Medicina', 'Direito', 'Engenharia Civil', 'Arquitetura e Urbanismo', 'Relacoes Internacionais', 'Publicidade e Propaganda', 'Fisioterapia', 'Psicologia', 'Ciencia da Computacao', 'Nutricao']

  def generate_email():
    
    extensões_de_email = ['@gmail.com', '@outlook.com', '@hotmail.com']
    email = ''
    email += nome
    email += '-'
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

  resposta_pronta = { 'nome': nome, 'email': generate_email(), 'idade': idade, 'senha': generate_password(), 'estado_civil': choice(estado_civil), 'trabalha_ou_estuda_com': choice(profissão_ou_estudo), 'empregado_ou_desempregado': empregado_ou_desempregado }


  if empregado_ou_desempregado == 'Desempregado(a)':
    resposta_pronta = { 'nome': nome, 'email': generate_email(), 'idade': idade, 'senha': generate_password(), 'estado_civil': choice(estado_civil), 'trabalha_ou_estuda_com': None, 'empregado_ou_desempregado': empregado_ou_desempregado }
  
  return resposta_pronta

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api', methods=['GET'])
def api():
  return generate_random_person()

app.run(host='0.0.0.0', port=8080, debug=True)