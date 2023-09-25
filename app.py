import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from schemas import *
import os


info = Info(title="Email Service", version="1.0.0")
app = OpenAPI(__name__, info=info)

app.config['JSON_SORT_KEYS'] = True
app.config.from_object(os.getenv("APP_SETTINGS"))

home_tag = Tag(name="Email Service", description="Documentação da API do Email Service")

Email_tag = Tag( name="E-Mail", description="Serviço de envio de E-mail")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi/swagger, tela do swagger com a documentação do Email Service.
    """
    return redirect('/openapi/swagger')


@app.post('/send_email', tags=[Email_tag],
          responses={"200": PostSchema,  "409": ErrorSchema,  "400": ErrorSchema})
def send_email(form: PostSchema):
    """Rota POST para envio de e-mail.
    Esta rota faz o envio de um e-mail baseado no campos :

        to_email: str  - E-mail para onde será enviada a mensagem
        subject: str   - Subject do e-mail
        body: str      - Corpo do e-mail.
    """

    from_email = app.config['FROM_EMAIL']   
    password = app.config['PASSWORD']

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = form.to_email
    msg['Subject'] = form.subject
    msg.attach(MIMEText(form.body, 'plain'))

    try:
     
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.ehlo()
        server.starttls
        server.login(from_email, password )
        server.sendmail(from_email, form.to_email , msg.as_string())
        server.quit()
         
        msg = "E-mail enviado com sucesso!"
        return {"mensagem": msg} , 200

    except Exception as e:
        error_msg = "Erro ao enviar o e-mail :/"
        return {"mensagem": error_msg}, 400
