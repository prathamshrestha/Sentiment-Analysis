from django.db import models
from  django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver



class User(AbstractUser):
    middle_name      =models.CharField(verbose_name='middle name',max_length=100)
    contact_address =models.CharField(max_length=150)
    contact_number  =models.CharField(max_length=10, blank=True)
    is_collegestudent= models.BooleanField(default=False)



    groups=None
    user_permissions=None

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance= None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)