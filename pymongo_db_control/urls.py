from rest_framework import routers
from .views import UsersViewSet
from django.urls import path, include, re_path

router = routers.SimpleRouter()
router.register('py', UsersViewSet, basename='user')

urlpatterns = router.urls
