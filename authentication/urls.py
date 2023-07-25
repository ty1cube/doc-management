from django.urls import path
from . import views

app_name='authentication'

urlpatterns = [
    path('', views.user_login, name='user_login'),
    # path('logins/', views.LoginView.as_view(),name='login'),
]
