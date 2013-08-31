from django.db import models

# Create your models here.
class Notice(models.Model):
    # subject = models.TextField(max_length=100)
    notice = models.TextField(max_length=2000)
    pub_date = models.DateTimeField('date posted')

    def __unicode__(self):
        return self.notice