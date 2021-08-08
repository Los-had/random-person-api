from flask import Flask, render_template, url_for, redirect, request
from gerador import generate_random_person
from time import sleep
from enviar_email import enviar_email

app = Flask(__name__)

@app.route('/')
def index():
  try:
    return render_template('index.html')
  except:
    return redirect('/error')

@app.route('/api', methods=['GET'])
def api():
  try:
    return generate_random_person()
  except Exception as e:
    return e
    sleep(0.5)
    for r in range(15):
      return f'Você sera redirencionado em {str(r)} segundos\r'
    return redirect('/error')

@app.route('/main')
def goto_index():
  return redirect('/')

@app.route('/error')
def error():
  return render_template('error.html')

@app.route('/send')
def página_email():
  return render_template('send.html')

@app.route('/sucesso', methods=['POST', 'GET'])
def sucesso():
  try:
    if request.method == 'POST':
      msg = request.form['texto']
      email = request.form['email']
      enviar_email(email, msg)
      return redirect('/')
    else:
      return redirect('/error')
  except:
    return redirect('/error')

app.run(host='0.0.0.0', port=8080, debug=True)