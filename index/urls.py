from django.urls import path
from .import views

app_name = 'index'


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('mannual/', views.mannual, name='mannual'),
]