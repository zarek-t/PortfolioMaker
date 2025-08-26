# app.py
import streamlit as st
from portfolio import create_portfolio, get_asset_names
import matplotlib.pyplot as plt

st.set_page_config(page_title="Portfolio Maker Pro", layout="wide")
st.title("🚀 Portfolio Maker Pro")
st.subheader("Your Personal Investment Portfolio Advisor")

# Inputs
risk = st.radio("Risk Tolerance", ["Conservative", "Moderate", "Aggressive"])
goal = st.radio("Investment Goal", ["Preservation", "Growth", "Maximum Growth"])
years = st.slider("Investment Horizon (years)", min_value=1, max_value=50, value=10)

# Generate portfolio
allocation, exp_return, volatility, sharpe, max_drawdown, diversification_score = create_portfolio(
    years, risk.lower(), goal.lower()
)

# Metrics display
st.markdown("### 📊 Portfolio Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Expected Return", f"{exp_return*100:.2f}%")
col2.metric("Volatility", f"{volatility*100:.2f}%")
col3.metric("Sharpe Ratio", f"{sharpe:.2f}")

col4, col5 = st.columns(2)
col4.metric("Max Drawdown", f"{max_drawdown*100:.1f}%")
col5.metric("Diversification Score", f"{diversification_score:.2f}/1.0")

# Pie chart
asset_names = get_asset_names()
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']

fig, ax = plt.subplots()
ax.pie(allocation, startangle=90, colors=colors, explode=[0.05]*len(allocation))
legend_labels = [f"{name}: {pct*100:.1f}%" for name, pct in zip(asset_names, allocation)]
ax.legend(legend_labels, title="Asset Classes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
ax.set_title(f"Portfolio Allocation ({years}-year horizon)")
st.pyplot(fig)
