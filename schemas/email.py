from pydantic import BaseModel
from typing import Optional, List

class ErrorSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    mensagem: str

class PostSchema(BaseModel):
    """ Define como devem ser o campos para envio de e-mail.
    """

    to_email: str   # E-mail para onde será enviada a mensagem.
    subject: str    # Subject do e-mail.
    body: str       # Corpo do e-mail.
    
   
