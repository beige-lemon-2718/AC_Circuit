import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib_fontja

# plt.rcParams.update({
#     "text.usetex": True,
#     "pgf.texsystem": "lualatex",
# })

x = np.linspace(0, 4.0e6, 1000)
y = 1.0/((x*2.0e-5) - (1.0/(x*1.25e-08)))

plt.figure(figsize=(8, 6))

plt.plot(x, y)

# plt.title('$\sqrt{\frac{1}{1+\omega^2}}$のグラフ')
# plt.xlabel('ω')
# plt.ylabel('')

plt.grid(True)

plt.savefig('lc_graph.pdf')

plt.show()