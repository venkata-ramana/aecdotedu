from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=40)
    cover_pic = models.ImageField(upload_to='gallery_coverpic')

    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Galleries"

class GalleryImages(models.Model):
    image = models.ImageField(upload_to='gallery_images')
    foreign_key = models.ForeignKey(Gallery)

    class Meta:
         verbose_name_plural = "Gallery Images"