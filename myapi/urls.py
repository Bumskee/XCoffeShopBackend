from django.urls import path, include, re_path
from rest_framework import routers
from myapi import views
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^menues$', views.menuesApi),
    re_path(r'^menues/([0-9]+)$', views.menuesApi)
]