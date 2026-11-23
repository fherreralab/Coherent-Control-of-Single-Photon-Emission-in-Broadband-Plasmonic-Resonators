import numpy as np
import matplotlib.pyplot as plt

t_ps = np.loadtxt("Fig5b_time.txt")
omega = np.loadtxt("Fig5b_omega.txt")
P_emit = np.loadtxt("Fig5b_P_emit.txt.gz")

vmax = np.max(np.abs(P_emit))

fig, ax = plt.subplots(figsize=(6.5, 4.5), constrained_layout=True)

pcm = ax.pcolormesh(
    t_ps,
    omega,
    P_emit,
    cmap="seismic",
    vmin=-vmax,
    vmax=vmax,
    shading="auto",
)

cbar = fig.colorbar(pcm, ax=ax, pad=0.02)
cbar.set_label(r"$P_1(\omega, t) - P_1^{\mathrm{bg}}(\omega, t)$ (fs)")

ax.set_xlabel(r"Time $t$ (ps)")
ax.set_ylabel(r"Frequency $\omega$ (eV)")
ax.set_xlim(t_ps[0], t_ps[-1])
ax.set_ylim(omega[0], omega[-1])

plt.show()