import json
import uuid
import gym
import gym_zgame
from gym_zgame.envs.enums.PLAY_TYPE import PLAY_TYPE
from gym_zgame.envs.enums.PLAYER_ACTIONS import LOCATIONS, DEPLOYMENTS
from tkinter import *
import gym_zgame.envs.model.City
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




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
        self.list_active = []
        self.list_sickly = []
        self.list_dead = []
        self.list_zombie = []
        self.xlist = []
        self.create_widgets()

    def create_widgets(self):
        # cmd line UI
        print(self.env.render(mode='human'))

        # left frame (titles and tables)
        left = Frame(self)
        left.grid(row=0, column=0)

        title = Frame(left, bg="red")
        title.grid(row=0, column=0)

        tables = Frame(left, bg="blue", width = 21)
        tables.grid(row=1, column=0)

        # print title "ZGAME"
        Label(title, text="ZGAME", font='Chalkduster 35', justify=LEFT, width=21).grid(row=0, column=0, padx=(6,7), pady=(6,7))

        #print 3 by 3 tables of neighborhoods
        self.grid3by3(tables)

        right = Frame(self, bg='#86b8b0',padx=10,pady=44)
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
        self.loc1 = Entry(right, bg='#5e817b')
        self.loc1.grid(row=14, column=3, columnspan=2, rowspan=2,padx=10,pady=10)

        Label(right, text="Deployment 1", bg='#5e817b').grid(row=16, column=1, columnspan=2, rowspan=2,padx=10,pady=10, ipadx=5,ipady=5)
        self.dep1 = Entry(right, bg='#5e817b')
        self.dep1.grid(row=16, column=3, columnspan=2, rowspan=2,padx=10,pady=10)

        Label(right, text="Location 2", bg='#5e817b').grid(row=18, column=1, columnspan=2, rowspan=2,padx=10,pady=10, ipadx=5,ipady=5)
        self.loc2 = Entry(right, bg='#5e817b')
        self.loc2.grid(row=18, column=3, columnspan=2, rowspan=2,padx=10,pady=10)

        Label(right, text="Deployment 2", bg='#5e817b').grid(row=20, column=1, columnspan=2, rowspan=2,padx=10,pady=10, ipadx=5,ipady=5)
        self.dep2 = Entry(right, bg='#5e817b')
        self.dep2.grid(row=20, column=3, columnspan=2, rowspan=2,padx=10,pady=10)

        Button(right, text="Next step", command=self.update,height = 2, width = 40, bg='#b8ac86').grid(row=24, column=1, columnspan=4,rowspan=2,padx=10,pady=10)
        Button(right, text="Quit", command=self.quit,height = 2, width = 25, bg='#b8ac86').grid(row=0, column=3, columnspan=2,rowspan=1,padx=10,pady=10)

    # fig = Figure(figsize=(4.2, 4), dpi=100)
    # plt = fig.add_subplot(111)
    # exp_vals = [1400, 600, 300, 410, 250]
    # exp_labels = ["a", "b", "c", "d", "e"]
    # plt.plot(exp_vals, exp_labels)
    # plt.axis("equal")
    # pie2 = FigureCanvasTkAgg(fig, frame)
    # pie2.get_tk_widget().grid(row=1, column=0, sticky=W, padx = (10, 5), pady = (10,5))

    # new_york = float("100")
    # paris = float("80")
    # london = float("60")
    # titan = float("40")
    # brooklyn = float("0")
    #
    # fig = Figure(figsize=(4.5, 4), dpi=38)
    # subplot = fig.add_subplot(111)
    # labels2 = 'a', 'b', 'c', 'd', 'e'
    # pieSizes = [float(new_york), float(paris), float(london), float(titan), float(brooklyn)]
    # explode2 = (0, 0, 0, 0, 0)
    # subplot.pie(pieSizes, explode=explode2, labels=labels2, shadow=True, startangle=90)
    # subplot.axis('equal')
    # pie2 = FigureCanvasTkAgg(fig, frame)
    # pie2.get_tk_widget().grid(row=1, column=0, sticky=W, padx=(10, 5), pady=(10, 5))

    # printing information for NW
    # Label(frame,
    #       text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5} \nDeployments: {6}" \
    #       .format(self.env.city.mask_visible_data(nbh_nw, nbh_nw.num_active).name,
    #               self.env.city.mask_visible_data(nbh_nw, nbh_nw.num_sickly).name,
    #               self.env.city.mask_visible_data(nbh_nw, nbh_nw.num_zombie).name,
    #               self.env.city.mask_visible_data(nbh_nw, nbh_nw.num_dead).name,
    #               nbh_nw.orig_alive,
    #               nbh_nw.orig_dead,
    #               nbh_nw.get_current_deps()), justify=LEFT, width = 18, height = 9, bg="#00cccc"
    #       ).grid(row=1, column=0, sticky=W, padx = (10, 5), pady = (10,5))
    #
    # # printing information for N
    # Label(frame,
    #       text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5} \nDeployments: {6}" \
    #       .format(self.env.city.mask_visible_data(nbh_n, nbh_n.num_active).name,
    #               self.env.city.mask_visible_data(nbh_n, nbh_n.num_sickly).name,
    #               self.env.city.mask_visible_data(nbh_n, nbh_n.num_zombie).name,
    #               self.env.city.mask_visible_data(nbh_n, nbh_n.num_dead).name,
    #               nbh_n.orig_alive,
    #               nbh_n.orig_dead,
    #               nbh_n.get_current_deps()), justify=LEFT, width = 18, height = 9, bg="#00ff80"
    #       ).grid(row=1, column=1, sticky=W, padx = 5, pady = (10,5))
    #
    # # printing information for NE
    # Label(frame,
    #       text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5} \nDeployments: {6}" \
    #       .format(self.env.city.mask_visible_data(nbh_ne, nbh_ne.num_active).name,
    #               self.env.city.mask_visible_data(nbh_ne, nbh_ne.num_sickly).name,
    #               self.env.city.mask_visible_data(nbh_ne, nbh_ne.num_zombie).name,
    #               self.env.city.mask_visible_data(nbh_ne, nbh_ne.num_dead).name,
    #               nbh_ne.orig_alive,
    #               nbh_ne.orig_dead,
    #               nbh_ne.get_current_deps()), justify=LEFT, width = 18, height = 9, bg="#00cccc"
    #       ).grid(row=1, column=2, sticky=W, padx = (5,10), pady = (10,5))
    #
    # # printing information for W
    # Label(frame,
    #       text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5} \nDeployments: {6}" \
    #       .format(self.env.city.mask_visible_data(nbh_w, nbh_w.num_active).name,
    #               self.env.city.mask_visible_data(nbh_w, nbh_w.num_sickly).name,
    #               self.env.city.mask_visible_data(nbh_w, nbh_w.num_zombie).name,
    #               self.env.city.mask_visible_data(nbh_w, nbh_w.num_dead).name,
    #               nbh_w.orig_alive,
    #               nbh_w.orig_dead,
    #               nbh_w.get_current_deps()), justify=LEFT, width = 18, height = 9, bg="#00ff80"
    #       ).grid(row=2, column=0, sticky=W, padx = (10, 5), pady = 5)
    #
    # # printing information for C
    # Label(frame,
    #       text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5} \nDeployments: {6}" \
    #       .format(self.env.city.mask_visible_data(nbh_c, nbh_c.num_active).name,
    #               self.env.city.mask_visible_data(nbh_c, nbh_c.num_sickly).name,
    #               self.env.city.mask_visible_data(nbh_c, nbh_c.num_zombie).name,
    #               self.env.city.mask_visible_data(nbh_c, nbh_c.num_dead).name,
    #               nbh_c.orig_alive,
    #               nbh_c.orig_dead,
    #               nbh_c.get_current_deps()), justify=LEFT, width = 18, height = 9, bg="#00cccc"
    #       ).grid(row=2, column=1, sticky=W, padx = 5, pady = 5)
    #
    # # printing information for E
    # Label(frame,
    #       text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5} \nDeployments: {6}" \
    #       .format(self.env.city.mask_visible_data(nbh_e, nbh_e.num_active).name,
    #               self.env.city.mask_visible_data(nbh_e, nbh_e.num_sickly).name,
    #               self.env.city.mask_visible_data(nbh_e, nbh_e.num_zombie).name,
    #               self.env.city.mask_visible_data(nbh_e, nbh_e.num_dead).name,
    #               nbh_e.orig_alive,
    #               nbh_e.orig_dead,
    #               nbh_e.get_current_deps()), justify=LEFT, width = 18, height = 9, bg="#00ff80"
    #       ).grid(row=2, column=2, sticky=W, padx = (5,10), pady = 5)
    #
    # # printing information for SW
    # Label(frame,
    #       text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5} \nDeployments: {6}" \
    #       .format(self.env.city.mask_visible_data(nbh_sw, nbh_sw.num_active).name,
    #               self.env.city.mask_visible_data(nbh_sw, nbh_sw.num_sickly).name,
    #               self.env.city.mask_visible_data(nbh_sw, nbh_sw.num_zombie).name,
    #               self.env.city.mask_visible_data(nbh_sw, nbh_sw.num_dead).name,
    #               nbh_sw.orig_alive,
    #               nbh_sw.orig_dead,
    #               nbh_sw.get_current_deps()), justify=LEFT, width = 18, height = 9, bg="#00cccc"
    #       ).grid(row=3, column=0, sticky=W, padx = (10, 5), pady = (5,10))
    #
    # # printing information for S
    # Label(frame,
    #       text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5} \nDeployments: {6}" \
    #       .format(self.env.city.mask_visible_data(nbh_s, nbh_s.num_active).name,
    #               self.env.city.mask_visible_data(nbh_s, nbh_s.num_sickly).name,
    #               self.env.city.mask_visible_data(nbh_s, nbh_s.num_zombie).name,
    #               self.env.city.mask_visible_data(nbh_s, nbh_s.num_dead).name,
    #               nbh_s.orig_alive,
    #               nbh_s.orig_dead,
    #               nbh_s.get_current_deps()), justify=LEFT, width = 18, height = 9, bg="#00ff80"
    #       ).grid(row=3, column=1, sticky=W, padx = 5, pady = (5,10))
    #
    # # printing information for SE
    # Label(frame,
    #       text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5} \nDeployments: {6}" \
    #       .format(self.env.city.mask_visible_data(nbh_se, nbh_se.num_active).name,
    #               self.env.city.mask_visible_data(nbh_se, nbh_se.num_sickly).name,
    #               self.env.city.mask_visible_data(nbh_se, nbh_se.num_zombie).name,
    #               self.env.city.mask_visible_data(nbh_se, nbh_se.num_dead).name,
    #               nbh_se.orig_alive,
    #               nbh_se.orig_dead,
    #               nbh_se.get_current_deps()), justify=LEFT, width = 18, height = 9, bg="#00cccc"
    #       ).grid(row=3, column=2, sticky=W, padx = (5,10), pady = (5,10))


    def grid3by3(self, frame):

        active = 0
        dead = 0
        sickly = 0
        zombie = 0

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
            active += nbh.num_active
            dead += nbh.num_dead
            sickly += nbh.num_sickly
            zombie += nbh.num_zombie

        self.xlist.append(self.turn)
        self.list_active.append(active)
        self.list_dead.append(dead)
        self.list_sickly.append(sickly)
        self.list_zombie.append(zombie)


        # printing information for NW
        self.oneblock(frame, nbh_nw, 1, 0 , (10,5), (10,5), '#00cccc')

        # printing information for N
        self.oneblock(frame, nbh_n, 1, 1, 5, (10,5), "#00ff80")

        # printing information for NE
        self.oneblock(frame, nbh_ne, 1, 2, (5,10), (10,5), "#00cccc")

        # printing information for W
        self.oneblock(frame, nbh_w, 2, 0, (10,5), 5, "#00ff80")

        # printing information for C
        self.oneblock(frame, nbh_c, 2, 1, 5, 5, "#00cccc")

        # printing information for E
        self.oneblock(frame, nbh_e, 2, 2, (5,10), 5, "#00ff80")

        # printing information for SW
        self.oneblock(frame, nbh_sw, 3, 0, (10,5), (5,10), "#00cccc")

        # printing information for S
        self.oneblock(frame, nbh_s, 3, 1, 5, (5,10), "#00ff80")

        # printing information for SE
        self.oneblock(frame, nbh_se, 3, 2, (5,10), (5,10), "#00cccc")

        self.graph(frame)

    # prints info for one block and button that leads to drawing pie chart
    def oneblock(self, frame, nbh, row_index, col_index, padx_value, pady_value, color):
        Label(frame,
              text="Active: {0} \nSickly: {1} \nZombies: {2} \nDead: {3} \nLiving at Start: {4} \nDead at Start: {5} \nDeployments: {6}" \
              .format(self.env.city.mask_visible_data(nbh, nbh.num_active).name,
                      self.env.city.mask_visible_data(nbh, nbh.num_sickly).name,
                      self.env.city.mask_visible_data(nbh, nbh.num_zombie).name,
                      self.env.city.mask_visible_data(nbh, nbh.num_dead).name,
                      nbh.orig_alive,
                      nbh.orig_dead,
                      nbh.get_current_deps()), justify=LEFT, width=19, height=10, bg= color
              ).grid(row=row_index, column=col_index, sticky=N+E+W+S, padx=padx_value, pady=pady_value)


        Button(frame, command= lambda : self.pieButtons(frame, nbh, row_index, col_index, padx_value, pady_value, color),
               text="i", highlightbackground= color
               ).grid(row=row_index, column=col_index, sticky=E + N, padx=padx_value, pady=pady_value)

    # draws pie chart and button to exit out of pie chart
    def pieButtons(self, frame, nbh, row_index, col_index, padx_value, pady_value, color):
        fig = Figure(figsize=(4, 4), dpi=35)
        fig.patch.set_facecolor(color)
        subplot = fig.add_subplot(111)
        labels2 = 'a', 'b', 'c', 'd'
        pieSizes = [nbh.num_active, nbh.num_sickly, nbh.num_zombie, nbh.num_dead]
        subplot.pie(pieSizes, labels=labels2, shadow=True, startangle=90)
        subplot.axis('equal')
        pie2 = FigureCanvasTkAgg(fig, frame)
        pie2.get_tk_widget().grid(row=row_index, column=col_index, sticky=N+E+S+W, padx=padx_value, pady=pady_value)

        Button(frame, command= lambda : self.oneblock(frame, nbh, row_index, col_index, padx_value, pady_value, color),
               text="X", highlightbackground=color
               ).grid(row=row_index, column=col_index, sticky=E + N, padx=padx_value, pady=pady_value)

    def graph(self, frame):
        fig = Figure(figsize=(4, 4), dpi=35)
        # fig.patch.set_facecolor("#00cccc")
        # subplot = fig.add_subplot(111)
        # y = [5,1,3,2,6,8]
        # subplot.plot([1,2,3,4,5,6],y)
        # subplot.plot([1,2,3,4,5,6],[12,10,9,3,5,6], "ro-")
        # subplot.get_yaxis().set_visible(False)

        subplot = fig.add_subplot(111)
        subplot.plot(self.xlist,self.list_active, "go-")
        subplot.plot(self.xlist,self.list_sickly, "yo-")
        subplot.plot(self.xlist,self.list_dead, "ro-")
        subplot.plot(self.xlist,self.list_zombie, "bo-")
        subplot.get_yaxis().set_visible(False)

        graph = FigureCanvasTkAgg(fig, frame)
        graph.get_tk_widget().grid(row = 1, column = 0, rowspan = 3, columnspan = 3, sticky = N+E+W+S, padx=10, pady=10)

    # function for quitting the gamme
    def quit(self):
        self.winfo_children()[0].quit()

    # update the GUI to next step
    def update(self):
        # self.env.print_player_action_selections()
        location_1 = int(self.loc1.get())
        deployment_1 = int(self.dep1.get())
        location_2 = int(self.loc2.get())
        deployment_2 = int(self.dep2.get())
        actions = self.env.encode_raw_action(add_1 = 0,
                                             location_1=LOCATIONS(location_1),
                                             deployment_1=DEPLOYMENTS(deployment_1),
                                             add_2 = 0,
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