from django.urls import path
from .views import LoginView, RegisterView, UserListView, DeactivateUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/deactivate/', DeactivateUserView.as_view(), name='deactivate-user'),
    path('login/', LoginView.as_view(), name='login'),
]
