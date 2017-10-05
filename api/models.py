from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class bloodbank(models.Model):
    #user=models.ForeignKey(User)

    hosp_name = models.TextField()
    hosp_add = models.TextField()
    hosp_contact = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    a_pos = models.IntegerField()
    b_pos = models.IntegerField()
    ab_pos = models.IntegerField()
    o_pos = models.IntegerField()
    a_neg = models.IntegerField()
    ab_neg = models.IntegerField()
    b_neg = models.IntegerField()
    o_neg = models.IntegerField()


    def __str__(self):
        return self.hosp_name

    class Meta:
        db_table = 'blood'