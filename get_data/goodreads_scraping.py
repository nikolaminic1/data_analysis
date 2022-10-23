import requests
import time
from bs4 import BeautifulSoup as soup
import pprint


p = pprint.PrettyPrinter(indent=2)


def requests_list():
    url = "https://www.apa.org/monitor/julaug02/eminent"
    data = requests.get(url).text
    p_data = soup(data, "html.parser")
    p.pprint(p_data)


if __name__ == '__main__':
    requests_list()
