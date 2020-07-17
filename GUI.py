import json
import uuid
import gym
import gym_zgame
from gym_zgame.envs.enums.PLAY_TYPE import PLAY_TYPE
from gym_zgame.envs.enums.PLAYER_ACTIONS import LOCATIONS, DEPLOYMENTS
from tkinter import *
import pyfiglet as pf
import gym_zgame.envs.model.City

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
        self.neighborhoods, self.fear, self.resources, self.orig_alive, self.orig_dead, self.score, self.total_score = self.env.city.getNeiborhoods()
        str = self.env.render(mode='human')
        self.env.print_player_action_selections()

        #Label(self, text = str).grid(row = 0, column = 0, columnspan = 4, sticky = W)
        Label(self, text = "", bg = "blue", width = 65).grid(row = 19, column = 0, columnspan = 3, sticky = W)
        Label(self, text = "", bg = "blue", width = 65).grid(row = 21, column = 0, columnspan = 3, sticky = W)
        Label(self, text = "", bg = "blue", width = 65).grid(row = 23, column = 0, columnspan = 3, sticky = W)
        Label(self, text = "", bg = "blue", width = 65).grid(row = 25, column = 0, columnspan = 3, sticky = W)

        self.grid3by3()


        Label(self, text = "", bg = "red", width = 65).grid(row = 0, column = 0, columnspan = 3, sticky = W)
        Label(self, text = "ZGAME Status", font = 'Chalkduster 50', justify = LEFT, width = 1).grid(row = 1, column = 0, columnspan = 3, sticky = E+S+W)
        Label(self, text = "", bg = "red", width = 65).grid(row =9, column = 0, columnspan = 3, sticky = S)

        Label(self, text = "Global Status", bg = "pink", width = 65).grid(row = 10, column = 0, columnspan = 3, sticky = N)
        Label(self, text = "", bg = "pink", width = 65).grid(row = 18, column = 0, columnspan = 3, sticky = N)


        str = ' Turn: {0} of {1}'.format(self.turn, self.max_turns)\
              + '\n Fear: {}'.format(self.fear)\
              + '\n Resources: {}'.format(self.resources)
        Label(self, text = str, justify = LEFT).grid(row = 11, column = 0, sticky = W)

        str =  'Turn Score: {0} (Total Score: {1})'.format(self.score, self.total_score)\
               + '\nLiving at Start: {}'.format(self.orig_alive)\
               + '\nDead at Start: {}'.format(self.orig_dead)
        Label(self, text = str, justify = LEFT).grid(row = 11, column = 1,columnspan = 3, sticky = W)

        Label(self, text = " ",bg="green", height = 48).grid(row = 0, column = 3, rowspan = 30, sticky = W)
        loc_str = ""
        for i in range(9):
            loc_str += "{0} - {1}\n".format(LOCATIONS(i).value,LOCATIONS(i).name)

        Label(self, text = loc_str, justify = LEFT).grid(row = 0, column = 4, rowspan = 30, sticky = W)

        Label(self, text = " ",bg="green", height = 48).grid(row = 0, column = 5, rowspan = 30, sticky = W)
        dep_str = ""
        for i in range(25):
            dep_str += "{0} - {1}\n".format(DEPLOYMENTS(i).value,DEPLOYMENTS(i).name)

        Label(self, text = dep_str, justify = LEFT).grid(row = 0, column = 6, rowspan = 30, sticky = W)

        Label(self, text = " ",bg="green", height = 48).grid(row = 0, column = 7, rowspan = 30, sticky = W)



        Label(self, text = "location 1").grid(row = 26, column = 0, columnspan = 1, sticky = W)
        self.loc1 = Entry(self)
        self.loc1.grid(row=26, column = 1, columnspan = 1, sticky = W)

        Label(self, text="deployment 1").grid(row=27, column=0, columnspan=1, sticky=W)
        self.dep1 = Entry(self)
        self.dep1.grid(row=27, column=1, columnspan=1, sticky=W)

        Label(self, text="location 2").grid(row=28, column=0, columnspan=1, sticky=W)
        self.loc2 = Entry(self)
        self.loc2.grid(row=28, column=1, columnspan=1, sticky=W)

        Label(self, text="deployment 2").grid(row=29, column=0, columnspan=1, sticky=W)
        self.dep2 = Entry(self)
        self.dep2.grid(row=29, column=1, columnspan=1, sticky=W)

        Button(self, text = "Next step", command = self.update).grid(row = 26, column = 2, rowspan = 2, sticky = N+E+W+S)
        Button(self, text = "Quit", command = self.quit).grid(row = 28, column = 2, rowspan = 2, sticky = N+E+W+S)

    def grid3by3(self):

        nbh_c = None
        nbh_n = None
        nbh_s = None
        nbh_e = None
        nbh_w = None
        nbh_ne = None
        nbh_nw = None
        nbh_se = None
        nbh_sw = None
        for nbh in self.neighborhoods:
            nbh_c = nbh if nbh.location is LOCATIONS.CENTER else nbh_c
            nbh_n = nbh if nbh.location is LOCATIONS.N else nbh_n
            nbh_s = nbh if nbh.location is LOCATIONS.S else nbh_s
            nbh_e = nbh if nbh.location is LOCATIONS.E else nbh_e
            nbh_w = nbh if nbh.location is LOCATIONS.W else nbh_w
            nbh_ne = nbh if nbh.location is LOCATIONS.NE else nbh_ne
            nbh_nw = nbh if nbh.location is LOCATIONS.NW else nbh_nw
            nbh_se = nbh if nbh.location is LOCATIONS.SE else nbh_se
            nbh_sw = nbh if nbh.location is LOCATIONS.SW else nbh_sw

        Label(self,
              text = "Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5}"\
              .format(self.env.city.mask_visible_data(nbh_nw.num_active).name,
                      self.env.city.mask_visible_data(nbh_nw.num_sickly).name,
                      self.env.city.mask_visible_data(nbh_nw.num_zombie).name,
                      self.env.city.mask_visible_data(nbh_nw.num_dead).name,
                      nbh_nw.orig_alive,
                      nbh_nw.orig_dead), justify = LEFT
              ).grid(row = 20, column = 0, sticky = W)

        Label(self,
              text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5}" \
              .format(self.env.city.mask_visible_data(nbh_n.num_active).name,
                      self.env.city.mask_visible_data(nbh_n.num_sickly).name,
                      self.env.city.mask_visible_data(nbh_n.num_zombie).name,
                      self.env.city.mask_visible_data(nbh_n.num_dead).name,
                      nbh_n.orig_alive,
                      nbh_n.orig_dead), justify = LEFT
              ).grid(row=20, column=1, sticky=W)

        Label(self,
              text = "Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5}" \
            .format(self.env.city.mask_visible_data(nbh_ne.num_active).name,
                    self.env.city.mask_visible_data(nbh_ne.num_sickly).name,
                    self.env.city.mask_visible_data(nbh_ne.num_zombie).name,
                    self.env.city.mask_visible_data(nbh_ne.num_dead).name,
                    nbh_ne.orig_alive,
                    nbh_ne.orig_dead), justify = LEFT
        ).grid(row=20, column=2, sticky=W)

        Label(self,
              text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5}" \
              .format(self.env.city.mask_visible_data(nbh_w.num_active).name,
                      self.env.city.mask_visible_data(nbh_w.num_sickly).name,
                      self.env.city.mask_visible_data(nbh_w.num_zombie).name,
                      self.env.city.mask_visible_data(nbh_w.num_dead).name,
                      nbh_w.orig_alive,
                      nbh_w.orig_dead), justify=LEFT
              ).grid(row=22, column=0, sticky=W)

        Label(self,
              text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5}" \
              .format(self.env.city.mask_visible_data(nbh_c.num_active).name,
                      self.env.city.mask_visible_data(nbh_c.num_sickly).name,
                      self.env.city.mask_visible_data(nbh_c.num_zombie).name,
                      self.env.city.mask_visible_data(nbh_c.num_dead).name,
                      nbh_c.orig_alive,
                      nbh_c.orig_dead), justify=LEFT
              ).grid(row=22, column=1, sticky=W)

        Label(self,
              text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5}" \
              .format(self.env.city.mask_visible_data(nbh_e.num_active).name,
                      self.env.city.mask_visible_data(nbh_e.num_sickly).name,
                      self.env.city.mask_visible_data(nbh_e.num_zombie).name,
                      self.env.city.mask_visible_data(nbh_e.num_dead).name,
                      nbh_e.orig_alive,
                      nbh_e.orig_dead), justify=LEFT
              ).grid(row=22, column=2, sticky=W)

        Label(self,
              text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5}" \
              .format(self.env.city.mask_visible_data(nbh_sw.num_active).name,
                      self.env.city.mask_visible_data(nbh_sw.num_sickly).name,
                      self.env.city.mask_visible_data(nbh_sw.num_zombie).name,
                      self.env.city.mask_visible_data(nbh_sw.num_dead).name,
                      nbh_sw.orig_alive,
                      nbh_sw.orig_dead), justify=LEFT
              ).grid(row=24, column=0, sticky=W)

        Label(self,
              text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5}" \
              .format(self.env.city.mask_visible_data(nbh_s.num_active).name,
                      self.env.city.mask_visible_data(nbh_s.num_sickly).name,
                      self.env.city.mask_visible_data(nbh_s.num_zombie).name,
                      self.env.city.mask_visible_data(nbh_s.num_dead).name,
                      nbh_s.orig_alive,
                      nbh_s.orig_dead), justify=LEFT
              ).grid(row=24, column=1, sticky=W)

        Label(self,
              text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5}" \
              .format(self.env.city.mask_visible_data(nbh_se.num_active).name,
                      self.env.city.mask_visible_data(nbh_se.num_sickly).name,
                      self.env.city.mask_visible_data(nbh_se.num_zombie).name,
                      self.env.city.mask_visible_data(nbh_se.num_dead).name,
                      nbh_se.orig_alive,
                      nbh_se.orig_dead), justify=LEFT
              ).grid(row=24, column=2, sticky=W)

    def quit(self):
        self.winfo_children()[0].quit()
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
        self.neighborhoods, self.fear, self.resources, self.orig_alive, self.orig_dead, self.score, self.total_score = self.env.city.getNeiborhoods()

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
