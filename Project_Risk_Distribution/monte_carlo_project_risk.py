import numpy as np
import matplotlib.pyplot as plt

# -------- INITIAL CONFIGURATION --------
np.random.seed(42)
n_simulations = 10_000

# Project phases with base cost and duration estimates (in days)
phases = {
    'foundation': {'base_cost': 100_000, 'cost_std': 10_000, 'base_duration': 15, 'duration_std': 3},
    'structure': {'base_cost': 200_000, 'cost_std': 25_000, 'base_duration': 30, 'duration_std': 5},
    'finishing': {'base_cost': 150_000, 'cost_std': 20_000, 'base_duration': 20, 'duration_std': 4}
}

# -------- SINGLE PROJECT SIMULATION FUNCTION --------
def simulate_project():
    total_cost = 0
    total_duration = 0

    for phase in phases.values():
        cost = np.random.normal(phase['base_cost'], phase['cost_std'])
        duration = np.random.normal(phase['base_duration'], phase['duration_std'])

        total_cost += max(0, cost)
        total_duration += max(0, duration)

    return total_cost, total_duration

# -------- RUNNING THE SIMULATION --------
costs, durations = zip(*[simulate_project() for _ in range(n_simulations)])

# -------- VISUALIZATION --------
plt.figure(figsize=(12, 5))

# Cost histogram
plt.subplot(1, 2, 1)
plt.hist(costs, bins=50, color='skyblue', edgecolor='black')
plt.title("Total Project Cost Distribution")
plt.xlabel("Cost (R$)")
plt.ylabel("Frequency")
plt.axvline(np.mean(costs), color='red', linestyle='--', label=f"Mean: R${np.mean(costs):,.0f}")
plt.legend()

# Duration histogram
plt.subplot(1, 2, 2)
plt.hist(durations, bins=50, color='lightgreen', edgecolor='black')
plt.title("Total Project Duration Distribution")
plt.xlabel("Duration (days)")
plt.ylabel("Frequency")
plt.axvline(np.mean(durations), color='red', linestyle='--', label=f"Mean: {np.mean(durations):.1f} days")
plt.legend()

plt.tight_layout()
plt.show()

# -------- STATISTICS --------
print(f"Average cost: R${np.mean(costs):,.2f}")
print(f"90th percentile cost: R${np.percentile(costs, 90):,.2f}")
print(f"Average duration: {np.mean(durations):.2f} days")
print(f"90th percentile duration: {np.percentile(durations, 90):.2f} days")
