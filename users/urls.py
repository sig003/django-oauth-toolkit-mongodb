from django.urls import path
from .views import RegisterView, UserList, UserDetail, ModifyUserPassword

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('list/', UserList.as_view()),
    path('list/<pk>/', UserDetail.as_view()),
    path('password/<int:pk>/', ModifyUserPassword.as_view()),
]