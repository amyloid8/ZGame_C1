from enum import IntEnum
import random
import warnings


class NPC_STATES_DEAD(IntEnum):
    ALIVE = 0
    DEAD = 1
    ASHEN = 2

    @staticmethod
    def print():
        for state in NPC_STATES_DEAD:
            print('{0} -> {1}'.format(state.value, state.name))

    @classmethod
    def get_random(cls):
        return random.choice(list(NPC_STATES_DEAD))

    @staticmethod
    def get_value_from_string(state):
        if state.upper() == 'ALIVE':
            return NPC_STATES_DEAD.ALIVE.value
        elif state.upper() == 'DEAD':
            return NPC_STATES_DEAD.DEAD.value
        elif state.upper() == 'ASHEN':
            return NPC_STATES_DEAD.ASHEN.value
        else:
            warnings.warn('Tried to convert string ({}) to NPC_STATES_DEAD enum and failed; returned ALIVE'.format(state))
            return NPC_STATES_DEAD.ALIVE.value

    @staticmethod
    def get_name_from_string(state):
        if state.upper() == 'ALIVE':
            return NPC_STATES_DEAD.ALIVE.name
        elif state.upper() == 'DEAD':
            return NPC_STATES_DEAD.DEAD.name
        elif state.upper() == 'ASHEN':
            return NPC_STATES_DEAD.ASHEN.name
        else:
            warnings.warn('Tried to convert string ({}) to NPC_STATES_DEAD enum and failed; returned ALIVE'.format(state))
            return NPC_STATES_DEAD.ALIVE.name


class NPC_STATES_ZOMBIE(IntEnum):
    HUMAN = 0
    ZOMBIE_BITTEN = 1
    ZOMBIE = 2

    @staticmethod
    def print():
        for state in NPC_STATES_ZOMBIE:
            print('{0} -> {1}'.format(state.value, state.name))

    @classmethod
    def get_random(cls):
        return random.choice(list(NPC_STATES_ZOMBIE))

    @staticmethod
    def get_value_from_string(state):
        if state.upper() == 'HUMAN':
            return NPC_STATES_ZOMBIE.HUMAN.value
        elif state.upper() == 'ZOMBIE_BITTEN':
            return NPC_STATES_ZOMBIE.ZOMBIE_BITTEN.value
        elif state.upper() == 'ZOMBIE':
            return NPC_STATES_ZOMBIE.ZOMBIE.value
        else:
            warnings.warn('Tried to convert string ({}) to NPC_STATES_ZOMBIE enum and failed; returned HUMAN'.format(state))
            return NPC_STATES_ZOMBIE.HUMAN.value

    @staticmethod
    def get_name_from_string(state):
        if state.upper() == 'HUMAN':
            return NPC_STATES_ZOMBIE.HUMAN.name
        elif state.upper() == 'ZOMBIE_BITTEN':
            return NPC_STATES_ZOMBIE.ZOMBIE_BITTEN.name
        elif state.upper() == 'ZOMBIE':
            return NPC_STATES_ZOMBIE.ZOMBIE.name
        else:
            warnings.warn('Tried to convert string ({}) to NPC_STATES_ZOMBIE enum and failed; returned HUMAN'.format(state))
            return NPC_STATES_ZOMBIE.HUMAN.name


class NPC_STATES_FLU(IntEnum):
    HEALTHY = 0
    INCUBATING = 1
    FLU = 2
    IMMUNE = 3

    @staticmethod
    def print():
        for state in NPC_STATES_FLU:
            print('{0} -> {1}'.format(state.value, state.name))

    @classmethod
    def get_random(cls):
        return random.choice(list(NPC_STATES_FLU))

    @staticmethod
    def get_value_from_string(state):
        if state.upper() == 'HEALTHY':
            return NPC_STATES_FLU.HEALTHY.value
        elif state.upper() == 'INCUBATING':
            return NPC_STATES_FLU.INCUBATING.value
        elif state.upper() == 'FLU':
            return NPC_STATES_FLU.FLU.value
        elif state.upper() == 'IMMUNE':
            return NPC_STATES_FLU.IMMUNE.value
        else:
            warnings.warn('Tried to convert string ({}) to NPC_STATES_FLU enum and failed; returned HEALTHY'.format(state))
            return NPC_STATES_FLU.HEALTHY.value

    @staticmethod
    def get_name_from_string(state):
        if state.upper() == 'HEALTHY':
            return NPC_STATES_FLU.HEALTHY.name
        elif state.upper() == 'INCUBATING':
            return NPC_STATES_FLU.INCUBATING.name
        elif state.upper() == 'FLU':
            return NPC_STATES_FLU.FLU.name
        elif state.upper() == 'IMMUNE':
            return NPC_STATES_FLU.IMMUNE.name
        else:
            warnings.warn('Tried to convert string ({}) to NPC_STATES_FLU enum and failed; returned HEALTHY'.format(state))
            return NPC_STATES_FLU.HEALTHY.name
