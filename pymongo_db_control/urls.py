from rest_framework import routers
from .views import UsersViewSet

router = routers.SimpleRouter()
router.register('py', UsersViewSet, basename='user')

urlpatterns = router.urls