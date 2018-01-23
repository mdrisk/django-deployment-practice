from django.conf.urls import url
from lvl4app import views

#template tagging
app_name = 'lvl4app'

urlpatterns = [
    url(r'^relative/$', views.relative, name="relative"),
    url(r'^other/$', views.other, name="other"),


]
