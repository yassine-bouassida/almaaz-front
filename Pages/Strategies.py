import streamlit as st

# Define function for the strategies page
def strategies():
    st.title("📊 Strategies")
    st.write("Welcome to Almaaz's Strategies page! Here you can explore different investment strategies.")
    st.write("Below are some popular investment strategies provided by Almaaz:")

    # List of strategies
    strategies_list = [
        ("Buy and Hold", "Long-term investment strategy where investors hold onto securities for an extended period."),
        ("Value Investing", "Strategy where investors look for undervalued stocks trading at a price below their intrinsic value."),
        ("Growth Investing", "Focuses on stocks with strong potential for future growth, often characterized by high earnings or revenue growth rates."),
        ("Dividend Investing", "Investing in stocks that pay regular dividends, providing a steady income stream for investors."),
        ("Momentum Investing", "Based on the idea that assets that have performed well in the past will continue to perform well in the future."),
        ("Contrarian Investing", "Contrarian investors go against prevailing market trends, buying when others are selling and selling when others are buying."),
        ("Index Investing", "Investing in a portfolio of stocks designed to match the performance of a particular market index, such as the S&P 500."),
        ("Technical Analysis", "Analysis of past market data, primarily price and volume, to forecast future price movements."),
        ("Fundamental Analysis", "Evaluation of a company's financial health and performance to determine its intrinsic value and potential for growth.")
    ]

    # Display strategies in a formatted list
    for strategy, description in strategies_list:
        st.markdown(f"### {strategy}")
        st.write(description)
        st.markdown("---")

# Call the strategies function to display the page
strategies()
