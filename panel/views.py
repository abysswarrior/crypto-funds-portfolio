from django.shortcuts import render, HttpResponse
from binance_lab_portfolio.views import BinanceLabAssetsInfo


def home(request):
    """home page"""
    return render(request, 'panel/index.html')


def binance_portfolio(request):
    """binance portfolio page"""

    portfolio_data = BinanceLabAssetsInfo.as_view()(request).render().data

    context = {
        'portfolio':portfolio_data
    }
    return render(request, 'panel/binance_portfolio.html', context)
