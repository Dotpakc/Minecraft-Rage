from django.urls import path

from . import views

app_name = 'skins'

urlpatterns = [
   path('' , views.index , name='index'),
   path('create/' , views.create , name='create'),
   path('<id>/' , views.detail , name='detail'),
   path('<uuid:id>/like/' , views.like , name='add_like'),
]