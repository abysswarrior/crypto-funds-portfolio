from django.urls import path
from .views import *

urlpatterns = [
    path('assets/', PanteraCapitalAssetsInfo.as_view())
]