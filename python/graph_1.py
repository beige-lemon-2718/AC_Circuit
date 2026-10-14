import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

magnitude = 1.0
phase_deg = 40
phase = np.deg2rad(phase_deg)

x = magnitude * np.cos(phase)
y = magnitude * np.sin(phase)

fig, ax = plt.subplots(figsize=(6, 6))

# フェーザ
ax.annotate(
    "",
    xy=(x, y),
    xytext=(0, 0),
    arrowprops=dict(arrowstyle="->", linewidth=2, color="tab:blue")
)

# 実部・虚部を示す補助線
ax.plot([x, x], [0, y], "--", color="gray")
ax.plot([0, x], [y, y], "--", color="gray")

# 位相角
arc = Arc(
    (0, 0), 0.5, 0.5,
    angle=0,
    theta1=0,
    theta2=phase_deg,
    color="tab:red"
)
ax.add_patch(arc)
ax.text(0.3, 0.1, rf"$\phi={phase_deg}^\circ$", color="tab:red")

ax.text(x / 2, y / 2 + 0.08, r"$\dot{V}$", color="tab:blue")
ax.text(x, -0.08, r"$V\cos\phi$", ha="center")
ax.text(-0.05, y, r"$V\sin\phi$", ha="right", va="center")

ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)
ax.set_aspect("equal")
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.set_xlabel("実軸")
ax.set_ylabel("虚軸")
ax.grid(alpha=0.25)

plt.tight_layout()
plt.show()