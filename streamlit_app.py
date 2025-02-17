import streamlit as st
import page1_name
import page2_name

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Main Page", "Page 1", "Page 2"])

if page == "Main Page":
    st.title("PCOS Predictor")
    st.header("burp")
    st.write(
        "Here is some information about our app."
    )
elif page == "Page 1":
    page1_name.display_page()
elif page == "Page 2":
    page2_name.display_page()