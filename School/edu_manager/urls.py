from rest_framework import routers
from .views import TeacherViewSet, ClassViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register("teacher", TeacherViewSet)
router.register("classes", ClassViewSet)
router.register("student", StudentViewSet)

urlpatterns = router.urls