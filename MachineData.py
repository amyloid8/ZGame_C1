import numpy as np
import json
import pandas as pd
import matplotlib.pyplot as plt
from gym_zgame.envs.enums.PLAYER_ACTIONS import DEPLOYMENTS


class DataAnalyzer:

    def __init__(self, filename):

        temp = pd.read_json(filename, lines=True)
        self.all_data = pd.DataFrame(temp)

        self.ids = self.all_data['game ID']
        self.score = self.all_data['total score']
        self.dep_record = self.all_data['total deployments']
        self.reward = 0

        self.alive = self.all_data['alive']
        self.dead = self.all_data['dead']
        self.ashen = self.all_data['ashen']
        self.human = self.all_data['human']
        self.zombie = self.all_data['zombie']
        self.healthy = self.all_data['healthy']
        self.flu = self.all_data['flu']
        self.immune = self.all_data['immune']

    # def read_data(self):
    #     self.all_data = pd.read_json(filename, lines=True)
    #     # self.all_data = pd.read_json(self.ANALYSIS_FILENAME, lines=True)
    #     self.all_data = pd.DataFrame(self.all_data)

    def graph_population(self):
        df = self.all_data
        # ax1 = plt.gca()
        # ax2 = plt.gca()
        # ax3 = plt.gca()

        # df.plot(kind='line', x='game ID', y='alive', color='green', ax=ax1)
        # df.plot(kind='line', x='game ID', y='dead', color='red', ax=ax1)
        # df.plot(kind='line', x='game ID', y='ashen', color='black', ax=ax1)
        # df.plot(kind='line', x='game ID', y='human', color='green', ax=ax2)
        # df.plot(kind='line', x='game ID', y='zombie', color='purple', ax=ax2)
        # df.plot(kind='line', x='game ID', y='healthy', color='green', ax=ax3)
        # df.plot(kind='line', x='game ID', y='flu', color='red', ax=ax3)
        # df.plot(kind='line', x='game ID', y='immune', color='blue', ax=ax3)

        length = self.ids.count()
        game_num = list(range(1,length+1))
        fig, axs = plt.subplots(3, sharex=True, sharey=True)
        fig.suptitle('NPC Trends')
        axs[0].plot(game_num, self.alive)
        axs[0].plot(game_num, self.dead)
        axs[0].plot(game_num, self.ashen)
        axs[1].plot(game_num, self.human)
        axs[1].plot(game_num, self.zombie)
        axs[2].plot(game_num, self.healthy)
        axs[2].plot(game_num, self.flu)
        axs[2].plot(game_num, self.immune)

        plt.show()

        # plt.show()
        # df.plot.line()
        # plt.xlabel('game #')
        # plt.ylabel('number of npcs')
        # plt.title('NPCs')
        # plt.xticks(rotation=90)
        # # plt.tight_layout()
        # plt.show()

if __name__ == '__main__':
    analyzer = DataAnalyzer('analysis_info.json')
    analyzer.graph_population()