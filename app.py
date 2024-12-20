import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True
)

project_1_page = st.Page(
    page="views/project_1.py",
    title="Project 1",
    icon=":material/bar_chart:"
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page]
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("assets/logo.png")
# --- RUN NAVIGATION ---
pg.run()

