import gym
import math
from gym_zgame.envs.model.City import City
import json
import numpy as np
import ZGameHumanPlay, ZGameMachinePlay, ZGameMachineTrain
import pandas as pd
import matplotlib.pyplot as plt
import os
from gym_zgame.envs.enums.PLAYER_ACTIONS import DEPLOYMENTS

import pandas as pd

class IndividualAnalyzer:

    def __init__(self, filename):
        self.all_data = pd.read_json(filename, lines=True)
        self.all_data = pd.DataFrame(self.all_data)

        self.games_list = []
        self.game_info = []
        self.DEP_NAMES = {}

    def get_categories(self):
        categories = list(self.all_data.columns)
        print(categories)

    def get_category_data(self, category):
        category_data = self.all_data[category]
        category_data.head()
        print(category_data)

    def get_rewards(self):
        rewards = self.all_data['reward']
        print(rewards)
        return rewards

    # gets frequency of deployment usage
    def get_actions_count(self):
        actions = self.all_data['deployments']
        print(actions)
        actions_count = {}
        i = 0
        for i in range(len(DEPLOYMENTS)):
            actions_count.update({i:0})
        for deployments in actions:
            for dep in deployments:
                if dep in actions_count.keys():
                    actions_count[dep] += 1
        actions_data = pd.DataFrame(actions_count, index=['# of uses'])
        actions_data = pd.DataFrame.sort_index(actions_data, 1)
        dep_names = []
        for dep in DEPLOYMENTS:
            for i in actions_count.keys():
                if i == dep.value:
                    dep_names.append(dep.name)
        y_values = []
        for i in actions_count.values():
            y_values.append(i)
        # plots # of uses of each deployment in one game
        plt.bar(dep_names, y_values)
        plt.xlabel('Deployment used')
        plt.ylabel('# of uses')
        plt.title('Deployment Usage')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

        return actions_count




# import matplotlib.pyplot as plt
# plt.ion()
# class DynamicUpdate():
#     #Suppose we know the x range
#     min_x = 0
#     max_x = 10
#
#     def on_launch(self):
#         #Set up plot
#         self.figure, self.ax = plt.subplots()
#         self.lines, = self.ax.plot([],[], 'o')
#         #Autoscale on unknown axis and known lims on the other
#         self.ax.set_autoscaley_on(True)
#         self.ax.set_xlim(self.min_x, self.max_x)
#         #Other stuff
#         self.ax.grid()
#         ...
#
#     def on_running(self, xdata, ydata):
#         #Update data (with the new _and_ the old points)
#         self.lines.set_xdata(xdata)
#         self.lines.set_ydata(ydata)
#         #Need both of these in order to rescale
#         self.ax.relim()
#         self.ax.autoscale_view()
#         #We need to draw *and* flush
#         self.figure.canvas.draw()
#         self.figure.canvas.flush_events()
#
#     #Example
#     def __call__(self):
#         import numpy as np
#         import time
#         self.on_launch()
#         xdata = []
#         ydata = []
#         for x in np.arange(0,10,0.5):
#             xdata.append(x)
#             ydata.append(np.exp(-x**2)+10*np.exp(-(x-7)**2))
#             self.on_running(xdata, ydata)
#             time.sleep(1)
#         return xdata, ydata
#
# d = DynamicUpdate()
# d()



if __name__ == '__main__':
    a = IndividualAnalyzer('train_info.json')
    a.get_rewards()
    a.get_category_data('deployments')
    a.get_categories()
    a.get_actions_count()

