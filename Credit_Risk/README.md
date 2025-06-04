# Debt Coverage Risk Analysis using Monte Carlo Simulation

This project evaluates a borrower's ability to service debt based on uncertain revenue conditions. It uses a **Monte Carlo simulation** to estimate the **Debt Service Coverage Ratio (DSCR)**, also known as **ICD (Índice de Cobertura da Dívida)** in Portuguese.

---

# Objective

Simulate how changes in revenue impact a company's **capacity to repay its debt**, and estimate the probability of:
- **Default** (ICD < 1)
- **Stress** (ICD < minimum safety threshold)

---

# Problem Overview

Parameters:
- Expected Revenue: R$ 1,000,000  
- Revenue Volatility: ±R$ 150,000  
- Fixed Cost: R$ 400,000  
- Variable Cost: 35% of Revenue  
- Annual Debt Service: R$ 300,000  
- Desired ICD Threshold: 1.2

---

# Methodology

For each of the 10,000 simulations:
1. Randomly sample revenue from a normal distribution.
2. Calculate:
   - Variable Cost = 35% of revenue
   - Cash Flow = Revenue - Variable Cost - Fixed Cost
3. If cash flow is positive:
   - Compute ICD = Cash Flow / Debt Service
   - Else, ICD = 0 (no coverage)

---

# Key Outputs

- Histogram of simulated ICD values
- Red line: **mean ICD**
- Blue line: **safety threshold (ICD = 1.2)**

# Sample Output:

```text
Mean ICD: 1.65
Probability of default (ICD < 1): 9.73%
Probability of being below safety threshold (ICD < 1.2): 19.64%
