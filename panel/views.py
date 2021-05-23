from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    """panels home page"""
    context = {
        'portfolio': {
            "last_24h_total_price_change_str": "-0.99%",
            "last_24h_total_price_change_int": -0.99,
            "last_7d_total_price_change_str": "-26.32%",
            "last_7d_total_price_change_int": -26.32,
            "last_30d_total_price_change_str": "-21.76%",
            "last_30d_total_price_change_int": -21.76,
            "last_90d_total_price_change_str": "-13.02%",
            "last_90d_total_price_change_int": -13.02,
            "last_1Y_total_price_change_str": "+510.64%",
            "last_1Y_total_price_change_int": 510.64,
            "last_YTD_total_price_change_str": "+113.68%",
            "last_YTD_total_price_change_int": 113.68,
            "total_asset_count": 17,
            "assets": [
                {
                    "id": "1",
                    "asset_full_name": "Bitcoin",
                    "asset_symbol": "BTC",
                    "price_str": "$36,349.72",
                    "price_int": 36349.72,
                    "reported_marketcap_str": "$686B",
                    "reported_marketcap_int": 686000000000.0,
                    "last_24h_volume_str": "$10.61B",
                    "last_24h_volume_int": 10610000000.0,
                    "last_24h_price_change_str": "+0.15%",
                    "last_24h_price_change_int": 0.15,
                    "last_7d_price_change_str": "-21.49%",
                    "last_7d_price_change_int": -21.49,
                    "last_30d_price_change_str": "-28.67%",
                    "last_30d_price_change_int": -28.67,
                    "last_90d_price_change_str": "-32.58%",
                    "last_90d_price_change_int": -32.58,
                    "last_1Y_price_change_str": "+297.60%",
                    "last_1Y_price_change_int": 297.6,
                    "last_YTD_price_change_str": "+24.16%",
                    "last_YTD_price_change_int": 24.16,
                    "sector": "Currencies",
                    "liquid_supply_str": "18.72M",
                    "liquid_supply_int": 18720000.0
                },
                {
                    "id": "2",
                    "asset_full_name": "Ethereum",
                    "asset_symbol": "ETH",
                    "price_str": "$2,172.49",
                    "price_int": 2172.49,
                    "reported_marketcap_str": "$254B",
                    "reported_marketcap_int": 254000000000.0,
                    "last_24h_volume_str": "$11.10B",
                    "last_24h_volume_int": 11100000000.0,
                    "last_24h_price_change_str": "-3.43%",
                    "last_24h_price_change_int": -3.43,
                    "last_7d_price_change_str": "-38.57%",
                    "last_7d_price_change_int": -38.57,
                    "last_30d_price_change_str": "-7.03%",
                    "last_30d_price_change_int": -7.03,
                    "last_90d_price_change_str": "+23.86%",
                    "last_90d_price_change_int": 23.86,
                    "last_1Y_price_change_str": "+966.24%",
                    "last_1Y_price_change_int": 966.24,
                    "last_YTD_price_change_str": "+201.57%",
                    "last_YTD_price_change_int": 201.57,
                    "sector": "Smart Contract Platforms",
                    "liquid_supply_str": "115M",
                    "liquid_supply_int": 115000000.0
                }
            ]
        }
    }
    return render(request, 'panel/dashboard.html', context)
