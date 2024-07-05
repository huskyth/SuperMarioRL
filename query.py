from matplotlib import pyplot as plt
from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
import time
import cv2

# TODO://gym==0.23.0
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

# state0 = env.reset()
#
#
# state, reward, done, info = env.step(5)
# plt.imshow(state)
# plt.show()
# assert False

done = True
step = 0
temp = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
for step in range(5000):
    if done:
        step = 0
        state = env.reset()
    state, reward, done, info = env.step(temp[step])
    time.sleep(0.01)
    state = cv2.cvtColor(state, cv2.COLOR_BGR2RGB)
    cv2.imwrite(f"state_{step}_reward_{reward}.png", state)
    print(f"step {step}")
    step += 1
    env.render()
    if step == 16:
        break

time.sleep(10)

env.close()
