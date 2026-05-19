import streamlit as st
from src.components.header import teacher_header
from src.components.footer import footer_dashboard
from src.ui.base_layout import style_base_layout, style_background_dashboard
from src.screens.home_screen import home_screen


def teacher_screen():

    style_base_layout()
    style_background_dashboard()

    
    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == 'login':
        teacher_screen_login()

    elif st.session_state.teacher_login_type == 'register':
        teacher_screen_register()

    footer_dashboard()




def teacher_screen_login():

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        teacher_header()

    with c2:
        if st.button('Go back to Home', key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_state'] = None
            st.rerun()
    

    st.header('Login into teacher profile')
    st.space()
    st.space()

    username_input  = st.text_input('Enter Username', placeholder='@Username')
    pass_input      = st.text_input('Enter Password', placeholder='Password', type='password')
    st.divider()

    btn1, btn2 = st.columns(2)

    with btn1:
        st.button("login", width='stretch', icon=':material/passkey:', shortcut='enter', key='login')

    with btn2:
        if st.button("Register", type='primary', width='stretch', icon=':material/passkey:', key='register'):
            st.session_state.teacher_login_type = 'register'
            st.rerun()

    
    
 
def teacher_screen_register():

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        teacher_header()
    with c2:
        if st.button('Go back to Home', key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_state'] = None
            st.rerun()
    
    st.header('Register into teacher profile')
    st.space()
    st.space()

    username_input      = st.text_input('Enter Username', placeholder='@Username')
    name_input          = st.text_input('Enter Name', placeholder='Display Name')
    pass_input          = st.text_input('Enter Password', placeholder='Password', type='password')
    conform_pass_input  = st.text_input('Conform Password', placeholder='Conform Password', type='password')
    
    st.divider()

    btn1, btn2 = st.columns(2)
    with btn1:
        st.button("Register", type='primary', width='stretch', icon=':material/passkey:', key='register', shortcut='enter')
    with btn2:
        if st.button("login", width='stretch', icon=':material/passkey:', key='login'):
            st.session_state.teacher_login_type = 'login'
            st.rerun()


    