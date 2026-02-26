from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, ObservationViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'observations', ObservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]