from email.policy import default
from django.db import router
from django.urls import URLPattern, path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from .views import IgrejaViewSet

router = DefaultRouter()
router.register("igreja", IgrejaViewSet, basename="igreja")

urlpatterns = [path("", include(router.urls))]
