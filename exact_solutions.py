import math
import random

def simulate_gbm_exact(S0, mu, sigma, T, n_paths):
    """Exact GBM solution: S_T = S_0 * exp((μ - σ²/2)T + σ√T * Z)"""
    sqrt_T = math.sqrt(T)
    drift = (mu - 0.5 * sigma ** 2) * T
    vol_factor = sigma * sqrt_T
    prices = [S0 * math.exp(drift + vol_factor * random.gauss(0, 1)) for _ in range(n_paths)]
    return prices

def theoretical_gbm_mean(S0, mu, T):
    """E[S_T] = S_0 * exp(μT)"""
    return S0 * math.exp(mu * T)

def theoretical_gbm_variance(S0, mu, sigma, T):
    """Var[S_T] = S_0² * exp(2μT) * (exp(σ²T) - 1)"""
    exp_2mu_T = math.exp(2 * mu * T)
    exp_sigma2_T = math.exp(sigma ** 2 * T)
    return (S0 ** 2) * exp_2mu_T * (exp_sigma2_T - 1)