"""Adapted from the Pistonball environment in PettingZoo."""

from typing_extensions import override

import numpy as np
from gymnasium.spaces import Box
from pettingzoo.butterfly.pistonball.pistonball import FPS
from pettingzoo.butterfly.pistonball.pistonball import raw_env as PistonballEnv
from pettingzoo.utils import wrappers

from momaland.utils.conversions import mo_aec_to_parallel
from momaland.utils.env import MOAECEnv


def env(**kwargs):
    """Returns the wrapped environment in `AEC` format.

    Args:
        **kwargs: keyword args to forward to the raw_env function.

    Returns:
        A fully wrapped AEC env.
    """
    env = raw_env(**kwargs)
    env = wrappers.ClipOutOfBoundsWrapper(env)
    return env


def parallel_env(**kwargs):
    """Returns the wrapped env in `parallel` format.

    Args:
        **kwargs: keyword args to forward to the raw_env function.

    Returns:
        A fully wrapped parallel env.
    """
    env = raw_env(**kwargs)
    env = mo_aec_to_parallel(env)
    return env


def raw_env(**kwargs):
    """Returns the environment in `AEC` format.

    Args:
        **kwargs: keyword args to forward to create the `MOPistonball` environment.

    Returns:
        A raw env.
    """
    env = MOPistonball(**kwargs)
    return env


