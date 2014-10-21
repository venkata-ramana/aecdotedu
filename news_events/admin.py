from django.contrib import admin

# Register your models here.
from news_events.models import News
from news_events.models import Event
from news_events.models import Carosel
admin.site.register(Carosel)
admin.site.register(News)
admin.site.register(Event)