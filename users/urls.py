from django.urls import path
from .views import create_user , update_user, login_view, home_view, user_list, logout_view
# from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home_view, name='home'),
    path('create-user/', create_user, name='create_user'),
    path('update-user/<int:pk>/', update_user, name='user_update'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user-list', user_list, name='user_list'),
]
