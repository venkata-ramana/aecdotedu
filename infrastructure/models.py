from django.db import models

# Create your models here.

class InfrastructureInfo(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()

    def __unicode__(self):
        return self.title