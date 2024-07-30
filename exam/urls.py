from django.urls import path
from exam import views
from .views import exam_landing_page


urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('<int:exam_id>/questions/', views.question_list, name='question_list'),
    path('submit_answers/', views.submit_answers, name='your_submit_view_url_name'),
    path('landing/', exam_landing_page, name='exam_landing'),
]