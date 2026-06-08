import time
import streamlit as st
from src.database.config import supabase
from src.database.db import enroll_students_to_subjects



@st.dialog('Quick Enrollment')
def auto_enroll_dialog(subject_code):
    student_id = st.session_state.student_data['student_id']

    res = supabase.table('subjects').select('subject_id, name').eq('subject_code', subject_code).execute()
    if not res.data:
        st.error('Subject code not found!')
        if st.button('Close'):
            st.query_params.clear()
            st.rerun()
        return
    
    subject = res.data[0]

    check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
    if check.data:
        st.info('Youre already enrolled!')
        if st.button('Got it!'):
            st.query_params.clear()
            st.rerun()
        return

    st.markdown(f"Would you like to enroll in **{subject['name']}**?")

    col1, col2 = st.columns(2)

    with col1:
        st.info('Youre already enrolled!')
        if st.button('Got it!'):
            st.query_params.clear()
            st.rerun()

    with col2:
        st.button('Yes enroll now!', type='primary', width='stretch')
        enroll_students_to_subjects(student_id, subject['subject_id'])
        st.success('Joined succesfully!')
        st.query_params.clear()
        time.sleep(1)
        st.rerun()

