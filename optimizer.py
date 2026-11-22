from dataclasses import dataclass
from itertools import combinations

@dataclass(frozen=True)
class Player:
    name: str
    role: str
    cost: int
    contribution: int
    risk: int

PLAYERS = (
    Player("Harbor", "guard", 5, 19, 2),
    Player("Linden", "guard", 4, 13, 1),
    Player("Cobalt", "wing", 6, 24, 4),
    Player("Aster", "wing", 4, 15, 1),
    Player("Briar", "post", 5, 20, 2),
    Player("Dune", "post", 3, 11, 1),
    Player("Slate", "wing", 3, 10, 2),
)
REQUIRED_ROLES = frozenset({"guard", "wing", "post"})

@dataclass(frozen=True)
class Roster:
    players: tuple[Player, ...]
    cost: int
    contribution: int
    risk: int

def ranked_rosters(players=PLAYERS, *, budget=14, risk_ceiling=6):
    """Return feasible three-player portfolios sorted by contribution."""
    feasible = []
    for selected in combinations(players, len(REQUIRED_ROLES)):
        if {p.role for p in selected} != REQUIRED_ROLES:
            continue
        cost = sum(p.cost for p in selected)
        risk = sum(p.risk for p in selected)
        if cost <= budget and risk <= risk_ceiling:
            feasible.append(Roster(selected, cost, sum(p.contribution for p in selected), risk))
    return sorted(feasible, key=lambda r: (-r.contribution, r.cost, r.risk, tuple(p.name for p in r.players)))

if __name__ == "__main__":
    result = ranked_rosters()
    if result:
        best = result[0]
        print("Synthetic roster:", ", ".join(p.name for p in best.players))
        print(f"Cost {best.cost}; contribution {best.contribution}; risk {best.risk}")
    else:
        print("No feasible roster. Review the budget or risk ceiling.")
