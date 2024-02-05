from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'', ClassificationViewSet, basename='classification')
router.register(r'paleta', PaletaViewSet, basename='paleta')
urlpatterns = router.urls
