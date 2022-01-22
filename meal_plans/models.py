from django.db import models

# Create your models here.
class WeekDay(models.Model):
	"""Days of the Week for the Meal Plan."""
	text = models.CharField(max_length =200)
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__ (self):
		"""Return a string representation of the model."""
		return self.text

class Meal(models.Model):
	"""Meals for every day."""
	weekday = models.ForeignKey(WeekDay, on_delete=models.CASCADE)
	meal = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return a string representation of the model."""
		if len(self.meal)>20:
			return f"{self.meal[:20]}..."
		else:
			return self.meal