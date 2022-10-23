import requests
import time
from bs4 import BeautifulSoup as soup
import pprint


p = pprint.PrettyPrinter(indent=2)


def requests_list():

    with open('./page.html', 'r') as infile:
        p_data = soup(infile, "html.parser")
        div_with_list = p_data.find('div', attrs={"class":"wysiwyg lengthy"})
        p_data = div_with_list.find_all('p')

        list_of_names = list()

        for i in p_data:
            if i.text is not None:
                list_of_names.append(i.text)

        p.pprint(list_of_names)


if __name__ == '__main__':
    requests_list()
