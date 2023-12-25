from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('work', views.WorkViewsets)

urlpatterns = [
    path('profile', views.ProfileView),
    path('user', views.UserView)
]
urlpatterns += router.urls
