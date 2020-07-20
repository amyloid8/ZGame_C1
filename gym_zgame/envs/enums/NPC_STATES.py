import random
import warnings


class NPC_STATES_DEAD:
    dead_state_Dict = {'ALIVE':0,'DEAD':1,'ASHEN':2}

    @staticmethod
    def print():
        for key in dead_state_Dict:
            print('{0} -> {1}'.format(key, dead_state_Dict[key]))

    @classmethod
    def get_random(cls):
        return random.choice(dead_state_Dict.keys())

    @staticmethod
    def get_value_from_string(state):
        if state.upper() in dead_state_Dict:
            return dead_state_Dict[state.upper()]
        else:
            warnings.warn('String ({}) not in dead_state_Dict; returned ALIVE'.format(state))
            return dead_state_Dict['ALIVE']

    @staticmethod
    def get_name_from_string(state):
        if state.upper() in dead_state_Dict:
            return state.upper()
        else:
            warnings.warn('String ({}) not in dead_state_Dict; returned ALIVE'.format(state))
            return 'ALIVE'


class NPC_STATES_ZOMBIE:
    zombie_state_Dict = {'HUMAN':0,'ZOMBIE_BITTEN':1,'ZOMBIE':2}

    @staticmethod
    def print():
        for key in zombie_state_Dict:
            print('{0} -> {1}'.format(key, zombie_state_Dict[key]))

    @classmethod
    def get_random(cls):
        return random.choice(zombie_state_Dict.keys())

    @staticmethod
    def get_value_from_string(state):
        if state.upper() in zombie_state_Dict:
            return zombie_state_Dict[state.upper()]
        else:
            warnings.warn('String ({}) not in zombie_state_Dict; returned HUMAN'.format(state))
            return 'HUMAN'
    @staticmethod
    def get_name_from_string(state):
        if state.upper() in zombie_state_Dict:
            return state.upper()
        else:
            warnings.warn('String ({}) not in zombie_state_Dict; returned HUMAN'.format(state))
            return 'HUMAN'


class NPC_STATES_FLU:
    flu_state_Dict = {'HEALTHY':0,'INCUBATING':1,'FLU':2,'IMMUNE':3}

    @staticmethod
    def print():
        for key in flu_state_Dict:
            print('{0} -> {1}'.format(key, flu_state_Dict[key]))

    @classmethod
    def get_random(cls):
        return random.choice(flu_state_Dict.keys())

    @staticmethod
    def get_value_from_string(state):
        if state.upper() in flu_state_Dict:
            return flu_state_Dict[state.upper()]
        else:
            warnings.warn('String ({}) not in flu_state_Dict; returned HEALTHY'.format(state))
            return flu_state_Dict['HEALTHY']

    @staticmethod
    def get_name_from_string(state):
        if state.upper() in flu_state_Dict:
            return state.upper()
        else:
            warnings.warn('String ({}) not in flu_state_Dict; returned HEALTHY'.format(state))
            return 'HEALTHY'
