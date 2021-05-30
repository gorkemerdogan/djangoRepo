from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url('register/', views.register, name='register'),
    #url('index/', views.index, name='index'),
    url('login/', views.user_login, name='login'),
]