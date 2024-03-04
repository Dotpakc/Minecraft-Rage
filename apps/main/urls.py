from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
   path('' , views.index , name='index'),
   path('contact_form/' , views.contact_form , name='question')
]