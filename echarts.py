from pprint import pprint
import fire
import xlrd
import burn
from burn import Burn


def method_selecter(name):
    '''Burn:燃尽图'''
    if name == 'Burn':
        burn = Burn.Burn('burn.xlsx')
        pass


if __name__ == "__main__":
    fire.Fire(method_selecter)
