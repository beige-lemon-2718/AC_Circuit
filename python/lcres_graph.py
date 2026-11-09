import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams.update({
#     "text.usetex": True,
#     "pgf.texsystem": "lualatex",
# })

x = np.linspace(0, 5000000, 1000)
y = np.sqrt(1/((x*20.0) - (1/(x*20.0))))

plt.figure(figsize=(8, 6))

plt.plot(x, y)

# plt.title('$\sqrt{\frac{1}{1+\omega^2}}$のグラフ')
# plt.xlabel('ω')
# plt.ylabel('')

plt.grid(True)

plt.savefig('lc_graph.pdf')

plt.show()