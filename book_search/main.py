import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm
import os
import pprint

pp = pprint.PrettyPrinter(indent=2)

string_to_try = "dsm"

dir_path = "D:/Books"


def find_book():
    list_of_files = list()

    for i in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, i)):
            list_of_files.append(i)

    for k in list_of_files:
        m = k.lower().find(string_to_try)
        if m != -1:
            print(os.path.join(dir_path, k))


if __name__ == "__main__":
    find_book()
