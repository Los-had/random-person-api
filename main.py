from flask import Flask, render_template, url_for, redirect
from gerador import generate_random_person
from time import sleep

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

app.run(host='0.0.0.0', port=8080, debug=True)