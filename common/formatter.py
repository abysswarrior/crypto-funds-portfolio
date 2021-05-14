def human_readable_number_to_int(human_readable_number):
    """change number from string human readable format like $50B to integer

    Args:
        human_readable_number (string): number like `$1,500.60` or `$54B`

    Returns:
        integer number like 150000000

    """
    # remove $ sign
    human_readable_number = human_readable_number.replace('$', '')

    int_number = 0

    if human_readable_number != '--' and human_readable_number != '0':

        # billion
        if human_readable_number[-1] == 'B':
            int_number = float(human_readable_number.replace('B', '')) * 1000 * 1000 * 1000

        # million
        elif human_readable_number[-1] == 'M':
            int_number = float(human_readable_number.replace('M', '')) * 1000 * 1000

        # thousand or other
        else:
            int_number = float(human_readable_number.replace(',', ''))

    return int_number


def price_change_to_int(price_change_str):
    """format changing price in percent to integer

    Args:
        price_change_str (string): price like `%50.6`

    Returns:
        integer price like 50.6

    """
    price_change_int = 0

    if price_change_str != '--':
        price_change_int = float(price_change_str.replace('%', ''))

    return price_change_int
