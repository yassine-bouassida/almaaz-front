import streamlit as st
import pandas as pd

# Function to load local CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Define function for the profile page
def profile():
    st.title("👤 My Profile")

    # Dummy user profile data
    user_profile_data = {
        'Name': 'John Doe',
        'Age': 30,
        'Email': 'john.doe@example.com',
        'Address': '123 Main St, City, Country',
        'Phone': '+1234567890'
    }

    # Display user profile information
    st.subheader("User Profile")
    st.write(f"Name: {user_profile_data['Name']}")
    st.write(f"Age: {user_profile_data['Age']}")
    st.write(f"Email: {user_profile_data['Email']}")
    st.write(f"Address: {user_profile_data['Address']}")
    st.write(f"Phone: {user_profile_data['Phone']}")

    # You can add more sections for additional user profile information if needed

# Define function for the investments page
def investments():
    st.title("📈 My Investments")

    # Dummy investment data (replace this with actual data)
    investment_data = {
        'Symbol': ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB'],
        'Name': ['Apple Inc.', 'Alphabet Inc.', 'Microsoft Corporation', 'Amazon.com Inc.', 'Meta Platforms Inc.'],
        'Shares': [10, 5, 15, 8, 12],
        'Average Price': [150.20, 2300.50, 300.75, 3500.00, 320.00],
        'Current Price': [160.50, 2400.00, 310.25, 3600.00, 330.00],
        'Value': [1605.00, 12000.00, 4653.75, 28800.00, 3960.00],
        'Profit/Loss': [450.00, -250.00, 103.75, -1600.00, 120.00]
    }

    # Create DataFrame from investment data
    df_investments = pd.DataFrame(investment_data)

    # Display investment data as a table
    st.dataframe(df_investments.style.format({
        'Average Price': '${:,.2f}',
        'Current Price': '${:,.2f}',
        'Value': '${:,.2f}',
        'Profit/Loss': '${:,.2f}'
    }), height=500)

# Set page configuration
st.set_page_config(
    page_icon="👤",
    layout="wide"
)

# Load local CSS file
local_css("Style.css")

# Main content of the app
menu_selection = st.sidebar.selectbox("Navigation", ["Profile", "My Investments"])
#menu_selection = "Profile"

if menu_selection == "Profile":
    profile()
elif menu_selection == "My Investments":
    investments()
