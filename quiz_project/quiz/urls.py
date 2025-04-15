from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/results/<int:result_id>/', views.results, name='results'),
    path('history/', views.results_history, name='history'),
]