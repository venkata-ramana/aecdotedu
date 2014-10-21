from django.db import models

class News(models.Model):
    caption = models.CharField(max_length=100)
    description = models.TextField()
    date_time = models.DateTimeField()
    def __unicode__(self):
        return self.caption
    class Meta:
        verbose_name_plural = "News"

class Event(models.Model):
    event_title = models.CharField(max_length=100)
    event_agenda = models.TextField()
    date_time_updated = models.DateTimeField()
    def __unicode__(self):
            return self.event_title
    class Meta:
        verbose_name_plural = "Events"

class Carosel(models.Model):
    images_in_cycle = models.ImageField(upload_to='carosel')
