from exact_solutions import simulate_gbm_exact, theoretical_gbm_mean

def validate_gbm_convergence(S0, mu, sigma, T, path_counts):
    """Validate GBM convergence by Law of Large Numbers"""
    theoretical_mean = theoretical_gbm_mean(S0, mu, T)
    simulated_means = []
    errors = []
    for n_paths in path_counts:
        prices = simulate_gbm_exact(S0, mu, sigma, T, n_paths)
        simulated_mean = sum(prices) / len(prices)
        simulated_means.append(simulated_mean)
        error = abs(simulated_mean - theoretical_mean) / theoretical_mean * 100
        errors.append(error)
    return {
        'theoretical_mean': theoretical_mean,
        'simulated_means': simulated_means,
        'errors': errors
    }

def check_discretization_error(exact_prices, approx_prices):
    """Compare exact vs approximate simulation results"""
    if len(exact_prices) != len(approx_prices):
        raise ValueError("Price lists must have same length")
    exact_mean = sum(exact_prices) / len(exact_prices)
    approx_mean = sum(approx_prices) / len(approx_prices)
    exact_var = sum((p - exact_mean) ** 2 for p in exact_prices) / len(exact_prices)
    approx_var = sum((p - approx_mean) ** 2 for p in approx_prices) / len(approx_prices)
    mean_error = abs(approx_mean - exact_mean) / exact_mean * 100
    var_error = abs(approx_var - exact_var) / exact_var * 100
    return {
        'exact_mean': exact_mean,
        'approx_mean': approx_mean,
        'exact_var': exact_var,
        'approx_var': approx_var,
        'mean_error_pct': mean_error,
        'var_error_pct': var_error
    }