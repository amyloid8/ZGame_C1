import uuid
import gym
import gym_zgame
from gym_zgame.envs.enums.PLAY_TYPE import PLAY_TYPE
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common import make_vec_env
from stable_baselines import A2C


class ZGame:
    """
    RL Algorithm: A2C
    Original paper: https://arxiv.org/abs/1602.01783
    OpenAI blog post: https://openai.com/blog/baselines-acktr-a2c/
    https://stable-baselines.readthedocs.io/en/master/modules/a2c.html
    """
    def __init__(self, model_filename='rl-agent', num_steps=1000, num_envs=4):
        self.ENV_NAME = 'ZGame-v0'
        self.MODEL_FILENAME = model_filename
        self.GAME_ID = uuid.uuid4()
        self.env = None
        self.current_actions = []
        self.turn = 0
        self.max_turns = 14
        # Learning Parameters
        self._verbosity = 1
        self.num_steps = num_steps
        self.num_envs = num_envs
        # Always do these actions upon start
        self._setup()

    def _setup(self):
        # Game parameters
        self.env = make_vec_env(self.ENV_NAME, n_envs=self.num_envs)
        self.env.play_type = PLAY_TYPE.MACHINE
        self.env.render_mode = 'machine'
        self.env.MAX_TURNS = self.max_turns
        self.env.reset()
        # Report success
        print('Created new environment {0} with GameID: {1}'.format(self.ENV_NAME, self.GAME_ID))

    def done(self):
        print("Episode finished after {} turns".format(self.turn))
        self._cleanup()

    def _cleanup(self):
        self.env.close()

    def run(self):
        print('Starting new game for training!')
        model = A2C(MlpPolicy, self.env, verbose=self._verbosity)
        model.learn(total_timesteps=self.num_steps)
        model.save(self.MODEL_FILENAME)
