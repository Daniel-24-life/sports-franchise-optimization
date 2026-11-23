<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/cover-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="docs/cover-light.svg" />
  <img src="docs/cover-light.svg" alt="Sports Franchise Optimization" width="1280" />
</picture>

# Sports Franchise Optimization

Find the best feasible roster for a given budget, role mix, and risk limit.

[▶ Demo](#demo) · [中文](README.zh.md) · [![CI](https://github.com/Daniel-24-life/sports-franchise-optimization/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Daniel-24-life/sports-franchise-optimization/actions/workflows/ci.yml) · [MIT](LICENSE) · Python 3.11+

## Demo

<img src="docs/roster-tradeoff.png" alt="Sports Franchise Optimization" width="800" />

## Problem

The highest-ranked player can be a poor fit when the roster still needs a role covered. An exact small-scale search makes the constraint trade-offs visible.

## What I built

- Enumerate candidate rosters without discarding feasible combinations.
- Apply budget, role and risk checks before ranking.
- Plot the best feasible score across budgets.

## How it works

```mermaid
flowchart LR
    A["Candidate roster"] --> B["Constraints"] --> C["Ranked choice"]
```

## Run in 60 seconds

```sh
python optimizer.py
python -m pip install matplotlib
python render_chart.py
```

## Tests

**3 tests passed.** [Verified GitHub Actions run](https://github.com/Daniel-24-life/sports-franchise-optimization/actions/runs/45105908472).

```sh
python -m unittest -v
```

## Repository layout

| Path | Contents |
| --- | --- |
| [`optimizer.py`](optimizer.py) | Candidate fixture and exact solver |
| [`test_optimizer.py`](test_optimizer.py) | Feasibility and ranking tests |
| [`render_chart.py`](render_chart.py) | Budget trade-off chart |

<sub>The example uses synthetic roster inputs. Enumeration is exact for the included candidate set and its scoring assumptions.</sub>
