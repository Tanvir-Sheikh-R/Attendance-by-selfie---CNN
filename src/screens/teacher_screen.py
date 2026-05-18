import streamlit as st
from src.components.header import teacher_header
from src.ui.base_layout import style_base_layout, style_background_dashboard
from src.screens.home_screen import home_screen


def teacher_screen():


    style_base_layout()
    style_background_dashboard()

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        teacher_header()

    with c2:
        st.button('Go back to Home', key='loginbackbtn', shortcut='control+backspace')


    st.header('Register your teacher profile')