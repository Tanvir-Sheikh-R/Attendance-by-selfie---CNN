import streamlit as st


def footer_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style = " margin-top: 2rem; display: flex; justify-content: center; items-align: center " >
            <p style = 'font-weight: bold; color:white;' > Created by Tanvir </p>
        </div>
        """, unsafe_allow_html=True)