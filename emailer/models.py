from django.db import models

class All_Mail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()