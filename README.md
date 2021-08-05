# random-person-api

<main>
  <p>API que entrega dados aleatórios sobre pessoas que (provavelmente) não existem.</p>
  <article>
    <br>
    <h3>Como usar?</h3>
    <br>
    <p>Copie o link abaixo</p>
    <a href="https://random-person-api.choccy-milk.repl.co/api" class="api_link">https://random-person-api.choccy-milk.repl.co/api</a>
    <p>e digite no seu editor de código: <br><i><strong>AVISO: este é apenas um exemplo de uso em python.</strong></i></p><br>

```
import requests 
import json 

api = requests.get('https://random-person-api.choccy-milk.repl.co/api')
resposta = json.loads(api.text)


nome = resposta['nome']

email = resposta['email']

idade = resposta['idade']

senha = resposta['senha']

estado_civil = resposta['estado_civil']

localizacao = resposta['localizacao']

empregada_ou_desempregada = resposta
['empregado_ou_desempregado']

trabalha_ou_estuda_com = ['trabalha_ou_estuda_com']
   ```
   <p>Pronto! Você pegou todos as informações que a api forneçe</p>
   <h3>Como instalar localmente?</h3>
   Baixe o projeto no github e depois abra o seu terminal e digite:

   ```
   cd random-person-api
   pip3 install -r requirements.txt
   python3 main.py
   ```
  para encerrar o processo digite ``Ctrl + C`` ou ``Cmd + C``
  </article>
  <br>
  <hr>
  <br>
  <footer>
    <p>Se sinta livre para contribuir, ainda em desenvolvimento na plataforma <a href="https://replit.com">Repl.it</a></p>
    <p>Licença: <a href="LICENSE">MIT</a></p>
    <p>Links: <br><a href="htts://github.com/Los-had/random-person-api">GitHub</a> <br><a href="https://replit.com/@choccy-milk/random-person-api?v=1">Repl.it</a></p>
    <br><hr><br>
    <p>Made by Los-had with ❤</p>
  </footer>
</main>