from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:pk>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:pk>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('<int:pk>/tweet_details', views.tweet_details, name = 'tweet_details'),
    path('<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('profile/', views.profile, name='profile'),





    
]