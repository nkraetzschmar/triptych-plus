import matplotlib.pyplot as plt

s = 32

m = [i+1 for i in range(20)]
N = [2**m for m in m]

triptych = [s * (3 * m + 7) for m in m]
triptych_plus = [s * (2 * m + 12) for m in m]
short_ring_signatures = [s * (3 * m + 16) for m in m]
triptych_plus_accountable = [s * (2 * m + 14) for m in m]

lsag_N = [i+2 for i in range(63)]
lsag = [s * (N+1) for N in lsag_N]

plt.figure(figsize=(6,4))
plt.plot(N, triptych, N, triptych_plus, lsag_N, lsag)
plt.ylabel("signature size (bytes)")
plt.xlabel("number of ring members")
plt.legend(["Triptych", "Triptych+", "LSAG"])
plt.grid()
plt.xscale("log", basex=2)
plt.savefig("build/linkable.pyplot.pdf", bbox_inches="tight", transparent=True)

plt.figure(figsize=(6,4))
plt.plot(N, short_ring_signatures, N, triptych_plus_accountable)
plt.ylabel("signature size (bytes)")
plt.xlabel("number of ring members")
plt.legend(["Short Accountable Ring Signatures", "Triptych+ (accountable signatures)"])
plt.grid()
plt.xscale("log", basex=2)
plt.savefig("build/accountable.pyplot.pdf", bbox_inches="tight", transparent=True)
