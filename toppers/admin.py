from django.contrib import admin

# Register your models here.
from toppers.models import BatchWiseTopper
from toppers.models import AggregateTopper


admin.site.register(BatchWiseTopper)
admin.site.register(AggregateTopper)