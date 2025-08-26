# main.py
from portfolio import create_portfolio
import matplotlib.pyplot as plt

def display_portfolio_chart(portfolio):
    labels = portfolio.keys()
    sizes = portfolio.values()
    colors = ['#4CAF50', '#2196F3', '#FFC107']  # Stocks, Bonds, Cash
    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title("Recommended Portfolio Allocation")
    plt.show()

def main():
    print("Welcome to AutoPortfolio!")
    
    # Get user input
    while True:
        try:
            years = int(input("Enter the number of years until your investment goal: "))
            if years <= 0:
                print("Please enter a positive number of years.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    while True:
        risk = input("Enter your risk tolerance (low/medium/high): ").lower()
        if risk not in ["low", "medium", "high"]:
            print("Invalid input. Please enter 'low', 'medium', or 'high'.")
            continue
        break

    # Generate portfolio
    portfolio = create_portfolio(years, risk)
    
    # Display portfolio
    print("\nRecommended Portfolio Allocation:")
    for asset, percent in portfolio.items():
        print(f"{asset}: {percent}%")
    
    # Show chart
    display_portfolio_chart(portfolio)

if __name__ == "__main__":
    main()
