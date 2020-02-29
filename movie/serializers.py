from .models import Movie
from rest_framework import serializers
import json


class MovieSerializer(serializers.ModelSerializer):
	genre = serializers.SerializerMethodField()
	class Meta:
		model = Movie
		fields = ['id','name','imdb_score','director','genre','popularity_99']

	def get_genre(self, obj):
		return json.loads(Movie.objects.filter(id = obj.id)[0].genre)
