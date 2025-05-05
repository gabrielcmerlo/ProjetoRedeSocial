from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('add-friend/', views.add_friend, name='add_friend'),
    path('messages/', views.messages, name='messages'),
]