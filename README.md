# Data for Coherent Control of Single-Photon Emission in Broadband Plasmonic Resonators

Data used in "Coherent Control of Single-Photon Emission in Broadband Plasmonic Resonators", by Athul S. Rema, Adrián E. Rubio López, and Felipe Herrera.

Preprint: https://arxiv.org/abs/XXXX.XXXXX

All files are plain text, whitespace-separated, with a header row naming each column. One file is gzipped, and numpy.loadtxt opens it directly without unpacking.

Throughout, the emitter is a quantum dot of dipole moment 24 D placed 2 nm from a 20 nm-radius silver nanosphere, with transition frequency ω_e = 2.97 eV at the maximum of the spectral density K(ω). The kernel bandwidth is Γ_K = 63 meV, and all traces use the same per-tooth amplitude |D_0| = 10⁻⁵ a.u.

## Fig1 — controlling emission temporal profiles

Excited-state population P_e(t) = |C_e0(t)|² under reservoir driving, for teeth of width σ = 1 meV.

Fig1a_Pop.txt is the single-tooth case (N = 1), with columns t_ps and Pe_N1. Fig1b_Pop.txt is the seven-tooth comb, columns t_ps and Pe_N7; its spacing is Δω = 10.5 meV, so the bursts recur every T_rec = 0.394 ps.

## Fig2 — single-photon frequency-time evolution

All four panels use the optimal comb for σ = 1 meV, namely N = 23 teeth spaced by Δω = 2.864 meV, which puts the first burst at T_rec = 1.444 ps. Here P_1(ω,t) = |C_g1(ω,t)|² is the single-photon spectrum and P_1^bg = |D(ω)|²t² the drive-only background, both in fs.

Fig2a.txt is the excited-state population together with its coherent-sum bound: columns t_ps, P_e(t), Env^2(t).

Fig2b.txt and Fig2c.txt are cuts of the single-photon spectrum, taken on a comb tooth (δ = 0) and midway between two teeth (δ = Δω/2). Each has three columns: time, the drive-only background, and the full spectrum.

Fig2d_P_emit.txt.gz holds the 2D map of the emitter-induced change P_1 − P_1^bg, with rows indexed by frequency and columns by time. The two axes are in Fig2d_omega.txt (eV) and Fig2d_time.txt (ps), and the map covers the plotted window 2.925–3.015 eV.

Fig2d.py redraws panel (d) from those three files.

## Fig3 — optimal single-photon pulses

Population at the first burst, P_1 = P_e(T_rec), against the number of comb teeth N. The teeth always span Γ_K = 63 meV, so the spacing is Δω = Γ_K/(N − 1) and the first burst arrives at T_rec = 2πħ/Δω. The optima are N = 23, 44 and 217 for σ = 1, 0.5 and 0.1 meV.

Fig3.txt has five columns: N, then P_1 for σ = 0.1, 0.5 and 1 meV, and finally the coherent-sum bound max_t P_env(t), which grows as N².
