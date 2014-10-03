from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User, primary_key = True)
    avatar_image = models.ImageField(upload_to='avatars/')
