import time
import streamlit as st
from src.components.header import teacher_header
from src.components.footer import footer_dashboard
from src.ui.base_layout import style_base_layout, style_background_dashboard
from src.screens.home_screen import home_screen
from src.database.db import check_teacher_exists, create_teacher, teacher_login


def teacher_screen():

    style_base_layout()
    style_background_dashboard()

    if 'teacher_data' in st.session_state:
        teacher_dashboard()

    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == 'login':
        teacher_screen_login()

    elif st.session_state.teacher_login_type == 'register':
        teacher_screen_register()

    footer_dashboard()




def teacher_dashboard():
    teacher_data = st.session_state.teacher_data

    st.header(f"""Welcome {teacher_data['name']}""")



def check_registration_from(username_input, pass_input, name_input, conform_pass_input):

    if not username_input or not name_input or not pass_input or not conform_pass_input:
        return False, 'All fields are required'
    
    if pass_input != conform_pass_input:
        return False, "Password dosen't match"
    
    if check_teacher_exists(username_input):
        return False, 'Teacher already exists'
    
    try:
        create_teacher(username_input, pass_input, name_input)
        return True, 'Sucessfully Created! Login Now'

    except Exception as e:
        return False, 'Unexpected Error!'
    



def check_login_from(username_input, pass_input):
        
    if not username_input or not pass_input :
        return False

    teacher = teacher_login(username_input, pass_input)    
    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    
    return False


    


    
    


def teacher_screen_login():

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        teacher_header()

    with c2:
        if st.button('Go back to Home', key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_state'] = None
            st.rerun()
    

    st.header('Login into teacher profile', text_alignment='center')
    st.space()
    st.space()

    username_input  = st.text_input('Enter Username', placeholder='@Username')
    pass_input      = st.text_input('Enter Password', placeholder='Password', type='password')

    st.divider()

    btn1, btn2 = st.columns(2)
    with btn1:
        if st.button("login Now", width='stretch', icon=':material/passkey:', shortcut='enter', key='login'):
            success = check_login_from(username_input, pass_input)
            if success:
                st.toast('Welcome back', icon='👋')
                time.sleep(1)
            else:
                st.error('Invalid username or password')

    with btn2:
        if  st.button("Register Instead", type='primary', width='stretch', icon=':material/passkey:', key='register'):
            st.session_state.teacher_login_type = 'register'
            st.rerun()

    
    
# In teacher screen Registration From submission

def teacher_screen_register():

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        teacher_header()
    with c2:
        if  st.button('Go back to Home', key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_state'] = None
            st.rerun()
    
    st.header('Register into teacher profile', text_alignment='center')
    st.space()
    st.space()

    username_input      = st.text_input('Enter Username', placeholder='@Username')
    name_input          = st.text_input('Enter Name', placeholder='Display Name')
    pass_input          = st.text_input('Enter Password', placeholder='Password', type='password')
    conform_pass_input  = st.text_input('Conform Password', placeholder='Conform Password', type='password')
    
    st.divider()

    btn1, btn2 = st.columns(2)
    with btn1:
        if st.button("Register Now", type='primary', width='stretch', icon=':material/passkey:', key='register', shortcut='enter'):
            success, message = check_registration_from(username_input, pass_input, name_input, conform_pass_input)
            if success:
                st.success(message)
                time.sleep(2)
                st.session_state.teacher_login_type = 'login'
                st.rerun()
            else:
                st.error(message)

    with btn2:
        if  st.button("login Instead", width='stretch', icon=':material/passkey:', key='login'):
            st.session_state.teacher_login_type = 'login'
            st.rerun()


    