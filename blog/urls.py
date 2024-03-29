from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #ex: /blog/5/question_id
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #ex:/blog/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
