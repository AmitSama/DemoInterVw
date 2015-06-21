from django.db import models
from django.utils import timezone

class Site(models.Model):
	name = models.CharField(max_length=50)
	created_date = models.DateTimeField(default=timezone.now)
	a_val = models.DecimalField(max_digits=10, decimal_places=2)
	b_val = models.DecimalField(max_digits=10, decimal_places=2)
	
	
	#not functional now
	def createEntry(self, name, a_val, b_val):
		self.name = name
		self.a_val = a_val
		self.b_val = b_val
		self.save()
	
	def __str__(self):
		return self.name
# Create your models here.
