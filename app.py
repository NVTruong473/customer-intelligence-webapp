import streamlit as st
from config import PAGE_TITLE, LOGO_PATH
from styles import load_css
from auth import auth_page
from ui import dashboard


# --------------------------------
# PAGE CONFIG
# --------------------------------
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=LOGO_PATH,
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------
# LOAD STYLE
# --------------------------------
load_css()


# --------------------------------
# SESSION STATE INIT
# --------------------------------
default_session = {
    "login": False,
    "user": "",
}

for key, value in default_session.items():
    if key not in st.session_state:
        st.session_state[key] = value


# --------------------------------
# APP ROUTER
# --------------------------------
if st.session_state.login:
    dashboard()
else:
    auth_page()
