from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('memes/', views.memes_index, name='index'),
    path('memes/<int:meme_id>/', views.memes_detail, name='detail'),
    path('memes/create/', views.MemeCreate.as_view(), name='memes_create'),
    path('memes/<int:pk>/update/', views.MemeUpdate.as_view(), name='memes_update'),
    path('memes/<int:pk>/delete/', views.MemeDelete.as_view(), name='memes_delete'), 
]