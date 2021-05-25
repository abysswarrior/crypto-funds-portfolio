from django.urls import path
from .views import *

app_name = 'panel'
urlpatterns = [
    path('', home, name='home'),
    path('binance-portfolio/', binance_portfolio, name='binance')
]