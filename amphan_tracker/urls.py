from django.urls import path

from . import views

urlpatterns=[
	path('',views.index,name='index'),
  path('forecast_track/',views.forecast_track,name='current_index'),
	path('amisafe/',views.amisafe,name='amisafe')
	# path('elections/',views.elections,name='elections'),
	# path('candidates/',views.candidates,name='candidates'),
	# path('visualization/',views.visualization,name='visualization'),

]