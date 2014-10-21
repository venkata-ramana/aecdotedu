from django.db import models

class NewsPaperArticles(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news_media')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Print Media/Electronic Media"