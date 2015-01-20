from django.contrib import admin

# Register your models here.
from . models import GalleryImages,Gallery
class ItemInline(admin.StackedInline):
    model = GalleryImages
    extra = 0

class GalleryAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

admin.site.register(Gallery,GalleryAdmin)