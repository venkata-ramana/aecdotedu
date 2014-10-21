from django.db import models

class BatchWiseTopper(models.Model):
    roll_number = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    percentage = models.FloatField(null=True,blank=True)
    batch = models.CharField(max_length=9)
    branch = models.CharField(max_length=3)
    year = models.IntegerField()
    SEM0 = 'SEM0'
    SEM1 = 'SEM1'
    SEM2 = 'SEM2'
    SEM3 = 'SEM3'
    SEM4 = 'SEM4'
    SEM5 = 'SEM5'
    SEM6 = 'SEM6'
    SEM7 = 'SEM7'
    SEM8 = 'SEM8'
    SEMESTERS = ((SEM1,'SEM1'),
                 (SEM2,'SEM2'),
                 (SEM3,'SEM3'),
                 (SEM4,'SEM4'),
                 (SEM5,'SEM5'),
                 (SEM6,'SEM6'),
                 (SEM7,'SEM7'),
                 (SEM8,'SEM8'))
    semseter_in_school = models.CharField(max_length=3,choices=SEMESTERS,default=SEM1)
    
    def __unicode__(self):
        return self.roll_number
    class Meta:
        verbose_name_plural = "Batch Wise Toppers"


class AggregateTopper(models.Model):
    roll_number = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    batch = models.CharField(max_length=9)
    branch = models.CharField(max_length=3)
    percentage = models.FloatField(null=True,blank=True)
    def __unicode__(self):
        return self.roll_number
    class Meta:
        verbose_name_plural = "Aggregate Toppers"