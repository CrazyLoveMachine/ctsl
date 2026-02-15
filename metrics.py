import math
import statistics

def calculate_statistics(prices):
    mean = statistics.mean(prices)
    median = statistics.median(prices)
    stddev = statistics.stdev(prices)
    return {'mean': mean, 'median': median, 'stddev': stddev}

def percentage_error(actual, expected):
    return abs((actual - expected) / expected) * 100

def relative_error(actual, expected):
    return abs((actual - expected) / actual) * 100
