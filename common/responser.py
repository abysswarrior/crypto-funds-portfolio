from .formatter import *


def create_portfolio_data_with_yearly_data(coin_info):
    """create json response based on given coin info

    this function only works for data that has yearly information

    Args:
        coin_info (list): array of coin info

    Returns:
        json response

    """
    data = {}

    data['id'] = coin_info[0]
    data['asset_full_name'] = coin_info[1]
    data['asset_symbol'] = coin_info[3]
    data['price_str'] = coin_info[4]
    data['price_int'] = human_readable_number_to_int(coin_info[4])
    data['reported_marketcap_str'] = coin_info[6]
    data['reported_marketcap_int'] = human_readable_number_to_int(coin_info[6])
    data['last_24h_volume_str'] = coin_info[7]
    data['last_24h_volume_int'] = human_readable_number_to_int(coin_info[7])
    data['last_24h_price_change_str'] = coin_info[5]
    data['last_24h_price_change_int'] = price_change_to_int(coin_info[5])
    data['last_7d_price_change_str'] = coin_info[8]
    data['last_7d_price_change_int'] = price_change_to_int(coin_info[8])
    data['last_30d_price_change_str'] = coin_info[9]
    data['last_30d_price_change_int'] = price_change_to_int(coin_info[9])
    data['last_90d_price_change_str'] = coin_info[10]
    data['last_90d_price_change_int'] = price_change_to_int(coin_info[10])
    data['last_1Y_price_change_str'] = coin_info[11]
    data['last_1Y_price_change_int'] = price_change_to_int(coin_info[11])
    data['last_YTD_price_change_str'] = coin_info[12]
    data['last_YTD_price_change_int'] = price_change_to_int(coin_info[12])
    data['sector'] = coin_info[13]
    data['liquid_supply_str'] = coin_info[14]
    data['liquid_supply_int'] = human_readable_number_to_int(coin_info[14])

    return data


def create_portfolio_data_without_yearly_data(coin_info):
    """create json response based on given coin info

    this function only works for data that has not yearly information

    Args:
        coin_info (list): array of coin info

    Returns:
        json response

    """
    data = {}

    data['id'] = coin_info[0]
    data['asset_full_name'] = coin_info[1]
    data['asset_symbol'] = coin_info[3]
    data['price_str'] = coin_info[4]
    data['price_int'] = human_readable_number_to_int(coin_info[4])
    data['reported_marketcap_str'] = coin_info[6]
    data['reported_marketcap_int'] = human_readable_number_to_int(coin_info[6])
    data['last_24h_volume_str'] = coin_info[7]
    data['last_24h_volume_int'] = human_readable_number_to_int(coin_info[7])
    data['last_24h_price_change_str'] = coin_info[5]
    data['last_24h_price_change_int'] = price_change_to_int(coin_info[5])
    data['last_7d_price_change_str'] = coin_info[8]
    data['last_7d_price_change_int'] = price_change_to_int(coin_info[8])
    data['last_30d_price_change_str'] = coin_info[9]
    data['last_30d_price_change_int'] = price_change_to_int(coin_info[9])
    data['last_90d_price_change_str'] = coin_info[10]
    data['last_90d_price_change_int'] = price_change_to_int(coin_info[10])
    data['last_YTD_price_change_str'] = coin_info[11]
    data['last_YTD_price_change_int'] = price_change_to_int(coin_info[11])
    data['sector'] = coin_info[12]
    data['liquid_supply_str'] = coin_info[13]
    data['liquid_supply_int'] = human_readable_number_to_int(coin_info[13])

    return data


def create_final_response_with_yearly_data(total, portfolio_data):
    """add some total info and create final json response

    this function only works for data that has yearly information

    Args:
        total (list): array of portfolio total info
        portfolio_data (list): list of all portfolio data per coins

    Returns:
        final json response

    """
    response = {}

    response['last_24h_total_price_change_str'] = total[2]
    response['last_24h_total_price_change_int'] = price_change_to_int(total[2])
    response['last_7d_total_price_change_str'] = total[5]
    response['last_7d_total_price_change_int'] = price_change_to_int(total[5])
    response['last_30d_total_price_change_str'] = total[6]
    response['last_30d_total_price_change_int'] = price_change_to_int(total[6])
    response['last_90d_total_price_change_str'] = total[7]
    response['last_90d_total_price_change_int'] = price_change_to_int(total[7])
    response['last_1Y_total_price_change_str'] = total[8]
    response['last_1Y_total_price_change_int'] = price_change_to_int(total[8])
    response['last_YTD_total_price_change_str'] = total[9]
    response['last_YTD_total_price_change_int'] = price_change_to_int(total[9])
    response['total_asset_count'] = len(portfolio_data)
    response['assets'] = portfolio_data

    return response


def create_final_response_without_yearly_data(total, portfolio_data):
    """add some total info and create final json response

    this function only works for data that has not yearly information

    Args:
        total (list): array of portfolio total info
        portfolio_data (list): list of all portfolio data per coins

    Returns:
        final json response

    """
    response = {}

    response['last_24h_total_price_change_str'] = total[2]
    response['last_24h_total_price_change_int'] = price_change_to_int(total[2])
    response['last_7d_total_price_change_str'] = total[5]
    response['last_7d_total_price_change_int'] = price_change_to_int(total[5])
    response['last_30d_total_price_change_str'] = total[6]
    response['last_30d_total_price_change_int'] = price_change_to_int(total[6])
    response['last_90d_total_price_change_str'] = total[7]
    response['last_90d_total_price_change_int'] = price_change_to_int(total[7])
    response['last_YTD_total_price_change_str'] = total[8]
    response['last_YTD_total_price_change_int'] = price_change_to_int(total[8])
    response['total_asset_count'] = len(portfolio_data)
    response['assets'] = portfolio_data

    return response
