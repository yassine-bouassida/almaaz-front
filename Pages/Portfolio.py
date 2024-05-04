import streamlit as st
import pandas as pd

# Define function for the portfolio page
def portfolio():
    st.title("Portfolio")

    # Simulated portfolio data
    portfolio_data = {
        'Cash Available': 10000,
        'Total Invested': 90000,
        'Profit/Loss': 5000,
        'Portfolio Value': 95000
    }

    # Display blocks for cash available, total invested, profit/loss, and portfolio value
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("Cash Available")
        st.write(f"${portfolio_data['Cash Available']}")
    with col2:
        st.subheader("Total Invested")
        st.write(f"${portfolio_data['Total Invested']}")
    with col3:
        st.subheader("Profit/Loss")
        st.write(f"${portfolio_data['Profit/Loss']}")
    with col4:
        st.subheader("Portfolio Value")
        st.write(f"${portfolio_data['Portfolio Value']}")

    # Display portfolio holdings
    st.subheader("Portfolio Holdings")
    holdings_data = {
        'Symbol': ['AAPL', 'GOOGL', 'MSFT'],
        'Shares': [100, 50, 75],
        'Price': [150.20, 2500.50, 300.75],
        'Value': [15020.00, 125025.00, 22556.25]
    }
    holdings_df = pd.DataFrame(holdings_data)
    st.write(holdings_df)

    # Display portfolio performance
    st.subheader("Portfolio Performance")
    st.line_chart(data=portfolio_performance())

# Function to generate dummy portfolio performance data (just for demonstration)
def portfolio_performance():
    # Generate some random portfolio performance data
    # Replace this with actual data or calculations based on your needs
    import numpy as np
    import pandas as pd

    dates = pd.date_range(start='2023-01-01', end='2024-01-01', freq='D')
    prices = np.random.normal(loc=100, scale=1, size=len(dates)).cumsum()
    portfolio_performance_data = pd.DataFrame({'Date': dates, 'Portfolio Value': prices})
    portfolio_performance_data.set_index('Date', inplace=True)
    return portfolio_performance_data

# Display the portfolio page
portfolio()
