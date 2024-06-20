import markdown

markdown.Markdown(extensions=['pymdownx.snippets'])

# --8<-- [start:func]
from pppmodels import Prophetoid
import numpy as np
import pandas as pd


# Generate example data with seasonal, weekday, and group effects
np.random.seed(42)
date_rng = pd.date_range(start='2023-01-01', end='2023-01-31', freq='D')
n = len(date_rng)

# Seasonal effects
t = np.arange(n)
cos_term_1 = np.cos(2 * np.pi * t / 365.24)
sin_term_1 = np.sin(2 * np.pi * t / 365.24)
cos_term_2 = np.cos(4 * 2 * np.pi * t / 365.24)  # Second order
sin_term_2 = np.sin(4 * 2 * np.pi * t / 365.24)  # Second order

# Weekday effects
weekday = date_rng.dayofweek

# Group effects
group1 = np.random.choice(['A', 'B'], size=n)
group2 = np.random.choice(['X', 'Y'], size=n)

data = pd.DataFrame({
    'date': date_rng,
    'group1': group1,
    'group2': group2,
    'weekday': weekday,
    'target': np.random.poisson(lam=np.exp(0.5 + 0.3 * cos_term_1 + 0.2 * sin_term_1 + 0.1 * cos_term_2 + 0.1 * sin_term_2
                                          + 0.2 * (weekday - 3)**2 + 0.5 * (group1 == 'A') - 0.5 * (group2 == 'Y')), size=n)
})

# Instantiate and use the model with Fourier series order 2
model = Prophetoid(data=data, date_col='date', target_col='target', group_cols=['group1', 'group2'], fourier_order=2)
model.build_model()
model.fit()

# Get the trace and print summary
trace = model.get_trace()
print(pm.summary(trace))

import arviz as az

print(az.loo(trace))

# --8<-- [end:func]
