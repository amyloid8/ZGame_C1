from enum import IntEnum
import random
import warnings
from gym_zgame.envs.enums.PLAYER_ACTIONS import LOCATIONS


class NPC_ACTIONS(IntEnum):
    STAY = 0
    N = 1
    S = 2
    E = 3
    W = 4

    @staticmethod
    def print():
        for action in NPC_ACTIONS:
            print('{0} -> {1}'.format(action.value, action.name))

    @classmethod
    def get_random(cls):
        return random.choice(list(NPC_ACTIONS))

    @staticmethod
    def get_value_from_string(action):
        if action.upper() == 'STAY':
            return NPC_ACTIONS.STAY.value
        elif action.upper() == 'N':
            return NPC_ACTIONS.N.value
        elif action.upper() == 'S':
            return NPC_ACTIONS.S.value
        elif action.upper() == 'E':
            return NPC_ACTIONS.E.value
        elif action.upper() == 'W':
            return NPC_ACTIONS.W.value
        else:
            warnings.warn('Tried to convert string ({}) to NPC_ACTIONS enum and failed; returned STAY'.format(action))
            return NPC_ACTIONS.STAY.value

    @staticmethod
    def get_name_from_string(action):
        if action.upper() == 'STAY':
            return NPC_ACTIONS.STAY.name
        elif action.upper() == 'N':
            return NPC_ACTIONS.N.name
        elif action.upper() == 'S':
            return NPC_ACTIONS.S.name
        elif action.upper() == 'E':
            return NPC_ACTIONS.E.name
        elif action.upper() == 'W':
            return NPC_ACTIONS.W.name
        else:
            warnings.warn('Tried to convert string ({}) to NPC_ACTIONS enum and failed; returned STAY'.format(action))
            return NPC_ACTIONS.STAY.name

    @staticmethod
    def reverse_action(npc_action):
        if npc_action is NPC_ACTIONS.N:
            return NPC_ACTIONS.S
        if npc_action is NPC_ACTIONS.S:
            return NPC_ACTIONS.N
        if npc_action is NPC_ACTIONS.E:
            return NPC_ACTIONS.W
        if npc_action is NPC_ACTIONS.W:
            return NPC_ACTIONS.E
        if npc_action is NPC_ACTIONS.STAY:
            return NPC_ACTIONS.STAY
