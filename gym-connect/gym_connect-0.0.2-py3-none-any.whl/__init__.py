from gym.envs.registration import register

register(
    id='connect-v0',
    entry_point='gym_foo.envs:ConnectEnv',
)
