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
    print("           🚀 PORTFOLIO MAKER PRO 🚀")
    print("     Your Personal Investment Portfolio Advisor")
    print("=" * 60)
    print()

def get_risk_tolerance():
    # Simplified risk assessment
    print("📊 RISK TOLERANCE ASSESSMENT")
    options = ["conservative", "moderate", "aggressive"]
    while True:
        choice = input("Enter risk tolerance (conservative/moderate/aggressive): ").lower()
        if choice in options:
            return choice
        print("❌ Invalid choice. Try again.")

def get_investment_goal():
    print("\n🎯 INVESTMENT GOAL")
    options = ["preservation", "growth", "maximum_growth"]
    while True:
        choice = input("Enter investment goal (preservation/growth/maximum_growth): ").lower()
        if choice in options:
            return choice
        print("❌ Invalid choice. Try again.")

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
    
    plt.figure(figsize=(8, 6))
    plt.pie(allocation, labels=asset_names, autopct='%1.1f%%', startangle=90, colors=colors, explode=[0.05]*len(allocation))
    plt.title(f'Portfolio Allocation ({years}-year horizon)')
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
