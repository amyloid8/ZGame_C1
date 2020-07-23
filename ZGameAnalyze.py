import gym
import math
from gym_zgame.envs.model.City import City
from gym_zgame.envs.model.Neighborhood import Neighborhood
import json
import numpy as np
import ZGameHumanPlay, ZGameMachinePlay, ZGameMachineTrain
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

import pandas as pd

class Analyzer:

    def __init__(self, filename='data_log.json'):
        # self.all_data = pd.read_json(filename, lines=True)
        self.FILENAME = filename
        self.all_data = pd.read_json(self.FILENAME, lines=True)

    def get_categories():
        cols = self.all_data.columns
        categories = list(cols)
        print(categories)

    def get_category_data(category):
        data = self.all_data
        category_data = data[category]
        category_data.head()
        print(category_data)

    def get_rewards():
        data = self.all_data
        rewards = all_data['reward']
        print(rewards)

    def get_action_history():
        return Neighborhood.get_dep_history()

