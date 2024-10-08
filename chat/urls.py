from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('create/', views.create_room, name='create_room'),
    path('leave/<str:room_name>/', views.leave_room, name='leave_room'),
    path('delete/<str:room_name>/', views.delete_room, name='delete_room'),
    path('<str:room_name>/', views.chat_room, name='chat_room'),
    path('get_messages/<str:room_name>/', views.get_messages, name='get_messages'),  # 새 URL 패턴 추가
]
