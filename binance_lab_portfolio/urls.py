from django.urls import path
from .views import *

urlpatterns = [
    path('assets/', BinanceLabAssetsInfo.as_view())
]