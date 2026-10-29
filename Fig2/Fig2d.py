# Fig. 2(d): emitter-induced change in the single-photon spectrum,
# P_1 - P_1^bg, for N = 23 teeth of width sigma = 1 meV.
# Set text.usetex to False if LaTeX is not installed.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter

HBAR = 0.6582119569      # hbar (meV ps)
GAMMA_K = 63.0           # kernel bandwidth, FWHM (meV)
N = 23                   # number of comb teeth
OMEGA_E = 2.97           # emitter frequency (eV)
T_MAX = 5.0              # plotted time range (ps)

DELTA_W = GAMMA_K / (N - 1)        # comb spacing (meV)
T_REC = 2 * np.pi * HBAR / DELTA_W  # recurrence time (ps)

plt.rcParams.update({
    "text.usetex": True, "font.family": "serif",
    "axes.labelsize": 16, "xtick.labelsize": 15, "ytick.labelsize": 15,
    "xtick.direction": "in", "ytick.direction": "in",
    "xtick.top": True, "ytick.right": True, "axes.linewidth": 1.2,
})

t = np.loadtxt("Fig2d_time.txt")
w = np.loadtxt("Fig2d_omega.txt")
P = np.loadtxt("Fig2d_P_emit.txt.gz")        # rows: omega, cols: t

fig, ax = plt.subplots(figsize=(5.8, 4.5))

vmax = np.percentile(np.abs(P), 98.0)
im = ax.pcolormesh(*np.meshgrid(t, w), P, cmap="seismic", shading="auto",
                   vmin=-vmax, vmax=vmax, rasterized=True)

for m in range(1, int(T_MAX // T_REC) + 1):
    ax.axvline(m * T_REC, color="black", ls=":", lw=1.5, alpha=0.8, zorder=10)
ax.axhline(OMEGA_E, color="black", ls="--", lw=1.0, alpha=0.7, zorder=10)

ax.set_xlim(0, T_MAX)
ax.set_ylim(2.925, 3.015)
ax.set_xlabel(r"$t$ $({\rm ps})$")
ax.set_ylabel(r"$\omega$ $({\rm eV})$")
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which="minor", direction="in", top=True, right=True, length=3, width=1.0)

cbar = fig.colorbar(im, ax=ax, pad=0.03, shrink=0.9, aspect=15)
cbar.ax.yaxis.set_major_formatter(FormatStrFormatter("%.4f"))
cbar.set_label(r"$P_1(\omega,t)-P_1^{\rm bg}(\omega,t)$ (fs)", rotation=270, labelpad=25)
cbar.ax.tick_params(labelsize=12)
cbar.outline.set_linewidth(0.8)

fig.savefig("Fig2d.png", transparent=True, dpi=600, bbox_inches="tight")
plt.show()
