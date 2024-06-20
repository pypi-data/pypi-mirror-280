import numpy as np
import pandas as pd
import pymc as pm
import pytensor.tensor as at

class Prophetoid:
    """Model inspired by Facebook's Prophet."""

    def __init__(self, data, date_col, target_col, group_cols, fourier_order=1):
        self.data = data.copy()
        self.date_col = date_col
        self.target_col = target_col
        self.group_cols = group_cols
        self.fourier_order = fourier_order
        self.model = None

    def prepare_data(self):
        # Ensure the date column is in datetime format
        self.data[self.date_col] = pd.to_datetime(self.data[self.date_col])

        # Extracting the day of the week
        self.data['weekday'] = self.data[self.date_col].dt.dayofweek

        # Creating Fourier series terms for seasonality (365.24-day period)
        t = (self.data[self.date_col] - self.data[self.date_col].min()).dt.total_seconds() / (24 * 3600)  # time in days since start

        for k in range(1, self.fourier_order + 1):
            self.data[f'cos_term_{k}'] = np.cos(2 * np.pi * k * t / 365.24)
            self.data[f'sin_term_{k}'] = np.sin(2 * np.pi * k * t / 365.24)

    def build_model(self):
        # Prepare data
        self.prepare_data()

        # Extract the unique categories for the groupings
        coords = {col: self.data[col].unique().tolist() for col in self.group_cols}
        coords['weekday'] = np.arange(7).tolist()

        with pm.Model(coords=coords) as model:
            # Priors for fixed effects
            intercept = pm.Normal("intercept", mu=0, sigma=1)

            beta_cos = {}
            beta_sin = {}
            for k in range(1, self.fourier_order + 1):
                beta_cos[k] = pm.Normal(f"beta_cos_{k}", mu=0, sigma=1)
                beta_sin[k] = pm.Normal(f"beta_sin_{k}", mu=0, sigma=1)

            beta_weekday = pm.Normal("beta_weekday", mu=0, sigma=1, dims="weekday")

            # Random effects for groupings
            group_betas = {}
            for col in self.group_cols:
                group_betas[col] = pm.Normal(f"beta_{col}", mu=0, sigma=1, dims=col)

            # Construct the linear predictor
            mu = intercept
            for k in range(1, self.fourier_order + 1):
                X_cos = self.data[f'cos_term_{k}'].values
                X_sin = self.data[f'sin_term_{k}'].values
                mu += beta_cos[k] * X_cos + beta_sin[k] * X_sin

            X_weekday = self.data['weekday'].values
            mu += beta_weekday[X_weekday]

            for col in self.group_cols:
                X_group = pd.Categorical(self.data[col]).codes
                mu += group_betas[col][X_group]

            # Likelihood (observed data)
            lambda_ = pm.math.exp(mu)
            observed_data = self.data[self.target_col].values
            pm.Poisson("observed", mu=lambda_, observed=observed_data)

        self.model = model

    def fit(self, draws=1000, tune=1000):
        with self.model:
            self.trace = pm.sample(draws=draws, tune=tune, return_inferencedata=True, idata_kwargs={"log_likelihood": True})

    def get_trace(self):
        return self.trace

