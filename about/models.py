from django.db import models

class About(models.Model):
    message_titled = models.CharField(max_length=120)
    message_body = models.TextField()
