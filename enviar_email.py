import smtplib

senha = open('senha.txt').read()

def enviar_email(autor, comentario):
  email_de = 'RandomPersonAPI.comments@gmail.com'
  email_para = 'githubtestefinal@gmail.com'
  smtp = 'smtp.gmail.com'
  servidor = smtplib.SMTP(smtp, 587)
  servidor.starttls()
  servidor.login(email_de, senha)
  msg = f'''
  Mensagem de: {autor}
  ----------------------------------
  
  "{comentario}"
  '''
  servidor.sendmail(email_de, email_para, msg)
  servidor.quit()
  print('Email enviado!')

if __name__ == '__main__':
  enviar_email('teste.teste@gmail.com', 'teste')