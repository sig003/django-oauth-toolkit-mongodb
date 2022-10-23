from rest_framework import routers
from .views import UsersViewSet

router = routers.SimpleRouter()
router.register('house', UsersViewSet)

urlpatterns = router.urls