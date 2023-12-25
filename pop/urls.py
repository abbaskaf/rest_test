from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('api-auth-token', views.obtain_auth_token),
    path('api-token', include('rest_framework.urls'))
]
