from pydantic import BaseModel
from typing import Optional, List

class ErrorSchema(BaseModel):
    """ Define como uma mensagem de erro será representada.
    """
    mensagem: str = "Erro ao enviar o e-mail :/"


class PostResultSchema(BaseModel):
    """ Define como uma mensagem de sucesso será representada.
    """
    mensagem: str = "E-mail enviado com sucesso!"

class PostSchema(BaseModel):
    """ Define como devem ser os campos para envio de e-mail.
    """

    to_email: str   # E-mail para onde será enviada a mensagem.
    subject: str    # Subject do e-mail.
    body: str       # Corpo do e-mail.
    
   
