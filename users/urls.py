from django.urls import path
from .views import RegisterView, UserList, UserDetail

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('list/', UserList.as_view()),
    path('list/<pk>/', UserDetail.as_view()),
]