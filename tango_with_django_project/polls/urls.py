from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]