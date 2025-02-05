from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
