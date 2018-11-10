from django.db import models


class Station(models.Model):
    TIMEZONES = (
        ('MSK','0'),
    )
    longitude = models.FloatField()
    latitude = models.FloatField()
    timezone = models.CharField(max_length=100, choices=TIMEZONES)

class Air(models.Model):
    station = models.ForeignKey(Station, related_name="data", on_delete=models.CASCADE)
    t_air = models.FloatField()
    datetime = models.DateTimeField()

    def Sub_zero(self):
        if self.t_air < 0:
            return True
        else:
            return False

    class Meta:
        unique_together = ('t_air', 'datetime')
        ordering = ['datetime']
    def __unicode__(self):
        return '%d: %s' % (self.datetime, self.t_air)
