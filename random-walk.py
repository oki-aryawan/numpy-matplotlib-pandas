import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

all_walk = []
for i in range(10):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        random_walk.append(step)
    all_walk.append(random_walk)

print(all_walk)
np_all_walks = np.array(all_walk)
np_all_walks_t = np.transpose(np_all_walks)
plt.plot(np_all_walks_t)
plt.xlabel('Walk')
plt.ylabel('Throw')
plt.show()
