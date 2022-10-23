import requests
import time
from bs4 import BeautifulSoup as soup
import pprint


p = pprint.PrettyPrinter(indent=2)


def write_names(names):
    with open('./names.txt', 'w+') as outfile:
        for name in names:
            outfile.write(name)
            outfile.write('\n')

        outfile.close()


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

        infile.close()


def extract_names():
    list_of_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "*"]

    with open('./names.txt', 'r+') as outfile:
        data = outfile.readlines()
        for name in data:
            pass

        # adding possibiliti to remplace all the numbers in names and live only strings that are later gonna be
        # stored in txt file for finding the full names


if __name__ == '__main__':
    # requests_list()
    extract_names()
