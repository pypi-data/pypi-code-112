#################################################################################
#   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.          #
#                                                                               #
#   Licensed under the Apache License, Version 2.0 (the "License").             #
#   You may not use this file except in compliance with the License.            #
#   You may obtain a copy of the License at                                     #
#                                                                               #
#       http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                               #
#   Unless required by applicable law or agreed to in writing, software         #
#   distributed under the License is distributed on an "AS IS" BASIS,           #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    #
#   See the License for the specific language governing permissions and         #
#   limitations under the License.                                              #
#################################################################################
"""A class for Gym Environment Adapter to bridge OpenAI Gym environment to UDE."""
from typing import Dict
from threading import RLock

from gym import Space

from ude import (
    UDEEnvironmentAdapterInterface,
    MultiAgentDict, UDEStepResult,
    AbstractSideChannel, SingleSideChannel, AgentID
)
import gym


class GymEnvironmentAdapter(UDEEnvironmentAdapterInterface):
    """
    GymEnvironmentAdapter class to interface gym environment to UDE Environment.
    """
    def __init__(self, gym_env: gym.Env,
                 agent_name: str = "agent0",
                 render: bool = False):
        """
        Initialize GymEnvironmentAdapter

        Args:
            gym_env (gym.Env): OpenAI Gym environment instance
            agent_name (str): Name of agent to use.
            render (bool): the flag to render OpenAI gym environment or not.
        """
        super().__init__()
        self._env = gym_env
        self._env.reset()
        self._new_env = None

        self._render = render

        self._side_channel = SingleSideChannel()
        self._agent_name = agent_name or "agent0"
        self._lock = RLock()

    @property
    def env(self) -> gym.Env:
        """
        Returns the current OpenAI gym environment.

        Returns:
            gym.Env: the current OpenAI gym environment.
        """
        with self._lock:
            return self._env

    @env.setter
    def env(self, value: gym.Env) -> None:
        """
        Sets new OpenAI gym environment.

        Args:
            value (gym.Env): new OpenAI gym environment to use.
        """
        self._new_env = value

    def step(self, action_dict: MultiAgentDict) -> UDEStepResult:
        """
        Performs one multi-agent step with given action, and retrieve
        observation(s), reward(s), done(s), action(s) taken,
        and info (if there is any).

        Args:
            action_dict (MultiAgentDict): the action for the agent with agent_name as key.

        Returns:
            UDEStepResult: observation, reward, done, last_action, info
        """
        with self._lock:
            action = action_dict[list(action_dict.keys())[0]]
            obs, reward, done, info = self._env.step(action)
            if self._render:
                self._env.render()
            return ({self._agent_name: obs}, {self._agent_name: reward}, {self._agent_name: done},
                    {self._agent_name: action}, info)

    def reset(self) -> MultiAgentDict:
        """
        Reset the environment and start new episode.
        Also, returns the first observation for new episode started.

        Returns:
            MultiAgentDict: first observation in new episode.
        """
        with self._lock:
            # If there is new environment to replace, replace it during reset.
            if self._new_env:
                if self._env:
                    self._env.close()
                self._env = self._new_env
                self._new_env = None
            obs = self._env.reset()
            if self._render:
                self._env.render()
            return {self._agent_name: obs}

    def close(self) -> None:
        """
        Close the environment, and environment will be no longer available to be used.
        """
        with self._lock:
            self._env.close()

    @property
    def observation_space(self) -> Dict[AgentID, Space]:
        """
        Returns the observation spaces of agents in env.

        Returns:
            Dict[AgentID, Space]: the observation spaces of agents in env.
        """
        with self._lock:
            observation_space = self._env.observation_space
            return {self._agent_name: observation_space}

    @property
    def action_space(self) -> Dict[AgentID, Space]:
        """
        Returns the action spaces of agents in env.

        Returns:
            Dict[AgentID, Space]: the action spaces of agents in env.
        """
        with self._lock:
            action_space = self._env.action_space
            return {self._agent_name: action_space}

    @property
    def side_channel(self) -> AbstractSideChannel:
        """
        Returns side channel to send and receive data from UDE Server

        Returns:
            AbstractSideChannel: the instance of side channel.
        """
        return self._side_channel
