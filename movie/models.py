from django.db import models
import json

# Create your models here.
class Movie(models.Model):
	imdb_score = models.FloatField()
	name = models.CharField(max_length=30)
	director = models.CharField(max_length=30)
	genre = models.CharField(max_length=100)
	popularity_99 = models.FloatField()

	# def get_genre(self):
	# 	return json.loads(self.genre)

	def set_genre(self, x):
		return json.dumps(self.genre)

	def __str__(self):
		return str(self.id)

	class Meta:
		ordering = ['imdb_score']
