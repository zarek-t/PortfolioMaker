# portfolio.py
import numpy as np

def create_portfolio(years, risk_tolerance="moderate", investment_goal="growth"):
    """
    Returns allocation, expected return, volatility, sharpe ratio,
    max drawdown, and diversification score.
    """
    returns = np.array([0.09, 0.08, 0.04, 0.06, 0.02, 0.05])
    stdevs = np.array([0.16, 0.18, 0.06, 0.15, 0.01, 0.20])
    correlations = np.array([
        [1.00, 0.85, -0.10, 0.60, -0.05, 0.20],
        [0.85, 1.00, -0.15, 0.55, -0.08, 0.25],
        [-0.10, -0.15, 1.00, 0.10, 0.95, -0.20],
        [0.60, 0.55, 0.10, 1.00, 0.05, 0.30],
        [-0.05, -0.08, 0.95, 0.05, 1.00, -0.15],
        [0.20, 0.25, -0.20, 0.30, -0.15, 1.00]
    ])

    # Base allocation by horizon
    if years <= 3:
        base = np.array([0.15, 0.10, 0.60, 0.05, 0.05, 0.05])
    elif years <= 7:
        base = np.array([0.30, 0.20, 0.35, 0.10, 0.03, 0.02])
    elif years <= 15:
        base = np.array([0.45, 0.25, 0.20, 0.05, 0.03, 0.02])
    elif years <= 25:
        base = np.array([0.60, 0.25, 0.10, 0.03, 0.01, 0.01])
    else:
        base = np.array([0.70, 0.20, 0.05, 0.03, 0.01, 0.01])

    # Apply risk tolerance to stocks only
    risk_mults = {"conservative": 0.7, "moderate": 1.0, "aggressive": 1.2}
    stock_indices = [0, 1]
    base[stock_indices] *= risk_mults.get(risk_tolerance, 1.0)

    # Apply goal multiplier
    goal_mults = {"preservation": 0.8, "growth": 1.0, "maximum_growth": 1.2}
    base *= goal_mults.get(investment_goal, 1.0)

    # Ensure minimum 1% allocation and normalize
    base = np.maximum(base, 0.01)
    allocation = base / base.sum()

    # Portfolio metrics
    exp_return = np.dot(allocation, returns)
    portfolio_var = allocation @ (np.outer(stdevs, stdevs) * correlations) @ allocation
    volatility = np.sqrt(portfolio_var)
    sharpe = (exp_return - 0.02) / volatility

    max_drawdown = np.sqrt(np.sum(allocation**2 * stdevs**2)) * 2.5
    diversification_score = calculate_diversification_score(allocation, correlations)

    return allocation, exp_return, volatility, sharpe, max_drawdown, diversification_score

def calculate_diversification_score(allocation, correlations):
    n = len(allocation)
    concentration = np.sum(allocation**2)
    avg_corr = np.sum(np.triu(np.abs(correlations), k=1)) * 2 / (n*(n-1))
    return max(0, min(1, (1 - concentration) * (1 - avg_corr)))

def get_asset_names():
    return ["US Stocks", "International Stocks", "Bonds", "Real Estate", "Cash", "Commodities"]

def get_portfolio_recommendations(allocation, years, risk_tolerance, investment_goal):
    asset_names = get_ass
