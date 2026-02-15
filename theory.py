import math

def gbm_theoretical_mean(S0, mu, T):
    """E[S_T] = S_0 * exp(μT)"""
    return S0 * math.exp(mu * T)

def gbm_theoretical_variance(S0, mu, sigma, T):
    """Var[S_T] = S_0² * exp(2μT) * (exp(σ²T) - 1)"""
    exp_2mu_T = math.exp(2 * mu * T)
    exp_sigma2_T = math.exp(sigma ** 2 * T)
    return (S0 ** 2) * exp_2mu_T * (exp_sigma2_T - 1)

def gbm_theoretical_std(S0, mu, sigma, T):
    """Standard deviation of GBM"""
    return math.sqrt(gbm_theoretical_variance(S0, mu, sigma, T))

def ou_theoretical_mean(X0, theta, mu, T):
    """E[X_T] = X_0 * exp(-θT) + μ * (1 - exp(-θT))"""
    exp_neg_theta_T = math.exp(-theta * T)
    return X0 * exp_neg_theta_T + mu * (1 - exp_neg_theta_T)

def ou_theoretical_variance(theta, sigma, T):
    """Var[X_T] = σ²/(2θ) * (1 - exp(-2θT))"""
    exp_neg_2theta_T = math.exp(-2 * theta * T)
    return (sigma ** 2) / (2 * theta) * (1 - exp_neg_2theta_T)

def ou_stationary_variance(theta, sigma):
    """Stationary variance: σ²/(2θ)"""
    return (sigma ** 2) / (2 * theta)

def ou_half_life(theta):
    """Half-life of OU process: ln(2) / θ"""
    return math.log(2) / theta
