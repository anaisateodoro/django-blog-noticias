# blog/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from blog.models import Noticia # Chama o app(blog) 

@shared_task
def verificar_e_enviar_noticia():
    # Supondo que você tenha um modelo Noticia com um campo 'publicada'
    noticias_novas = Noticia.objects.filter(publicada=True)
    
    if noticias_novas.exists():
        # Enviar e-mail para os usuários
        subject = "Nova notícia publicada no blog"
        message = "Uma nova notícia foi publicada no blog. Confira!"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['user1@example.com', 'user2@example.com'] # Lista de e-mails dos usuários

        send_mail(subject, message, from_email, recipient_list)
