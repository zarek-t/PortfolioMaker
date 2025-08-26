# main.py
import matplotlib.pyplot as plt
import numpy as np
from portfolio import (create_portfolio, get_asset_names, 
                       get_portfolio_recommendations)
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 60)
    print("           🚀 PORTFOLIO MAKER 🚀")
    print("     Your Personal Investment Portfolio Advisor")
    print("=" * 60)
    print()

def get_risk_tolerance():
    print("📊 RISK TOLERANCE ASSESSMENT")
    print("a) Conservative")
    print("b) Moderate") 
    print("c) Aggressive")
    while True:
        choice = input("Your choice (a/b/c): ").lower().strip()
        if choice == 'a':
            return "conservative"
        elif choice == 'b':
            return "moderate"
        elif choice == 'c':
            return "aggressive"
        else:
            print("❌ Invalid choice. Please enter a, b, or c.")

def get_investment_goal():
    print("\n🎯 INVESTMENT GOAL")
    print("a) Capital preservation")
    print("b) Steady growth")
    print("c) Maximum growth")
    while True:
        choice = input("Your choice (a/b/c): ").lower().strip()
        if choice == 'a':
            return "preservation"
        elif choice == 'b':
            return "growth"
        elif choice == 'c':
            return "maximum_growth"
        else:
            print("❌ Invalid choice. Please enter a, b, or c.")

def get_investment_horizon():
    print("\n⏰ INVESTMENT TIME HORIZON")
    while True:
        try:
            years = int(input("Enter years until goal: "))
            if years > 0:
                return years
            print("❌ Must be positive.")
        except ValueError:
            print("❌ Enter a valid number.")

def display_portfolio(allocation, exp_return, volatility, sharpe, max_drawdown, diversification_score, years):
    asset_names = get_asset_names()
    print("\n📊 PORTFOLIO ALLOCATION")
    for asset, pct in zip(asset_names, allocation):
        print(f"{asset}: {pct*100:.1f}%")
    print(f"\nExpected Return: {exp_return*100:.2f}%")
    print(f"Volatility: {volatility*100:.2f}%")
    print(f"Sharpe Ratio: {sharpe:.2f}")
    print(f"Max Drawdown: {max_drawdown*100:.1f}%")
    print(f"Diversification Score: {diversification_score:.2f}/1.0")

def plot_portfolio(allocation, exp_return, years):
    asset_names = get_asset_names()
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
    
    plt.figure(figsize=(10, 6))
    
    # Pie chart without labels or autopct
    wedges, _ = plt.pie(allocation, startangle=90, colors=colors, explode=[0.05]*len(allocation))
    
    # Create legend labels with asset names and percentages
    legend_labels = [f"{name}: {pct*100:.1f}%" for name, pct in zip(asset_names, allocation)]
    
    plt.legend(wedges, legend_labels, title="Asset Classes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.title(f'Portfolio Allocation ({years}-year horizon)')
    plt.tight_layout()
    plt.show()

def main():
    clear_screen()
    print_header()
    
    risk_tolerance = get_risk_tolerance()
    investment_goal = get_investment_goal()
    years = get_investment_horizon()
    
    (allocation, exp_return, volatility, sharpe, 
     max_drawdown, diversification_score) = create_portfolio(years, risk_tolerance, investment_goal)
    
    display_portfolio(allocation, exp_return, volatility, sharpe, max_drawdown, diversification_score, years)
    plot_portfolio(allocation, exp_return, years)

if __name__ == "__main__":
    main()
