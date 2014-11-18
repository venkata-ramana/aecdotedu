from django.db import models

# Create your models here.
class AcademicsInfo(models.Model):
    title = models.CharField(max_length=160)
    detail = models.TextField()


    def __unicode__(self):
        return self.title