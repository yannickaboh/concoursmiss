from django.db import models

# Create your models here.


class Gprovince(models.Model):
	nom = models.CharField(max_length=250, blank=False, null=False)
	longitude = models.CharField(max_length=100, blank=True, default='0.0')
	latitude = models.CharField(max_length=100, blank=True, default='0.0')

	def __str__(self):
		return self.nom

	class Meta:
		verbose_name_plural = 'Gprovinces'
		ordering = ['nom']
