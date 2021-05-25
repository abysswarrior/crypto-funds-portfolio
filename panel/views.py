from django.shortcuts import render, HttpResponse
from binance_lab_portfolio.views import BinanceLabAssetsInfo

# Create your views here.
def home(request):
    """panels home page"""

    portfolio_data = BinanceLabAssetsInfo.as_view()(request).render().data

    context = {
        'portfolio':portfolio_data
    }
    return render(request, 'panel/binance_portfolio.html', context)
