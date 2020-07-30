from django.db import models

class littask(models.Model):
    image=models.ImageField(upload_to='images/')