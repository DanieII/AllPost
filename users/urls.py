from django.urls import path

from users.views import Login, logout_view, Register

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', Register.as_view(), name='register'),
]
