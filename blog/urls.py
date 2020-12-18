from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
