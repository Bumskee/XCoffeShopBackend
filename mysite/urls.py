from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^', include('myapi.urls')),
    path('auth/', obtain_auth_token)
]
