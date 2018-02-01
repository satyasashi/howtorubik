from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name="post_list"),
	url(r'^(?P<pk>\d+)/(?P<post_slug>[\w\d-]+)/$', views.post_detail, name="post_detail"),
	url(r'^(?P<pk>\d+)/(?P<tag_slug>[\w\d-]+)/$', views.post_by_tag, name="post_by_tag"),
	url(r'^basic-3x3-cubing/', views.basicCubing, name="basicCubing"),
	url(r'^advanced-3x3-cubing/', views.advancedCubing, name="advancedCubing"),
	url(r'^basic-3x3-videos/', views.basicVideos, name="basicVideos"),
	url(r'^advanced-3x3-videos/', views.advancedVideos, name="advancedVideos"),
	url(r'^about/$', views.about, name="about"),
]