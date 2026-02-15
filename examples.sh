#!/bin/bash

# Example 1: GBM Exact Solution
# Simulate the exact solution of a Geometric Brownian Motion (GBM)
simulate_gbm_exact() {
  local mu=0.1
  local sigma=0.2
  local S0=100
  local T=1
  local dt=0.01
  local steps=$((T/dt))
  
  # Generate time vector
  for i in $(seq 0 $steps); do
    t=$(echo "scale=4; $i * $dt" | bc)
    S=$(echo "scale=4; $S0 * e( ($mu - ($sigma^2)/2) * $t + $sigma * sqrt($t) * ($RANDOM%100)/100)" | bc)
    echo "Time: $t, Stock Price: $S"
  done
}

# Example 2: GBM Euler Discretization
# Simulate a GBM using the Euler method
simulate_gbm_euler() {
  local mu=0.1
  local sigma=0.2
  local S0=100
  local T=1
  local dt=0.01
  local steps=$((T/dt))

  S=$S0
  # Generate time vector
  for (( i=0; i<=steps; i++ )); do
    dW=$(echo "scale=4; sqrt($dt) * ($RANDOM%100)/100" | bc)
    S=$(echo "scale=4; $S * e( ($mu - 0.5 * $sigma^2) * $dt + $sigma * dW)" | bc)
    echo "Time: $(echo "scale=4; $i * $dt" | bc), Stock Price: $S"
  done
}

# Example 3: High Volatility Scenario
# Simulate high volatility scenario in GBM
simulate_high_volatility() {
  local mu=0.1
  local sigma=0.5  # High volatility
  local S0=100
  local T=1
  local dt=0.01
  local steps=$((T/dt))

  S=$S0
  for (( i=0; i<=steps; i++ )); do
    dW=$(echo "scale=4; sqrt($dt) * ($RANDOM%100)/100" | bc)
    S=$(echo "scale=4; $S * e( ($mu - 0.5 * $sigma^2) * $dt + $sigma * dW)" | bc)
    echo "Time: $(echo "scale=4; $i * $dt" | bc), Stock Price (High Volatility): $S"
  done
}

# Example 4: Ornstein-Uhlenbeck Mean Reversion
# Simulate an Ornstein-Uhlenbeck process
simulate_mean_reversion() {
  local mu=100  # Long-term mean
  local theta=0.1
  local sigma=0.2
  local S0=50
  local T=1
  local dt=0.01
  local steps=$((T/dt))

  S=$S0
  for (( i=0; i<=steps; i++ )); do
    dW=$(echo "scale=4; sqrt($dt) * ($RANDOM%100)/100" | bc)
    S=$(echo "scale=4; $S + $theta * ($mu - $S) * $dt + $sigma * dW" | bc)
    echo "Time: $(echo "scale=4; $i * $dt" | bc), Price (Mean Reversion): $S"
  done
}

# Example 5: Convergence Validation
# Validate convergence of a simulation
validate_convergence() {
  local results=()
  for dt in 0.1 0.05 0.01; do
    S=$100
    for i in $(seq 1 10); do
      S=$(echo "scale=4; $S * e(0.1 * $dt)" | bc)
    done
    results+=($S)
  done
  echo "Convergence Results: ${results[@]}"
}

# Example 6: Comparison of Discretization Steps
# Compare results with different steps
compare_discretization() {
  for dt in 0.1 0.05 0.01; do
    echo "Using dt = $dt"
    simulate_gbm_euler $dt
  done
}

# Run examples
simulate_gbm_exact
simulate_gbm_euler
simulate_high_volatility
simulate_mean_reversion
validate_convergence
compare_discretization
