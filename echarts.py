import fire
from burn import Burn


def method_selecter(file_name, sheet_name):
    '''Burn:燃尽图'''
    if file_name == 'Burn':
        burn = Burn.Burn('Burn.xlsx', sheet_name)
        index, values = burn.get_data()
        velocities = burn.get_velocity(values)
        burn.draw(index, values, velocities)

if __name__ == "__main__":
    fire.Fire(method_selecter)
