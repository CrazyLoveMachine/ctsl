import argparse
import numpy as np
import matplotlib.pyplot as plt

# GBM Exact Method 
def gbm_exact(S0, mu, sigma, T, dt, N):
    ts = np.linspace(0, T, N+1)
    W = np.random.standard_normal(size=N)  # Brownian increments
    W = np.concatenate(([0], np.cumsum(W)))  # Cumulative sum to create Wiener process
    S = S0 * np.exp((mu - 0.5 * sigma**2) * ts + sigma * W)
    return ts, S

# GBM Euler Method 
def gbm_euler(S0, mu, sigma, T, dt):
    N = int(T / dt)
    S = np.zeros(N+1)
    S[0] = S0
    for t in range(1, N+1):
        Z = np.random.standard_normal()
        S[t] = S[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
    return np.linspace(0, T, N+1), S

# OU Process Simulation

def ou_process(X0, mu, theta, sigma, T, dt):
    N = int(T / dt)
    X = np.zeros(N+1)
    X[0] = X0
    for t in range(1, N+1):
        Z = np.random.standard_normal()
        X[t] = X[t-1] + theta * (mu - X[t-1]) * dt + sigma * np.sqrt(dt) * Z
    return np.linspace(0, T, N+1), X

# Function to validate inputs

def validate_inputs(args):
    if args.S0 <= 0 or args.sigma < 0 or args.T <= 0 or args.dt <= 0:
        raise ValueError("Initial stock price (S0), volatility (sigma), total time (T), and time step (dt) must be positive.")

# Main function to handle CLI commands

def main():
    parser = argparse.ArgumentParser(description='Simulate GBM and OU processes')
    parser.add_argument('--S0', type=float, required=True, help='Initial stock price for GBM')
    parser.add_argument('--mu', type=float, required=True, help='Drift coefficient for GBM or mean for OU process')
    parser.add_argument('--sigma', type=float, required=True, help='Volatility for GBM or standard deviation for OU process')
    parser.add_argument('--T', type=float, required=True, help='Total time length for the simulation')
    parser.add_argument('--dt', type=float, required=True, help='Time step for the simulation')
    parser.add_argument('--method', choices=['exact', 'euler', 'ou'], required=True, help='Method to use: GBM Exact, GBM Euler, or OU Process')

    args = parser.parse_args()

    # Validate inputs
    validate_inputs(args)

    # Simulation based on method
    if args.method == 'exact':
        ts, S = gbm_exact(args.S0, args.mu, args.sigma, args.T, args.dt, int(args.T / args.dt))
        plt.plot(ts, S, label='GBM Exact')
    elif args.method == 'euler':
        ts, S = gbm_euler(args.S0, args.mu, args.sigma, args.T, args.dt)
        plt.plot(ts, S, label='GBM Euler')
    elif args.method == 'ou':
        ts, X = ou_process(args.S0, args.mu, args.sigma, args.sigma, args.T, args.dt)
        plt.plot(ts, X, label='OU Process')

    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Simulation of Processes')
    plt.legend()
    plt.show()

# Entry point for execution
if __name__ == '__main__':
    main()