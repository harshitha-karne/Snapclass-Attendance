import streamlit as st

def teacher_screen():
    st.header('Teacher Screen')

    if st.button('back'):
        st.session_state['login_type']=None
        st.rerun()