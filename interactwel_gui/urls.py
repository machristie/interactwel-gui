
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^hello/', views.hello_world),
    url(r'^projects/', views.projects),
]
