# Project Cost & Duration Simulation using Monte Carlo

This project simulates the **total cost and time** required to complete a multi-phase project (e.g., construction) using **Monte Carlo methods**. Each phase has uncertain costs and durations modeled by normal distributions.

---

# Objective

Estimate the probability distribution of:
- **Total project cost**
- **Total project duration**

Considering 3 key phases:
1. Foundation
2. Structure
3. Finishing

Each with its own average cost/duration and associated uncertainty.

---

# Problem Overview

For each phase:
- Cost ∼ Normal(mean, std)
- Duration ∼ Normal(mean, std)

Only **non-negative values** are considered for realistic results.

---

# Base Parameters

```python
phases = {
    'foundation': {'base_cost': 100_000, 'cost_std': 10_000, 'base_duration': 15, 'duration_std': 3},
    'structure': {'base_cost': 200_000, 'cost_std': 25_000, 'base_duration': 30, 'duration_std': 5},
    'finishing': {'base_cost': 150_000, 'cost_std': 20_000, 'base_duration': 20, 'duration_std': 4}
}
n_simulations = 10_000
