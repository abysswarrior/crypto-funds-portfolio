from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class BinanceLabAssetsInfo(APIView):

    @staticmethod
    def get(request):
        data = {'last_24h_total_price_change_str': '-12.73%', 'last_24h_total_price_change_int': -12.73,
                'last_7d_total_price_change_str': '-5.93%', 'last_7d_total_price_change_int': -5.93,
                'last_30d_total_price_change_str': '+5.33%', 'last_30d_total_price_change_int': 5.33,
                'last_90d_total_price_change_str': '+40.47%', 'last_90d_total_price_change_int': 40.47,
                'last_1Y_total_price_change_str': '+881.09%', 'last_1Y_total_price_change_int': 881.09,
                'last_YTD_total_price_change_str': '+215.64%', 'last_YTD_total_price_change_int': 215.64,
                'total_asset_count': 17, 'assets': [
                {'id': '1', 'asset_full_name': 'Bitcoin', 'asset_symbol': 'BTC', 'price_str': '$49,337.29',
                 'price_int': 49337.29, 'reported_marketcap_str': '$934B', 'reported_marketcap_int': 934000000000.0,
                 'last_24h_volume_str': '$24.94B', 'last_24h_volume_int': 24940000000.0,
                 'last_24h_price_change_str': '-12.71%', 'last_24h_price_change_int': -12.71,
                 'last_7d_price_change_str': '-12.12%', 'last_7d_price_change_int': -12.12,
                 'last_30d_price_change_str': '-22.04%', 'last_30d_price_change_int': -22.04,
                 'last_90d_price_change_str': '+4.65%', 'last_90d_price_change_int': 4.65,
                 'last_1Y_price_change_str': '+433.16%', 'last_1Y_price_change_int': 433.16,
                 'last_YTD_price_change_str': '+68.72%', 'last_YTD_price_change_int': 68.72, 'sector': 'Currencies',
                 'liquid_supply_str': '18.71M', 'liquid_supply_int': 18710000.0},
                {'id': '2', 'asset_full_name': 'Ethereum', 'asset_symbol': 'ETH', 'price_str': '$3,709.23',
                 'price_int': 3709.23, 'reported_marketcap_str': '$438B', 'reported_marketcap_int': 438000000000.0,
                 'last_24h_volume_str': '$31.57B', 'last_24h_volume_int': 31570000000.0,
                 'last_24h_price_change_str': '-12.84%', 'last_24h_price_change_int': -12.84,
                 'last_7d_price_change_str': '+7.06%', 'last_7d_price_change_int': 7.06,
                 'last_30d_price_change_str': '+62.57%', 'last_30d_price_change_int': 62.57,
                 'last_90d_price_change_str': '+102.73%', 'last_90d_price_change_int': 102.73,
                 'last_1Y_price_change_str': '+1774.17%', 'last_1Y_price_change_int': 1774.17,
                 'last_YTD_price_change_str': '+411.71%', 'last_YTD_price_change_int': 411.71,
                 'sector': 'Smart Contract Platforms', 'liquid_supply_str': '115M', 'liquid_supply_int': 115000000.0},
                {'id': '3', 'asset_full_name': 'Terra', 'asset_symbol': 'LUNA', 'price_str': '$15.45',
                 'price_int': 15.45, 'reported_marketcap_str': '$6.15B', 'reported_marketcap_int': 6150000000.0,
                 'last_24h_volume_str': '$504M', 'last_24h_volume_int': 504000000.0,
                 'last_24h_price_change_str': '-10.31%', 'last_24h_price_change_int': -10.31,
                 'last_7d_price_change_str': '-6.53%', 'last_7d_price_change_int': -6.53,
                 'last_30d_price_change_str': '+0.40%', 'last_30d_price_change_int': 0.4,
                 'last_90d_price_change_str': '+173.36%', 'last_90d_price_change_int': 173.36,
                 'last_1Y_price_change_str': '--', 'last_1Y_price_change_int': 0,
                 'last_YTD_price_change_str': '+2317.15%', 'last_YTD_price_change_int': 2317.15,
                 'sector': 'Payment Platforms', 'liquid_supply_str': '890M', 'liquid_supply_int': 890000000.0},
                {'id': '4', 'asset_full_name': 'Polygon', 'asset_symbol': 'MATIC', 'price_str': '$1.05',
                 'price_int': 1.05, 'reported_marketcap_str': '$5.35B', 'reported_marketcap_int': 5350000000.0,
                 'last_24h_volume_str': '$1.66B', 'last_24h_volume_int': 1660000000.0,
                 'last_24h_price_change_str': '-9.67%', 'last_24h_price_change_int': -9.67,
                 'last_7d_price_change_str': '+36.56%', 'last_7d_price_change_int': 36.56,
                 'last_30d_price_change_str': '+146.27%', 'last_30d_price_change_int': 146.27,
                 'last_90d_price_change_str': '+762.22%', 'last_90d_price_change_int': 762.22,
                 'last_1Y_price_change_str': '+5016.16%', 'last_1Y_price_change_int': 5016.16,
                 'last_YTD_price_change_str': '+5732.70%', 'last_YTD_price_change_int': 5732.7, 'sector': 'Scaling',
                 'liquid_supply_str': '7.66B', 'liquid_supply_int': 7660000000.0}]}

        return Response(data, status=status.HTTP_200_OK)
