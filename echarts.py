from pprint import pprint
import fire
import xlrd
import burn
from burn import Burn


def method_selecter(file_name, sheet_name):
    '''Burn:燃尽图'''
    if file_name == 'Burn':
        burn = Burn.Burn('Burn.xlsx', sheet_name)
        burn.open_sheet()


if __name__ == "__main__":
    fire.Fire(method_selecter)
