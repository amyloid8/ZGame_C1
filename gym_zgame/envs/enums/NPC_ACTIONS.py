import random
import warnings
from gym_zgame.envs.enums.PLAYER_ACTIONS import LOCATIONS


class NPC_ACTIONS():
    action_Dict = {'STAY': 0, 'N': 1,'S':2,"E":3,"W":4}

    @staticmethod
    def print():
        for key in action_Dict:
            print('{0} -> {1}'.format(key, action_Dict[key]))

    @classmethod
    def get_random(cls):
        return random.choice(list(NPC_ACTIONS))

    @staticmethod
    def get_value_from_string(action):
        if action.upper() in action_Dict:
            return action_Dict[action]
        else:
            warnings.warn('Tried to convert string ({}) to NPC_ACTIONS enum and failed; returned STAY'.format(action))
            return action_Dict['STAY']

    @staticmethod
    def get_name_from_string(action):
        if action.upper() in action_Dict:
            return action.upper()
        else:
            warnings.warn('Tried to convert string ({}) to NPC_ACTIONS enum and failed; returned STAY'.format(action))
            return 'STAY'

    @staticmethod
    def reverse_action(npc_action):
        if npc_action is 'N':
            return 'S'
        if npc_action is 'S':
            return 'N'
        if npc_action is 'E':
            return 'W'
        if npc_action is 'W':
            return 'E'
        if npc_action is 'STAY':
            return 'STAY'
