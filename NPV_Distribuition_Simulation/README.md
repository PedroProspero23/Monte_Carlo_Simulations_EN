# NPV Simulation using Monte Carlo Method

This project simulates the **Net Present Value (NPV)** of a business over a 5-year horizon using a **Monte Carlo simulation** approach. It incorporates randomness in both **revenue generation** and the **discount rate**, providing a realistic view of project uncertainty.

---

# Objective

Estimate the possible range and probability distribution of a project's NPV considering variability in:
- Annual revenues
- Discount rates
- Operational costs (fixed and variable)

---

# Problem Overview

### Base Assumptions:
- Revenue follows a **normal distribution**  
- Discount rate is **variable** per simulation  
- Costs are split into:
  - **Fixed costs** (R$100,000/year)
  - **Variable costs** (30% of revenue)

---

# Model Parameters

```python
average_revenue = 500_000
revenue_std_dev = 50_000
annual_fixed_cost = 100_000
variable_cost_pct = 0.30
average_discount_rate = 0.12
discount_rate_std_dev = 0.02
years = 5
n_simulations = 10_000
