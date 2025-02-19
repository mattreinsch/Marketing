import streamlit as st
from st_paywall import add_auth
import stripe
from stripe.error import APIConnectionError

st.set_page_config(layout="wide")
st.title("My Cool SaaS! 🚀")

try:
    add_auth(required=True)
    # ONLY AFTER THE AUTHENTICATION + SUBSCRIPTION, THE USER WILL SEE THIS ⤵
    # The email and subscription status is stored in session state.
    st.write(f"Subscription Status: {st.session_state.user_subscribed}")
    st.write("🎉 Yay! You're all set and subscribed! 🎉")
    st.write(f'By the way, your email is: {st.session_state.email}')
except APIConnectionError as e:
    st.error(f"Connection error: {e}")
    st.write("Please check your network settings and try again.")
