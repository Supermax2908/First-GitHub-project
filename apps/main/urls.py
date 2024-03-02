from django.urls import path
from . import views

app_main = 'main'
urlpatterns = [
    path('', views.greeting, name='greeting'),
    path('', views.about_site, name='site')
]