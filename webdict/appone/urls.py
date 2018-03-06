from django.conf.urls import url,include
from appone import views

app_name = 'appone'

urlpatterns = [
    url(r'^dict/$', views.FormView, name="FormView")
]