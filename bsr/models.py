from django.db import models
class data(models.Model):
	Date = models.DateField()
	Total = models.IntegerField()
	Recovered = models.IntegerField()
	Death = models.IntegerField()
