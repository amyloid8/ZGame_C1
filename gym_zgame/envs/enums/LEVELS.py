from enum import IntEnum
import random
import warnings


class LEVELS(IntEnum):
    level_Dict = {'NONE':0,'FEW':1,'MANY':2}

    @staticmethod
    def print():
        for key in level_Dict:
            print('{0} -> {1}'.format(key, level_Dict[key]))

    @classmethod
    def get_random(cls):
        return random.choice(level_Dict.keys())

    @staticmethod
    def get_value_from_string(level):
        if level.upper() in level_Dict:
            return level_Dict[level.upper()]
        else:
            warnings.warn('String ({}) not in level_Dict; returned STAY'.format(level))
            return level_Dict['NONE']

    @staticmethod
    def get_name_from_string(level):
        if level.upper() in level_Dict:
            return level.upper()
        else:
            warnings.warn('String ({}) not in level_Dict; returned STAY'.format(level))
            return 'NONE'