import streamlit as st
from services.persistence.exercise_repositry import get_or_create_user


def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
    
    st.title("🏋️‍♀️AI Real-time Gym Coach")
    st.markdown("Welcome! Please enter username to start")

    with st.form("Login Form"):
        username=st.text_input("Username",placeholder="Enter your username")
        # submit_button = st.form_submit_button("Start Session",width="stretch")
        st.markdown('<div class="login-page">', unsafe_allow_html=True)

        submit_button=st.form_submit_button("Start Session",width="stretch")

        st.markdown('</div>', unsafe_allow_html=True)

    

    if submit_button:
        if not username:
            st.error("Username cannot be empty")
            return False
        user=get_or_create_user(username)
        
        st.session_state["user_id"]=user["id"]
        st.session_state["username"]=user["username"]

        st.rerun()
    
    return False
