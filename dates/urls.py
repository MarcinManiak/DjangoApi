from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import DatesViwset

router = routers.DefaultRouter()
router.register('dates', DatesViwset)

urlpatterns = [
    path('', include(router.urls))
]
