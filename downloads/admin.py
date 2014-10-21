from django.contrib import admin

# Register your models here.
from downloads.models import FileUpload
admin.site.register(FileUpload)
