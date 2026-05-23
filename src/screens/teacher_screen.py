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


    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        teacher_header()

    with c2:
        st.subheader(f"""Welcome {teacher_data['name']}""", text_alignment='center')
        if st.button('Logout', key='loginbackbtn', shortcut='control+backspace', width='stretch'):
            st.session_state['is_logged_in'] = False
            del st.session_state.teacher_data
            del st.session_state.current_teacher_tab
            st.rerun()
    
    st.space()

    if 'current_teacher_tab' not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'

    tab1, tab2, tab3 = st.columns(3)

    with tab1:
        type1 = 'primary' if st.session_state.current_teacher_tab == 'take_attendance' else 'tertiary'
        if st.button('Take Attendance', width='stretch', icon=':material/ar_on_you:', type=type1):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()

    with tab2:
        type2 = 'primary' if st.session_state.current_teacher_tab == 'manage_subjects' else 'tertiary'
        if st.button('Manage Subjects', width='stretch', icon=':material/book_ribbon:', type=type2):
            st.session_state.current_teacher_tab = 'manage_subjects'
            st.rerun()

    with tab3:
        type3 = 'primary' if st.session_state.current_teacher_tab == 'attendance_records' else 'tertiary'
        if st.button('Attendance Records', width='stretch', icon=':material/cards_stack:', type=type3):
            st.session_state.current_teacher_tab = 'attendance_records'
            st.rerun()

    st.divider()

    if st.session_state.current_teacher_tab == 'take_attendance':
        teacher_tab_take_attendance()
    if st.session_state.current_teacher_tab == 'manage_subjects':
        teacher_tab_manage_sunjects()
    if st.session_state.current_teacher_tab == 'attendance_records':
        teacher_tab_attendance_records()


    
def teacher_tab_take_attendance():
    st.header('Take AI Attendance')


def teacher_tab_manage_sunjects():
    teacher_id = st.session_state.teacher_data['teacher_id']
    col1, col2 = st.columns(2)
    with col1:
        st.header('Manage Subjects')
    with col2:
        if st.button('Create New Subjects', width='stretch'):
            create_subject_dialog(teacher_id)



def teacher_tab_attendance_records():
    st.header('Attendance Records')




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
        if st.button('Go back to Home', key='loginbackbtn_ts', shortcut='control+backspace'):
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
                # teacher_dashboard()
                st.rerun()
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
        if  st.button('Go back to Home', key='loginbackbtn_reg', shortcut='control+backspace'):
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


    