import json
import uuid
import gym
import gym_zgame
from gym_zgame.envs.enums.PLAY_TYPE import PLAY_TYPE
from gym_zgame.envs.enums.PLAYER_ACTIONS import LOCATIONS, DEPLOYMENTS
from tkinter import *

class GUI(Frame):

    def __init__(self, zgame, master):
        super(GUI, self).__init__(master)
        self.env = zgame.env
        self.GAME_ID = zgame.GAME_ID
        self.turn = zgame.turn
        self.max_turns = zgame.max_turns
        self.DATA_LOG_FILE_NAME = zgame.DATA_LOG_FILE_NAME


        self.grid()
        self.env.reset()
        self.create_widgets()

    def create_widgets(self):
        print('Starting new game with human play!')
        str = self.env.render(mode='human')
        Label(self, text = str).grid(row = 0, column = 0, columnspan = 4, sticky = W)

        Label(self, text = "location 1").grid(row = 1, column = 0, columnspan = 1, sticky = W)
        self.loc1 = Entry(self)
        self.loc1.grid(row=1, column = 1, columnspan = 1, sticky = W)

        Label(self, text="deployment 1").grid(row=1, column=2, columnspan=1, sticky=W)
        self.dep1 = Entry(self)
        self.dep1.grid(row=1, column=3, columnspan=1, sticky=W)

        Label(self, text="location 2").grid(row=2, column=0, columnspan=1, sticky=W)
        self.loc2 = Entry(self)
        self.loc2.grid(row=2, column=1, columnspan=1, sticky=W)

        Label(self, text="deployment 2").grid(row=2, column=2, columnspan=1, sticky=W)
        self.dep2 = Entry(self)
        self.dep2.grid(row=2, column=3, columnspan=1, sticky=W)

        Button(self, text = "Next step", command = self.update).grid(row = 3, column = 1, sticky = W)
        Button(self, text = "Quit", command = self.quit).grid(row = 3, column = 2, sticky = W)

    def quit(self):
        for widget in self.winfo_children():
            widget.destroy()
        Label(self, text = "Please exit the game manually").grid(row = 0, column = 0, sticky = W)

    def update(self):
        self.env.print_player_action_selections()
        location_1 = int(self.loc1.get())
        deployment_1 = int(self.dep1.get())
        location_2 = int(self.loc2.get())
        deployment_2 = int(self.dep2.get())
        actions = self.env.encode_raw_action(location_1=LOCATIONS(location_1),
                                             deployment_1=DEPLOYMENTS(deployment_1),
                                             location_2=LOCATIONS(location_2),
                                             deployment_2=DEPLOYMENTS(deployment_2))
        observation, reward, done, info = self.env.step(actions)
        print(info)
        self.env.render(mode='human')
        self.create_widgets()

        # Write action and stuff out to disk.
        data_to_log = {
            'game_id': str(self.GAME_ID),
            'step': self.turn,
            'actions': actions,
            'reward': reward,
            'game_done': done,
            'game_info': {k.replace('.', '_'): v for (k, v) in info.items()},
            'raw_state': observation
        }
        with open(self.DATA_LOG_FILE_NAME, 'a') as f_:
            f_.write(json.dumps(data_to_log) + '\n')

        # Update counter
        self.turn += 1
        if done:
            self.quit()


    """def update(self):
        for turn in range(self.max_turns):
            self.env.print_player_action_selections()
            location_1 = self.loc1.get("1.0", END)
            deployment_1 = self.dep1.get("1.0", END)
            location_2 = self.loc2.get("1.0", END)
            deployment_2 = self.dep2.get("1.0", END)
            actions = self.env.encode_raw_action(location_1=LOCATIONS(location_1),
                                                 deployment_1=DEPLOYMENTS(deployment_1),
                                                 location_2=LOCATIONS(location_2),
                                                 deployment_2=DEPLOYMENTS(deployment_2))
            observation, reward, done, info = self.env.step(actions)
            print(info)
            self.env.render(mode='human')

            # Write action and stuff out to disk.
            data_to_log = {
                'game_id': str(self.GAME_ID),
                'step': self.turn,
                'actions': actions,
                'reward': reward,
                'game_done': done,
                'game_info': {k.replace('.', '_'): v for (k, v) in info.items()},
                'raw_state': observation
            }
            with open(self.DATA_LOG_FILE_NAME, 'a') as f_:
                f_.write(json.dumps(data_to_log) + '\n')

            # Update counter
            self.turn += 1
            if done:
                self.done()
                break"""



