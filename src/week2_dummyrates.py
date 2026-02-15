import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,10,1000)

omegas = np.array([np.sin(2*t), np.cos(2*t), np.sin(t)])


plt.plot(t,omegas[0], t, omegas[1], t, omegas[2])
plt.savefig("plots/dummyrates.png")
plt.show()