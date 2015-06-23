from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^sites/$', views.show_all_sites),
    url(r'^sites/(?P<pk>[0-9]+)/$', views.details),
    url(r'^summary/$', views.summary),
    url(r'^summary-average/$', views.summary_average),
]