class MOPistonball(MOAECEnv, PistonballEnv):
    """An `AEC` environment where pistons need to cooperate to move a ball towards the edge of the window.

    ## Observation Space
    The observation space is unchanged from the original Pistonball. Each piston agent’s observation is an RGB image of the two pistons (or the wall) next to the agent and the space above them.

    ## Action Space
    The action space is unchanged from the original Pistonball. The action space is a 3D vector when set to discrete: 0 to move down, 1 to stay still, and 2 to move up. When set to continuous mode, an action takes a value between -1 and 1 proportional to the amount that the pistons are raised or lowered by.

    ## Reward Space
    The reward disentangles the original components of the scalar reward in Pistonball. As such, the reward space is a 3D vector containing rewards for:
    - Maximising the global reward. The global reward specifies how close the ball is to the edge of the window.
    - Maximising the local reward. The local reward is given when an agent moves the ball closer to the edge of the window.
    - Minimizing the time penalty.

    ## Starting State
    The ball is by default dropped at the right edge of the window. This can be changed by setting `random_drop` to `True`.

    ## Episode Termination
    The episode is terminated when the ball reaches the limit of the window.

    ## Episode Truncation
    The episode is truncated when `max_cycles` is reached. This is set to 125 by default.

    ## Arguments
    - `n_pistons (int, optional)`: The number of pistons in the environment. Defaults to 20.
    - `time_penalty (int, optional)`: The time penalty for not finishing the episode. Defaults to -0.1.
    - `continuous (int, optional)`: Whether to use continuous actions or not. Defaults to True.
    - `random_drop (int, optional)`: Whether to drop the ball at a random place. Defaults to True.
    - `ball_mass (int, optional)`: The mass of the ball. Defaults to 0.75.
    - `ball_friction (int, optional)`: The friction of the ball. Defaults to 0.3.
    - `ball_elasticity (int, optional)`: The elasticity of the ball. Defaults to 1.5.
    - `max_cycles (int, optional)`: The maximum number of cycles in the environment before termination. Defaults to 125.
    - `render_mode (int, optional)`: The render mode. Can be human, rgb_array or None. Defaults to None.

    ## Credits
    The code was adapted from the [original Pistonball](https://github.com/Farama-Foundation/PettingZoo/blob/master/pettingzoo/butterfly/pistonball/pistonball.py).
    """

    metadata = {
        "render_modes": ["human", "rgb_array"],
        "name": "mopistonball_v0",
        "is_parallelizable": True,
        "render_fps": FPS,
    }

    @override
    def __init__(
        self,
        n_pistons=20,
        time_penalty=-0.1,
        continuous=True,
        random_drop=True,
        random_rotate=True,
        ball_mass=0.75,
        ball_friction=0.3,
        ball_elasticity=1.5,
        max_cycles=125,
        render_mode=None,
    ):
        super().__init__(
            n_pistons=n_pistons,
            time_penalty=time_penalty,
            continuous=continuous,
            random_drop=random_drop,
            random_rotate=random_rotate,
            ball_mass=ball_mass,
            ball_friction=ball_friction,
            ball_elasticity=ball_elasticity,
            max_cycles=max_cycles,
            render_mode=render_mode,
        )
        self.reward_dim = 3  # [global, local, time]
        # A piston only gets a local reward if it is below the ball and the ball covers at most "max_covers" pistons. As
        # such, the local reward can only be "max_covers" times the width of the piston scaled by 0.5.
        max_covers = 1 + np.ceil(2 * self.ball_radius / self.piston_width)
        max_local_reward = max_covers * self.piston_width * 0.5
        # The global reward is computed by dividing its change in position by the total distance it needs to travel (at
        # least 1) and multiplying this by 100. The best case scenario is to travel the entire distance in one go
        # cancelling all terms and resulting in a reward of 100. The worst case is starting with a distance of 1 and
        # traveling to the wrong side of the screen. Note that a better lower bound can be obtained once the starting
        # position of the ball is known.
        max_global_reward = 100
        min_global_reward = (100 / 1) * (1 - self.screen_width)
        self.reward_spaces = {
            f"piston_{i}": Box(
                low=np.array([min_global_reward, -max_local_reward, self.time_penalty]),
                high=np.array([max_global_reward, max_local_reward, 0]),
                shape=(self.reward_dim,),
                dtype=np.float32,
            )
            for i in range(self.num_agents)
        }

    def reward_space(self, agent):
        """Return the reward space for an agent."""
        return self.reward_spaces[agent]

    @override
    def step(self, action):
        if self.terminations[self.agent_selection] or self.truncations[self.agent_selection]:
            self._was_dead_step(action)
            return

        action = np.asarray(action)
        agent = self.agent_selection
        if self.continuous:
            self.move_piston(self.pistonList[self.agent_name_mapping[agent]], action)
        else:
            self.move_piston(self.pistonList[self.agent_name_mapping[agent]], action - 1)

        self.space.step(self.dt)
        if self._agent_selector.is_last():
            ball_min_x = int(self.ball.position[0] - self.ball_radius)
            ball_next_x = self.ball.position[0] - self.ball_radius + self.ball.velocity[0] * self.dt
            if ball_next_x <= self.wall_width + 1:
                self.terminate = True
            # ensures that the ball can't pass through the wall
            ball_min_x = max(self.wall_width, ball_min_x)
            self.draw()
            local_reward = self.get_local_reward(self.lastX, ball_min_x)
            # Opposite order due to moving right to left
            global_reward = (100 / self.distance) * (self.lastX - ball_min_x)
            if not self.terminate:
                time_penalty = self.time_penalty
            else:
                time_penalty = 0
            agent_rewards = np.zeros((self.n_pistons, self.reward_dim), dtype=np.float32)
            agent_rewards[:, 0] = global_reward
            agent_rewards[self.get_nearby_pistons(), 1] = local_reward
            agent_rewards[:, 2] = time_penalty
            self.rewards = dict(zip(self.agents, agent_rewards))
            self.lastX = ball_min_x
            self.frames += 1
        else:
            self._clear_rewards()

        self.truncate = self.frames >= self.max_cycles
        # Clear the list of recent pistons for the next reward cycle
        if self.frames % self.recentFrameLimit == 0:
            self.recentPistons = set()
        if self._agent_selector.is_last():
            self.terminations = dict(zip(self.agents, [self.terminate for _ in self.agents]))
            self.truncations = dict(zip(self.agents, [self.truncate for _ in self.agents]))

        self.agent_selection = self._agent_selector.next()
        self._cumulative_rewards[agent] = np.zeros(self.reward_dim)
        self._accumulate_rewards()

        if self.render_mode == "human":
            self.render()

    @override
    def reset(self, seed=None, options=None):
        """Reset the environment."""
        super().reset(seed, options)
        zero_reward = np.zeros(self.reward_dim, dtype=np.float32)
        self._cumulative_rewards = dict(zip(self.agents, [zero_reward.copy() for _ in self.agents]))
        self.rewards = dict(zip(self.agents, [zero_reward.copy() for _ in self.agents]))
