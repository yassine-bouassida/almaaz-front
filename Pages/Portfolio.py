import streamlit as st
import pandas as pd

# Define function for the portfolio page
#cach
@st.cache_data()
def get_ticker_list():
    return pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
@st.cache_data()
def get_strategy_list():
    return pd.read_csv("strat.csv")

def get_investments():
    df=pd.read_csv("investments.csv")
    if df.empty:
        return pd.DataFrame(columns=["Ticker","Strategy"])
    return df
def add_new_investment(strategy):
    new_investment = st.session_state.new_investment
    investments = get_investments()
    #add new investment to investments
    new_investment_df = pd.DataFrame(new_investment,columns=["Ticker"])
    #add strategy
    new_investment_df["Strategy"] = strategy
    investments = pd.concat([investments,new_investment_df])
    investments.to_csv("investments.csv",index=False)
    #clear new_investment
    st.session_state.new_investment = []


def add_ticker(ticker):
    st.session_state.new_investment.append(ticker)

def add_investment():
    st.title("Add Investment")
    if "new_investment" not in st.session_state:
        st.session_state.new_investment = [] 
    ticker_list = get_ticker_list()
    selected_ticker = st.selectbox("Select Ticker", ticker_list)
    st.button("Add ticker",on_click= lambda: add_ticker(selected_ticker))
    if st.session_state.new_investment:
        st.write("New investment:")
        df=pd.DataFrame(st.session_state.new_investment,columns=["Ticker"])
        st.dataframe(df)
        strategy_list = get_strategy_list()
        selected_strategy = st.selectbox("Select Strategy", strategy_list)
        st.button("Add investment",on_click= lambda: add_new_investment(selected_strategy))

    
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
    # holdings_data = {
    #     'Symbol': ['AAPL', 'GOOGL', 'MSFT'],
    #     'Shares': [100, 50, 75],
    #     'Price': [150.20, 2500.50, 300.75],
    #     'Value': [15020.00, 125025.00, 22556.25]
    # }
    # holdings_df = pd.DataFrame(holdings_data)
    holdings_df = get_investments()
    st.write(holdings_df)

    # Display portfolio performance
    # st.subheader("Portfolio Performance")
    # st.line_chart(data=portfolio_performance())

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
menu_selection = st.sidebar.selectbox("Navigation", ["Portfolio", "Add Investment"])

if menu_selection == "Portfolio":
    if get_investments().empty:
        st.warning("No investments found. Add investments to view your portfolio.")
    portfolio()
elif menu_selection == "Add Investment":
    add_investment()
else:
    st.error("Invalid selection. Please select a valid option.")

