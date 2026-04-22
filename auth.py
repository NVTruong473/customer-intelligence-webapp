import streamlit as st
import pandas as pd
import re
from datetime import datetime
from utils import load_users, save_users, username_exists, reset_users


def valid_text(x):
    return re.match(r"^[A-Za-z0-9@._-]+$", str(x).strip())


def auth_page():

    st.markdown("""
    <div class='title-box'>
        <h2>Secure Account Center</h2>
        <p>Login / Register / Password Recovery</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Login", "Register", "Change Password", "Forgot Password"]
    )

    # --------------------------------
    # LOGIN
    # --------------------------------
    with tab1:

        st.subheader("Login")

        username = st.text_input("Username", key="login_user")
        password = st.text_input(
            "Password",
            type="password",
            key="login_pass"
        )

        if st.button("Login Now"):

            username = username.strip()
            password = password.strip()

            df = load_users()

            if username == "" or password == "":
                st.error("Username and password cannot be empty.")

            elif username not in df["username"].values:
                st.error("Username does not exist.")

            else:
                row = df[df["username"] == username].iloc[0]

                if int(row["locked"]) == 1:
                    st.error("Account is locked.")

                elif str(row["status"]).lower() != "active":
                    st.error("Account inactive.")

                elif str(row["password"]) != password:
                    st.error("Wrong password.")

                else:
                    st.session_state.login = True
                    st.session_state.user = username
                    st.success("Login success.")
                    st.rerun()

    # --------------------------------
    # REGISTER
    # --------------------------------
    with tab2:

        st.subheader("Register")

        username = st.text_input("New Username", key="reg_user")
        password = st.text_input(
            "New Password",
            type="password",
            key="reg_pass"
        )

        confirm = st.text_input(
            "Confirm Password",
            type="password",
            key="reg_confirm"
        )

        if st.button("Create Account"):

            username = username.strip()
            password = password.strip()
            confirm = confirm.strip()

            if username == "" or password == "":
                st.error("Cannot be empty.")

            elif username_exists(username):
                st.error("Username already exists.")

            elif not valid_text(username):
                st.error("Invalid username format.")

            elif len(password) < 6:
                st.error("Password must be at least 6 characters.")

            elif password != confirm:
                st.error("Password confirm mismatch.")

            else:
                df = load_users()

                new_row = pd.DataFrame([{
                    "username": username,
                    "password": password,
                    "old_password": "",
                    "role": "user",
                    "status": "active",
                    "failed_login_count": 0,
                    "locked": 0,
                    "created_at": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                }])

                df = pd.concat([df, new_row], ignore_index=True)
                save_users(df)

                st.success("Account created successfully.")

    # --------------------------------
    # CHANGE PASSWORD
    # --------------------------------
    with tab3:

        st.subheader("Change Password")

        username = st.text_input("Username", key="chg_user")

        current_pass = st.text_input(
            "Current Password",
            type="password",
            key="chg_current"
        )

        new_pass = st.text_input(
            "New Password",
            type="password",
            key="chg_new"
        )

        confirm = st.text_input(
            "Confirm New Password",
            type="password",
            key="chg_cf"
        )

        if st.button("Change Now"):

            username = username.strip()

            df = load_users()

            if username not in df["username"].values:
                st.error("Username not found.")

            else:
                idx = df[df["username"] == username].index[0]

                real_current = str(df.loc[idx, "password"])
                old_pass = str(df.loc[idx, "old_password"])

                if current_pass != real_current:
                    st.error("Current password incorrect.")

                elif new_pass == "":
                    st.error("New password cannot be empty.")

                elif len(new_pass) < 6:
                    st.error("New password too short.")

                elif new_pass == real_current:
                    st.error(
                        "New password cannot equal current password."
                    )

                elif new_pass == old_pass:
                    st.error(
                        "New password cannot equal previous password."
                    )

                elif new_pass != confirm:
                    st.error("Confirm mismatch.")

                else:
                    df.loc[idx, "old_password"] = real_current
                    df.loc[idx, "password"] = new_pass

                    save_users(df)

                    st.success("Password updated successfully.")

    # --------------------------------
    # FORGOT PASSWORD
    # --------------------------------
    with tab4:

        st.subheader("Forgot Password")

        username = st.text_input("Username", key="fg_user")

        old_known = st.text_input(
            "Previous Password",
            type="password",
            key="fg_old"
        )

        new_pass = st.text_input(
            "New Password",
            type="password",
            key="fg_new"
        )

        if st.button("Recover Password"):

            username = username.strip()

            df = load_users()

            if username not in df["username"].values:
                st.error("Username not found.")

            else:
                idx = df[df["username"] == username].index[0]

                old_real = str(df.loc[idx, "old_password"])
                current_real = str(df.loc[idx, "password"])

                if old_real == "":
                    st.error(
                        "No previous password found. "
                        "Please use Change Password first."
                    )

                elif old_known != old_real:
                    st.error("Previous password incorrect.")

                elif new_pass == "":
                    st.error("New password cannot be empty.")

                elif len(new_pass) < 6:
                    st.error("New password too short.")

                elif new_pass == current_real:
                    st.error(
                        "New password cannot equal current password."
                    )

                elif new_pass == old_real:
                    st.error(
                        "New password cannot equal previous password."
                    )

                else:
                    df.loc[idx, "password"] = new_pass
                    save_users(df)

                    st.success("Password recovered successfully.")

    # --------------------------------
    # RESET TEST DATA
    # --------------------------------
    st.divider()

    c1, c2, c3 = st.columns([6, 2, 2])

    with c3:
        if st.button("Reset Test Accounts"):
            reset_users()
            st.success("Test data reset completed.")
            st.rerun()
