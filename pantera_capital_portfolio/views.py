from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from common.crawler import crawl
from common.responser import *
from common.messari_urls import portfolio_urls


class PanteraCapitalAssetsInfo(APIView):
    """
    crawl pantera capital portfolio in messari.io and return
    as JSON
    """

    @staticmethod
    def get(request):

        portfolio_data = []

        # crawl pantera capital
        assets, total, driver = crawl(portfolio_urls["pantera_capital"])

        # loop over portfolio assets and format crawled data
        for coin in assets:

            coin_info = coin.text.split('\n')

            try:
                data = create_portfolio_data_without_yearly_data(coin_info)
            except Exception as e:
                print("NOT ENOUGH DATA ------> BINANCE LABs - ", coin_info[3])
                continue

            portfolio_data.append(data)

        # add total info to asset data
        final_data = create_final_response_without_yearly_data(total, portfolio_data)

        driver.quit()

        return Response(final_data, status=status.HTTP_200_OK)
