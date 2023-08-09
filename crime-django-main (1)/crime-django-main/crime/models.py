from django.db import models

class crime(models.Model):
  crime_type = models.CharField(max_length=100, blank=True, null=True, default="")
  year = models.IntegerField(blank=True, null=True, default=1)
  month = models.IntegerField(blank=True, null=True, default=1)  
  day = models.IntegerField(blank=True, null=True, default=1)  
  hour = models.IntegerField(blank=True, null=True, default=1)
  minute = models.IntegerField(blank=True, null=True, default=1)
  block = models.CharField(max_length=100, blank=True, null=True, default="")
  neighbor = models.CharField(max_length=100,blank=True, null=True, default="")
  x = models.CharField(max_length=20, blank=True, null=True, default="")
  y = models.CharField(max_length=20, blank=True, null=True, default="")

  def __str__(self):
    return self.crime_type