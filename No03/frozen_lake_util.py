import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import gym
from gym.envs.registration import register
register(id="FrozenLakeEasy-v0", entry_point="gym.envs.toy_text:FrozenLakeEnv",
         kwargs={"is_slippery": False})

# ‰¿’l‚Ì•\Ž¦
def show_q_value(Q):
    env = gym.make("FrozenLake-v0")
    nrow = env.unwrapped.nrow
    ncol = env.unwrapped.ncol
    state_size = 3
    q_nrow = nrow * state_size
    q_ncol = ncol * state_size
    reward_map = np.zeros((q_nrow, q_ncol))

    for r in range(nrow):
        for c in range(ncol):
            s = r * nrow + c
            state_exist = False
            if isinstance(Q, dict) and s in Q:
                state_exist = True
            elif isinstance(Q, (np.ndarray, np.generic)) and s < Q.shape[0]:
                state_exist = True

            if state_exist:
                # At the display map, the vertical index is reversed.
                _r = 1 + (nrow - 1 - r) * state_size
                _c = 1 + c * state_size
                reward_map[_r][_c - 1] = Q[s][0]  # LEFT 
                reward_map[_r - 1][_c] = Q[s][1]  # DOWN 
                reward_map[_r][_c + 1] = Q[s][2]  # RIGHT 
                reward_map[_r + 1][_c] = Q[s][3]  # UP 
                reward_map[_r][_c] = np.mean(Q[s])  # Center

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.imshow(reward_map, cmap=cm.RdYlBu, interpolation="bilinear",
               vmax=abs(reward_map).max(), vmin=-abs(reward_map).max())
    ax.set_xlim(-0.5, q_ncol - 0.5)
    ax.set_ylim(-0.5, q_nrow - 0.5)
    ax.set_xticks(np.arange(-0.5, q_ncol, state_size))
    ax.set_yticks(np.arange(-0.5, q_nrow, state_size))
    ax.set_xticklabels(range(ncol + 1))
    ax.set_yticklabels(range(nrow + 1))
    ax.grid(which="both")
    font_dict=dict(size=20)
    ax.text(0.6, 0.6, "H",fontdict=font_dict)
    ax.text(3.6, 6.6, "H",fontdict=font_dict)
    ax.text(9.6, 6.6, "H",fontdict=font_dict)
    ax.text(9.6, 3.6, "H",fontdict=font_dict)
    ax.text(0.6, 9.6, "S",fontdict=font_dict)
    ax.text(9.6, 0.6, "G",fontdict=font_dict)
    plt.show()
