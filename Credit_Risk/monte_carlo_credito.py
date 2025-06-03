import numpy as np
import matplotlib.pyplot as plt

# -------- INITIAL CONFIGURATION --------
np.random.seed(42)
n_simulations = 10_000

# Client parameters
average_revenue = 1_000_000   # Expected annual revenue (R$)
revenue_std_dev = 150_000     # Revenue variation
fixed_cost = 400_000          # Annual fixed cost
variable_cost_pct = 0.35      # 35% of revenue

# Debt
annual_debt_service = 300_000  # Annual payments (interest + principal)
icd_threshold = 1.2  # Minimum desired ICD (e.g., 1.2 → cash flow must be 20% greater than debt)

# -------- SIMULATION FUNCTION --------
def simulate_coverage_ratio():
    revenue = np.random.normal(average_revenue, revenue_std_dev)
    variable_cost = revenue * variable_cost_pct
    cash_flow = revenue - variable_cost - fixed_cost
    if cash_flow < 0:
        return 0  # doesn't cover any debt
    icd = cash_flow / annual_debt_service
    return icd

# -------- RUNNING MONTE CARLO SIMULATION --------
icds = [simulate_coverage_ratio() for _ in range(n_simulations)]

# -------- RESULT ANALYSIS --------
prob_default = np.mean([icd < 1 for icd in icds])
prob_below_threshold = np.mean([icd < icd_threshold for icd in icds])
average_icd = np.mean(icds)

# -------- VISUALIZATION --------
plt.hist(icds, bins=50, color='orange', edgecolor='black')
plt.axvline(average_icd, color='red', linestyle='--', label=f"Mean ICD: {average_icd:.2f}")
plt.axvline(icd_threshold, color='blue', linestyle='--', label=f"Desired Threshold: {icd_threshold}")
plt.title("Debt Coverage Ratio (ICD) Distribution")
plt.xlabel("ICD (cash flow / debt service)")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()

# -------- OUTPUT --------
print(f"Mean ICD: {average_icd:.2f}")
print(f"Probability of default (ICD < 1): {prob_default:.2%}")
print(f"Probability of being below safety threshold (ICD < {icd_threshold}): {prob_below_threshold:.2%}")
