import numpy as np

# Euler-Maruyama method for Geometric Brownian Motion (GBM)
def euler_maruyama_gbm(S0, mu, sigma, T, N):
    dt = T / N
    S = np.zeros(N+1)
    S[0] = S0
    for n in range(1, N+1):
        Z = np.random.normal()
        S[n] = S[n-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
    return S

# Euler-Maruyama method for Ornstein-Uhlenbeck (OU) process
def euler_maruyama_ou(X0, mu, theta, sigma, T, N):
    dt = T / N
    X = np.zeros(N+1)
    X[0] = X0
    for n in range(1, N+1):
        Z = np.random.normal()
        X[n] = X[n-1] + mu * (theta - X[n-1]) * dt + sigma * np.sqrt(dt) * Z
    return X

# Example usage:
# S = euler_maruyama_gbm(S0=100, mu=0.1, sigma=0.2, T=1, N=1000)
# X = euler_maruyama_ou(X0=0, mu=0.1, theta=0, sigma=0.2, T=1, N=1000)