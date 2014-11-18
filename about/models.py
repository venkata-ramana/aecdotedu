from django.db import models

class About(models.Model):
    message_titled = models.CharField(max_length=160)
    message_body = models.TextField()

    def __unicode__(self):
        return self.message_titled