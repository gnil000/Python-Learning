from django.urls import path

from .views import Login, Logout, Profile, Register

urlpatterns = [
    path('', Profile.as_view(), name='profile'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
]
