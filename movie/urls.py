
from django.conf.urls import url

from .views import MovieListView, MovieRUDView

app_name = 'Movie'

urlpatterns = [
	url(r'^$', MovieListView.as_view(), name='movie-filter-list'),
	url(r'^(?P<pk>\d+)/$', MovieRUDView.as_view(), name='movie-detail'),
	]
