from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .utils import alert_mail




@receiver(post_save, sender = User)
def create_user(sender, instance, created, **kwargs):
    if created:
        subject = 'HamroPasal account creation succussfully'
        message = 'Your email has been register in the hamropasal site.'
        recipient = instance.email

        alert_mail(subject, message, recipient)
    
@receiver(pre_save, sender= User)
def set_username(sender, instance, **kwargs):
    if not instance.username:
        username = f'{instance.first_name}_{instance.last_name}'.lower()
        counter = 1
        while User.objects.filter(username=username):
            username = f'{instance.first_name}_{instance.last_name}_{counter}'.lower()
            counter += 1
        instance.username = username