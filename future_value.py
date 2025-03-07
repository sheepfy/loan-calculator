import numpy as np
from scipy.optimize import bisect

A = 1_000_000
P = 100_000
r = 0.07
n = 12
M = 2000

def future_value(t):
    return P * (1 + r/n)**(n*t) + M * (((1 + r/n)**(n*t) - 1) / (r/n)) - A

t_solution = bisect(future_value, 0, 100)

t_years = t_solution
t_months = t_solution * 12

total_deposits = P + M * t_months
total_interest = A - total_deposits

print(f"Time in years: {t_years:.2f}")
print(f"Time in months: {t_months:.2f}")
print(f"Total deposits: {total_deposits:.2f}")
print(f"Total interest: {total_interest:.2f}")
