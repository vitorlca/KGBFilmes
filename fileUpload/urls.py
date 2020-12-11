from django.urls import include, path
from .views import *
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
  path('images/', views.image_list, name='image_list'),
  path('images/upload', views.image_upload, name='image_upload'),
  # path('images/upload_adm', views.upload_adm, name='image_upload_adm'),
]