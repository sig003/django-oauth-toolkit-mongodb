from rest_framework import routers
from .views import UsersViewSet, HousesViewSet

router = routers.SimpleRouter()
router.register('house', UsersViewSet)
router.register('houses/info', HousesViewSet)

urlpatterns = router.urls