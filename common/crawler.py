from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.environment_variables import *
import time


def crawl(url):
    """use selenium to crawl given url

    Args:
        url (string): url to crawl

    Returns:
        returns 3 item:

        assets: list of all coins info in portfolio
        total: total info of portfolio
        driver: driver object

    """
    chrome_options = Options()
    
    # add binary location only when running on heroku
    if ON_HEROKU:
        chrome_options.binary_location = GOOGLE_CHROME_BIN

    # some option to work headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")

    # add windows size to crawl whole page
    # TODO: add scrolling feature to selenium
    chrome_options.add_argument("window-size=1920,2100")

    # use proxy for restricted country to see messari.io
    if RESTRICTED_AREA:
        chrome_options.add_argument(f"--proxy-server=socks5://{PROXY_HOST}:{PROXY_PORT}")

    # add webdriver
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)

    # call url and wait 5 second to page load completely
    driver.get(url)
    time.sleep(5)

    # crawl
    assets = driver.find_elements_by_xpath('//*[@id="root"]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div')
    total = driver.find_elements_by_xpath('//*[@id="root"]/div[2]/div/div[2]/div[2]/div[3]')[0].text.split('\n')

    return assets, total, driver
