from django.db import models

# Create your models here.
class FileUpload(models.Model):
    file_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='file_upload')