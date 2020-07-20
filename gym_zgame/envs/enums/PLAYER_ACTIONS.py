from enum import IntEnum
import random
import warnings


class DEPLOYMENTS(IntEnum):
    deployment_Dict = {'NONE':0,
    'QUARANTINE_OPEN':1,
    'QUARANTINE_FENCED':2,
    'BITE_CENTER_DISINFECT':3,
    'BITE_CENTER_AMPUTATE':4,
    'Z_CURE_CENTER_FDA':5,
    'Z_CURE_CENTER_EXP':6,
    'FLU_VACCINE_OPT':7,
    'FLU_VACCINE_MAN':8,
    'KILN_OVERSIGHT':9,
    'KILN_NO_QUESTIONS':10,
    'BROADCAST_DONT_PANIC':11,
    'BROADCAST_CALL_TO_ARMS':12,
    'SNIPER_TOWER_CONFIRM':3,
    'SNIPER_TOWER_FREE':14,
    'PHEROMONES_BRAINS':15,
    'PHEROMONES_MEAT':16,
    'BSL4LAB_SAFETY_ON':17,
    'BSL4LAB_SAFETY_OFF':18,
    'RALLY_POINT_OPT':19,
    'RALLY_POINT_FULL':20,
    'FIREBOMB_PRIMED':21,
    'FIREBOMB_BARRAGE':22,
    'SOCIAL_DISTANCING_SIGNS':23,
    'SOCIAL_DISTANCING_CELEBRITY':24}

    @staticmethod
    def print():
        for key in deployment_Dict:
            print('{0} -> {1}'.format(key, deployment_Dict[key]))

    @classmethod
    def get_random(cls):
        return random.choice(deployment_Dict.keys())

    @staticmethod
    def get_value_from_string(deployment):
        if deployment.upper() in deployment_Dict:
            return deployment_Dict[deployment.upper()]    
        else:
            warnings.warn('String ({}) not in deployment_Dict; returned NONE'.format(deployment))
            return deployment_Dict['NONE']

    @staticmethod
    def get_name_from_string(deployment):
        if deployment.upper() in deployment_Dict:
            return deployment.upper() 
        else:
            warnings.warn('String ({}) not in deployment_Dict; returned NONE'.format(deployment))
            return 'NONE'


class LOCATIONS(IntEnum):
    location_Dict = {'CENTER':0,
    'N':1,
    'S':2,
    'E':3,
    'W':4,
    'NE':5,
    'NW':6,
    'SE':7,
    'SW':8}

    @staticmethod
    def print():
        for key in location_Dict:
            print('{0} -> {1}'.format(key, location_Dict[key]))

    @classmethod
    def get_random(cls):
        return random.choice(location_Dict.keys())

    @staticmethod
    def get_value_from_string(location):
        if location.upper() in location_Dict:
            return location_Dict[location.upper()]    
        else:
            warnings.warn('String ({}) not in location_Dict; returned CENTER'.format(location))
            return location_Dict['CENTER']

    @staticmethod
    def get_name_from_string(location):
        if location.upper() in location_Dict:
            return location.upper() 
        else:
            warnings.warn('String ({}) not in location_Dict; returned CENTER'.format(location))
            return 'CENTER'
