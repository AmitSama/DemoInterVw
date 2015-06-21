from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sites/', views.show_all_sites),
    url(r'^sites/(?P<pk>[0-9]+)/$', views.site_details),
    url(r'^summary/', views.summary),
]
