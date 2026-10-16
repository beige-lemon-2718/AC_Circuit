import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams.update({
#     "text.usetex": True,
#     "pgf.texsystem": "lualatex",
# })

x = np.linspace(0, 5000000, 1000)
y = np.sqrt(x**2*1.0e+3**2*10*1.0e-9**2/((1 + x**2*10*1.0e+3**2*10*1.0e-9**2)))

plt.figure(figsize=(8, 6))

plt.plot(x, y)

# plt.title('$\sqrt{\frac{1}{1+\omega^2}}$のグラフ')
# plt.xlabel('ω')
# plt.ylabel('')

plt.grid(True)

plt.savefig('hpf_graph.pdf')

plt.show()