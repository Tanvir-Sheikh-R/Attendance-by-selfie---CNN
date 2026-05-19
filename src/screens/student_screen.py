import numpy as np
from PIL import Image
import streamlit as st
from src.components.header import teacher_header
from src.components.footer import footer_dashboard
from src.ui.base_layout import style_base_layout, style_background_dashboard



def student_screen():


    style_base_layout()
    style_background_dashboard()
    

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        teacher_header()

    with c2:
        if st.button('Go back to Home', key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_state'] = None
            st.rerun()
    

    st.header('Login using FaceID', text_alignment='center')

    st.space()
    st.divider()
    st.space()

    photo_source = st.camera_input('Position your face in the center')
    if photo_source:
        np.array(Image(photo_source))
        
    footer_dashboard()