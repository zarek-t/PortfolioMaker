# portfolio.py

def create_portfolio(years, risk):
    # Base allocations
    allocations = {
        "low": {"Stocks": 40, "Bonds": 50, "Cash": 10},
        "medium": {"Stocks": 60, "Bonds": 30, "Cash": 10},
        "high": {"Stocks": 80, "Bonds": 15, "Cash": 5}
    }

    portfolio = allocations.get(risk, allocations["medium"])

    # Adjust based on years
    if years >= 20:
        portfolio["Stocks"] += 10
        portfolio["Bonds"] -= 5
        portfolio["Cash"] -= 5
    elif years <= 5:
        portfolio["Stocks"] -= 10
        portfolio["Bonds"] += 5
        portfolio["Cash"] += 5

    return portfolio

