import numpy as np
import json
import pandas as pd
import matplotlib.pyplot as plt
from gym_zgame.envs.enums.PLAYER_ACTIONS import DEPLOYMENTS


class DataAnalyzer:

    def __init__(self, log_filename, config_filename):
        self.CONFIG_FILENAME = config_filename
        temp = pd.read_json(log_filename, lines=True)
        self.all_data = pd.DataFrame(temp)

        self.config = {}
        with open(self.CONFIG_FILENAME) as file:
            data = json.load(file)
            self.config.update(data)
        self.steps = self.config["num_steps"]
        self.envs = self.config["num_envs"]
        self.interval = self.config["train_collection_interval"]

        # self.ids = self.all_data['game ID']
        self.score = self.all_data['total_score']
        self.dep_record = self.all_data['deployments']
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
        length = (self.steps * self.envs)//self.interval
        print(self.all_data)
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

        axs[0].legend(['Alive', 'Dead', 'Ashen'])
        axs[1].legend(['Human', 'Zombie'])
        axs[2].legend(['Healthy', 'Flu', 'Immune'])
        plt.xlabel('Steps')
        plt.ylabel('Number of NPC type')

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
    analyzer = DataAnalyzer('train_info.json', 'play_config.json')
    analyzer.graph_population()