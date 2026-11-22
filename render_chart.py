from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from optimizer import ranked_rosters

fig, ax = plt.subplots(figsize=(8.4, 4.7), layout="constrained")
fig.patch.set_facecolor("#f6f6ef")
ax.set_facecolor("#fbfbf7")
for budget in range(9, 18):
    candidates = ranked_rosters(budget=budget)
    if candidates:
        ax.scatter(budget, candidates[0].contribution, color="#226b5b", s=65, zorder=3)
baseline = ranked_rosters()[0]
ax.annotate(f"Budget 14: score {baseline.contribution}", (14, baseline.contribution),
            xytext=(11, baseline.contribution + 5), arrowprops={"arrowstyle": "->", "color": "#304741"})
ax.set(title="Roster choice under a fixed risk ceiling", xlabel="Budget (synthetic units)",
       ylabel="Best feasible contribution")
ax.set_ylim(35, 66)
ax.grid(axis="y", alpha=0.25)
fig.text(0.97, 0.01, "Fictional candidates · ceiling = 6", ha="right", color="#4b605a")
target = Path("docs") / "roster-tradeoff.png"
fig.savefig(target, dpi=130)
print(target)
