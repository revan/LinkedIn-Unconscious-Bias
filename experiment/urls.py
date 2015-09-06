from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/(?P<profile_id>.+)/$', views.profile, name='profile'),
    url(r'^(?P<experiment_id>[0-9]+)/$', views.pick, name='pick'),
    url(r'^(?P<experiment_id>[0-9]+)/results/$', views.results, name='results'),
]
