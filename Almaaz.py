import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth # pip install streamlit-authenticator

st.set_page_config(
    page_title="Welcome Page",
    page_icon="👋",
    layout="wide",

)

st.write("# Welcome to Almaaz Finance 👋")
st.header("The platform for all your investment needs! 📈")
st.divider()
st.subheader("Revolutionizing Trading Through Advanced Algorithms")
st.write("**Almaaz is a platform that provides you with the a wide range of innovative investment strategies and helps you keep track of your investments.**")
st.subheader("Empowering Users with Advanced Tools and Unmatched Performance")
st.write("**Our platform is beginner friendly and designed to help you make the most of your investments: No experience or effort needed.**")
st.divider()

names = ["Sarra Jerbi", "Amine Zouaoui", "Yassine Bouassida"]
usernames = ["sarra", "amine", "yassine"]
passwords = ["123", "456", "789"]

hashed_passwords = stauth.Hasher(passwords).generate()

 

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)
name, authentication_status, username = authenticator.login("Get started by logging in","main")


if authentication_status==False:
    # st.write("### New to Almaaz? ***Sign up to get started***")
    st.sidebar.title("Welcome Page")
    st.error("Invalid user name or password")
    st.sidebar.error("Please log in to continue")
    

if authentication_status==None:
#    st.write("### New to Almaaz? ***Sign up to get started***")
   st.sidebar.title("Welcome Page")
   st.warning("Please enter your user name and password to continue")
   st.sidebar.error("Please log in to continue")
   
if authentication_status:
    st.sidebar.title(f"Welcome {name} 👋")
    st.sidebar.success("You are now logged in")
    authenticator.logout("Logout", "sidebar")


# st.write("### New to Almaaz? ***Sign up to get started***")

# if st.button("Sign up here"):
#     st.subheader("Sign Up")
#     new_username = st.text_input("Username")
#     new_name = st.text_input("Name")
#     new_password = st.text_input("Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")

#     if new_username and new_name and new_password and confirm_password:
#         if new_password == confirm_password:
#             # Add code to check if username already exists
#             if new_username not in usernames:
#                 # Add code to hash the password securely
#                 # For example:
#                 # hashed_password = hash_function(new_password)
#                 st.success("Sign up successful! You can now log in.")
#             else:
#                 st.error("Username already exists. Please choose a different username.")
#         else:
#             st.error("Passwords do not match. Please try again.")
#     else:
#         st.warning("Please fill in all the fields.")