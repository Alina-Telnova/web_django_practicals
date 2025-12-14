from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import viewsets

router = SimpleRouter()
router.register(r'organizations', viewsets.OrganizationViewSet)
router.register(r'users', viewsets.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]