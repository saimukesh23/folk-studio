import streamlit as st
from core.auth import register_user, login_user

def show_login_page(translations):
    st.title(translations["app_title"])

    menu = [translations["login"], translations["register"]]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == translations["login"]:
        st.subheader(translations["login"])

        username = st.text_input(translations["username"])
        password = st.text_input(translations["password"], type="password")

        if st.button(translations["login"]):
            user = login_user(username, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.username = user[1]
                st.session_state.native_place = user[3]
                st.experimental_rerun()
            else:
                st.error("Incorrect username or password")

    elif choice == translations["register"]:
        st.subheader(translations["register"])

        new_username = st.text_input(translations["username"])
        new_password = st.text_input(translations["password"], type="password")
        native_place = st.text_input(translations["native_place"])

        if st.button(translations["register"]):
            if register_user(new_username, new_password, native_place):
                st.success("You have successfully registered. Please login.")
            else:
                st.error("Username already exists")
