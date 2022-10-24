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
    list_of_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "*", "Â"]

    with open('./names.txt', 'r+') as outfile:
        data = outfile.readlines()
        list_final_names = list()
        for name in data:
            striped_name = name.strip()
            final_name = str()
            for char in striped_name:
                if char not in list_of_chars:
                    final_name += char
            list_final_names.append(final_name)

    with open('./final_names.txt', 'w') as fn_file:
        for k in list_final_names:
            fn_file.write(k.strip('.').strip())
            fn_file.write('\n')

        fn_file.close()
        # adding possibility to replace all the numbers in names and live only strings that are later going to be
        # stored in txt file for finding the full names


def fetch_profiles():
    with open('./final_names.txt', 'r') as i_file:
        list_of_names = i_file.readlines()
        striped_list = [i.strip() for i in list_of_names]
        print(striped_list)

        i_file.close()


if __name__ == '__main__':
    # requests_list()
    # extract_names()
    fetch_profiles()
