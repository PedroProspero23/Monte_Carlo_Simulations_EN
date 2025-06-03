import numpy as np
import matplotlib.pyplot as plt

# -------- INITIAL SETTINGS --------
np.random.seed(42)

# Number of simulations
n_simulations = 10_000
years = 5

# Base parameters (can be adjusted or parameterized later)
average_revenue = 500_000
revenue_std_dev = 50_000
annual_fixed_cost = 100_000
variable_cost_pct = 0.3  # 30% of revenue
average_discount_rate = 0.12
discount_rate_std_dev = 0.02

# -------- NPV SIMULATION FUNCTION --------
def simulate_npv():
    revenue = np.random.normal(average_revenue, revenue_std_dev, years)
    variable_costs = revenue * variable_cost_pct
    total_costs = variable_costs + annual_fixed_cost
    cash_flow = revenue - total_costs

    discount_rate = np.random.normal(average_discount_rate, discount_rate_std_dev)
    discount_factors = [(1 / (1 + discount_rate)) ** i for i in range(1, years + 1)]
    npv = np.sum(cash_flow * discount_factors)
    return npv

# -------- RUNNING MONTE CARLO SIMULATION --------
npvs = [simulate_npv() for _ in range(n_simulations)]

# -------- RESULT VISUALIZATION --------
plt.hist(npvs, bins=50, edgecolor='black')
plt.title("NPV Distribution (Monte Carlo Simulation)")
plt.xlabel("Net Present Value (R$)")
plt.ylabel("Frequency")
plt.axvline(np.mean(npvs), color='red', linestyle='dashed', linewidth=2,
            label=f"Mean NPV: R${np.mean(npvs):,.2f}")
plt.legend()
plt.tight_layout()
plt.show()

# -------- DESCRIPTIVE STATISTICS --------
print(f"Mean NPV: R${np.mean(npvs):,.2f}")
print(f"Minimum NPV: R${np.min(npvs):,.2f}")
print(f"Maximum NPV: R${np.max(npvs):,.2f}")
print(f"10th Percentile NPV: R${np.percentile(npvs, 10):,.2f}")
print(f"90th Percentile NPV: R${np.percentile(npvs, 90):,.2f}")
