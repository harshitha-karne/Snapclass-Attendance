import streamlit as st

def student_screen():
    st.header('student Screen')

    if st.button('back'):
        st.session_state['login_type']=None
        st.rerun()