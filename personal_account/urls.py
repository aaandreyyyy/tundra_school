from django.urls import path
from . import views_lk

urlpatterns = [
    path('logout_user', views_lk.logout_user, name='logout')
]
