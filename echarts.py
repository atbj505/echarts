from pprint import pprint
from burn import Burn
import fire
import xlrd


def method_selecter(name):
    '''Burn:燃尽图'''
    if name == 'Burn':
        burn = Burn()


if __name__ == "__main__":
    fire.Fire(method_selecter)
