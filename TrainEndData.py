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
        self.actions_count = {}

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
        # length = 1000
        print(self.all_data)
        game_num = list(range(1,length+1))
        fig, axs = plt.subplots(3, sharex=True, sharey=True)
        fig.suptitle('NPC Trends')
        axs[0].plot(game_num, self.alive, color='green')
        axs[0].plot(game_num, self.dead, color='red')
        axs[0].plot(game_num, self.ashen, color='black')
        axs[1].plot(game_num, self.human, color='green')
        axs[1].plot(game_num, self.zombie, color='purple')
        axs[2].plot(game_num, self.healthy, color='green')
        axs[2].plot(game_num, self.flu, color='red')
        axs[2].plot(game_num, self.immune, color='blue')

        axs[0].legend(['Alive', 'Dead', 'Ashen'])
        axs[1].legend(['Human', 'Zombie'])
        axs[2].legend(['Healthy', 'Flu', 'Immune'])
        plt.xlabel('Steps')
        plt.ylabel('Number of NPC type')

        plt.show()

    def graph_dep_trends(self):
        # length = (self.steps * self.envs)//self.interval
        length = 5
        game_num = list(range(1,length+1))




        return

    def graph_dep_usage(self):
        print(self.actions_count)
        self.actions_count = self.get_dep_counts()
        actions_data = pd.DataFrame(self.actions_count, index=['# of uses'])
        actions_data = pd.DataFrame.sort_index(actions_data, 1)
        dep_names = []
        for dep in DEPLOYMENTS:
            for i in self.actions_count.keys():
                if i == dep.value:
                    dep_names.append(dep.name)
        y_values = []
        for i in self.actions_count.values():
            y_values.append(i)
        # plots # of uses of each deployment in one game
        plt.bar(dep_names, y_values)
        plt.xlabel('Deployment used')
        plt.ylabel('# of uses')
        plt.title('Total Deployment Usage')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()
        return

    def get_dep_counts(self):
        actions = self.dep_record
        print('hi')
        print(actions)
        actions_count = {}
        i = 0
        for i in range(len(DEPLOYMENTS)):
            actions_count.update({i: 0})
        for dep_list in actions:
            print(dep_list)
            for dep in dep_list:
                if dep in actions_count.keys():
                    actions_count[dep] += 1
        return actions_count


if __name__ == '__main__':
    analyzer = DataAnalyzer('train_info.json', 'play_config.json')
    # analyzer.graph_population()
    analyzer.get_dep_counts()
    analyzer.graph_dep_usage()