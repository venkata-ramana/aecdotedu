from django.contrib import admin

# Register your models here.
from .models import News
from .models import Event
from .models import Carosel
admin.site.register(Carosel)
admin.site.register(News)
admin.site.register(Event)