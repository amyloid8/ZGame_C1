import json
import uuid
import gym
import gym_zgame
from gym_zgame.envs.enums.PLAY_TYPE import PLAY_TYPE
from gym_zgame.envs.enums.PLAYER_ACTIONS import LOCATIONS, DEPLOYMENTS
from tkinter import *
import gym_zgame.envs.model.City


class GUI(Frame):

    def __init__(self, zgame, master):
        super(GUI, self).__init__(master)
        self.env = zgame.env
        self.neighborhoods, self.fear, self.resources, self.orig_alive, self.orig_dead, self.score, self.total_score = self.env.city.getNeiborhoods()
        self.GAME_ID = zgame.GAME_ID
        self.turn = zgame.turn
        self.max_turns = zgame.max_turns
        self.DATA_LOG_FILE_NAME = zgame.DATA_LOG_FILE_NAME
        self.grid()
        self.env.reset()
        self.create_widgets()

    def create_widgets(self):
        str = self.env.render(mode='human')
        right = Frame(self, bg='#86b8b0',padx=10,pady=10)
        right.grid(row=0, column=1)
        #GLOBAL INFO
        str = ' Turn: {0} of {1}'.format(self.turn, self.max_turns) \
              + '\n Fear: {}'.format(self.fear) \
              + '\n Resources: {}'.format(self.resources)
        Label(right, text=str, justify=LEFT, bg='#b886af').grid(row=3, column=3, columnspan=2, rowspan=3,padx=10,pady=10, ipadx=5,ipady=5)

        str = 'Turn Score: {0} (Total Score: {1})'.format(self.score, self.total_score) \
              + '\nLiving at Start: {}'.format(self.orig_alive) \
              + '\nDead at Start: {}'.format(self.orig_dead)
        Label(right, text=str, justify=LEFT, bg='#b886af').grid(row=6, column=3, rowspan=3, columnspan=2,padx=10,pady=10, ipadx=5,ipady=5)
        Label(right, text="Deployments", bg='#e32770').grid(row=0, column=0,padx=10,pady=10, ipadx=5,ipady=5)
        Label(right, text="Locations", bg='#e32770').grid(row=0, column=1, columnspan=2,padx=10,pady=10, ipadx=5,ipady=5)
        loc_str = ""
        for i in range(9):
            if i  is 8:
                loc_str += "{0} - {1}".format(LOCATIONS(i).value, LOCATIONS(i).name)
            else:
                loc_str += "{0} - {1}\n".format(LOCATIONS(i).value, LOCATIONS(i).name)

        Label(right, text=loc_str, justify=LEFT,bg='#dfcec2').grid(row=1, column=1, rowspan=10, columnspan=2,padx=10,pady=10, ipadx=5,ipady=5)
        dep_str = ""
        for i in range(25):
            if i is 24:
                dep_str += "{0} - {1}".format(DEPLOYMENTS(i).value, DEPLOYMENTS(i).name)
            else:
                dep_str += "{0} - {1}\n".format(DEPLOYMENTS(i).value, DEPLOYMENTS(i).name)
        Label(right, text=dep_str, justify=LEFT,bg='#dfcec2').grid(row=1, column=0, rowspan=24, padx=10,pady=10, ipadx=5,ipady=5)


        Label(right, text="Location 1", bg='#5e817b').grid(row=14, column=1, columnspan=2, rowspan=2,padx=10,pady=10, ipadx=5,ipady=5)
        loc1 = Entry(right, bg='#5e817b')
        loc1.grid(row=14, column=3, columnspan=2, rowspan=2,padx=10,pady=10)

        Label(right, text="Deployment 1", bg='#5e817b').grid(row=16, column=1, columnspan=2, rowspan=2,padx=10,pady=10, ipadx=5,ipady=5)
        dep1 = Entry(right, bg='#5e817b')
        dep1.grid(row=16, column=3, columnspan=2, rowspan=2,padx=10,pady=10)

        Label(right, text="Location 2", bg='#5e817b').grid(row=18, column=1, columnspan=2, rowspan=2,padx=10,pady=10, ipadx=5,ipady=5)
        loc2 = Entry(right, bg='#5e817b')
        loc2.grid(row=18, column=3, columnspan=2, rowspan=2,padx=10,pady=10)

        Label(right, text="Deployment 2", bg='#5e817b').grid(row=20, column=1, columnspan=2, rowspan=2,padx=10,pady=10, ipadx=5,ipady=5)
        dep2 = Entry(right, bg='#5e817b')
        dep2.grid(row=20, column=3, columnspan=2, rowspan=2,padx=10,pady=10)

        Button(right, text="Next step", command=self.update,height = 2, width = 40, bg='#b8ac86').grid(row=24, column=1, columnspan=4,rowspan=2,padx=10,pady=10)
        Button(right, text="Quit", command=self.quit,height = 2, width = 25, bg='#b8ac86').grid(row=0, column=3, columnspan=2,rowspan=1,padx=10,pady=10)

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
              text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5}" \
              .format(self.env.city.mask_visible_data(nbh_nw.num_active).name,
                      self.env.city.mask_visible_data(nbh_nw.num_sickly).name,
                      self.env.city.mask_visible_data(nbh_nw.num_zombie).name,
                      self.env.city.mask_visible_data(nbh_nw.num_dead).name,
                      nbh_nw.orig_alive,
                      nbh_nw.orig_dead), justify=LEFT
              ).grid(row=20, column=0, sticky=W)

        Label(self,
              text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5}" \
              .format(self.env.city.mask_visible_data(nbh_n.num_active).name,
                      self.env.city.mask_visible_data(nbh_n.num_sickly).name,
                      self.env.city.mask_visible_data(nbh_n.num_zombie).name,
                      self.env.city.mask_visible_data(nbh_n.num_dead).name,
                      nbh_n.orig_alive,
                      nbh_n.orig_dead), justify=LEFT
              ).grid(row=20, column=1, sticky=W)

        Label(self,
              text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5}" \
              .format(self.env.city.mask_visible_data(nbh_ne.num_active).name,
                      self.env.city.mask_visible_data(nbh_ne.num_sickly).name,
                      self.env.city.mask_visible_data(nbh_ne.num_zombie).name,
                      self.env.city.mask_visible_data(nbh_ne.num_dead).name,
                      nbh_ne.orig_alive,
                      nbh_ne.orig_dead), justify=LEFT
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

        # Button(self, text="Quit", command=self.quit).place(relx = 0.5, rely = 0.5)


    def quit(self):
        self.winfo_children()[0].quit()

    def update(self):
        # self.env.print_player_action_selections()
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

        # self.env.render(mode='human')
        self.create_widgets()