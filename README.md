# 🚀 Portfolio Maker Pro

A sophisticated Python application that generates personalized investment portfolios based on your investment timeline, risk tolerance, and financial goals. This tool provides comprehensive portfolio analysis with professional-grade visualizations and detailed recommendations.

## ✨ Features

### 🎯 **Personalized Portfolio Creation**
- **Risk Tolerance Assessment**: Interactive questionnaire to determine your comfort level with market volatility
- **Investment Goal Selection**: Choose between capital preservation, steady growth, or maximum growth
- **Time Horizon Analysis**: Optimized allocations for short-term (1-3 years) to very long-term (25+ years) investments

### 📊 **Advanced Portfolio Analysis**
- **6 Asset Classes**: US Stocks, International Stocks, Bonds, Real Estate, Cash, and Commodities
- **Correlation Matrix**: Sophisticated portfolio optimization using asset correlation data
- **Risk Metrics**: Expected return, volatility, Sharpe ratio, maximum drawdown, and diversification score
- **Professional Recommendations**: Actionable advice based on your portfolio metrics

### 📈 **Enhanced Visualizations**
- **Multi-Panel Charts**: Comprehensive 4-panel dashboard showing:
  - Asset allocation pie chart
  - Allocation percentage bars
  - Risk-return scatter plot
  - Portfolio growth projection
- **Interactive Elements**: Color-coded assets with professional styling
- **Export Options**: Save detailed reports as text files

### 🔄 **User Experience**
- **Professional Interface**: Clean, intuitive command-line interface with emojis and clear formatting
- **Error Handling**: Robust input validation and graceful error recovery
- **Multiple Sessions**: Create multiple portfolios in one session
- **Report Generation**: Save and share your portfolio recommendations

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Required packages (see requirements.txt)

### Installation
1. Clone or download the project files
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

### Usage Example
```
🚀 PORTFOLIO MAKER PRO 🚀
     Your Personal Investment Portfolio Advisor
============================================================

📊 RISK TOLERANCE ASSESSMENT
----------------------------------------

1. How would you react if your portfolio dropped 20% in a year?
   a) Sell everything immediately
   b) Feel nervous but hold on
   c) See it as a buying opportunity

Your choice (a/b/c): b

✅ Your risk tolerance: MODERATE

🎯 INVESTMENT GOAL
----------------------------------------
1. Capital Preservation - Focus on protecting your money
2. Steady Growth - Balanced approach for moderate returns
3. Maximum Growth - Aggressive approach for highest returns

Select your goal (1/2/3): 2
✅ Selected goal: Growth

⏰ INVESTMENT TIME HORIZON
----------------------------------------
How many years until you need this money?
• 1-3 years: Very short-term (capital preservation)
• 4-7 years: Short-term (conservative growth)
• 8-15 years: Medium-term (balanced)
• 16-25 years: Long-term (growth-oriented)
• 25+ years: Very long-term (aggressive growth)

Enter years: 15
✅ Investment horizon: 15 years

🔄 Generating your personalized portfolio...
```

## 📁 Project Structure

```
PortfolioMaker/
├── main.py              # Main application with enhanced UI
├── portfolio.py         # Core portfolio logic and calculations
├── requirements.txt     # Python dependencies
└── README.md           # This documentation
```

## 🔧 Technical Details

### Portfolio Optimization Algorithm
- **Modern Portfolio Theory**: Uses correlation matrices for accurate risk calculation
- **Risk-Adjusted Returns**: Sharpe ratio optimization with realistic risk-free rates
- **Diversification Scoring**: Quantitative assessment of portfolio diversification quality
- **Dynamic Allocation**: Time horizon and risk tolerance adjustments

### Asset Class Assumptions
- **US Stocks**: 9% expected return, 16% volatility
- **International Stocks**: 8% expected return, 18% volatility  
- **Bonds**: 4% expected return, 6% volatility
- **Real Estate**: 6% expected return, 15% volatility
- **Cash**: 2% expected return, 1% volatility
- **Commodities**: 5% expected return, 20% volatility

### Risk Tolerance Levels
- **Conservative**: 60% of base allocation (capital preservation focus)
- **Moderate**: 100% of base allocation (balanced approach)
- **Aggressive**: 140% of base allocation (growth focus)

## 📊 Sample Output

The application generates comprehensive portfolio analysis including:

- **Asset Allocation**: Percentage breakdown across 6 asset classes
- **Portfolio Metrics**: Expected return, volatility, Sharpe ratio
- **Risk Assessment**: Maximum drawdown estimates and diversification scores
- **Visual Charts**: Professional 4-panel dashboard
- **Text Report**: Detailed analysis saved to file

## 🎯 Use Cases

- **Individual Investors**: Personal retirement planning and goal-based investing
- **Financial Advisors**: Client portfolio recommendations and analysis
- **Educational Purposes**: Learning about modern portfolio theory and asset allocation
- **Financial Planning**: Goal-based investment strategy development

## 🔮 Future Enhancements

- **Real Market Data**: Integration with financial APIs for current market conditions
- **Monte Carlo Simulation**: Advanced portfolio projection modeling
- **Tax Optimization**: Tax-efficient allocation strategies
- **Rebalancing Alerts**: Portfolio maintenance recommendations
- **Web Interface**: Browser-based application with interactive charts
- **Mobile App**: Cross-platform mobile application

## 🤝 Contributing

Contributions are welcome! Areas for improvement include:
- Additional asset classes and investment strategies
- Enhanced risk modeling and stress testing
- Integration with financial data providers
- Performance optimization and code quality improvements

## 📄 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

This tool is for educational and informational purposes only. It does not constitute financial advice. Always consult with a qualified financial advisor before making investment decisions. Past performance does not guarantee future results, and all investments carry risk.

---

**Built with ❤️ for better financial decision making**
