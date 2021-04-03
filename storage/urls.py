from rest_framework.routers import DefaultRouter
from storage.views import CategoryViewSet, Model3dViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'models', Model3dViewSet, basename='models')

urlpatterns = router.urls
