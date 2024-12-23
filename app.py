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

project_2_page = st.Page(
    page="views/project_2.py",
    title="Project 2",
    icon=":material/bar_chart:"
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page]
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("assets/logo.png")

st.sidebar.markdown("""
<p style='text-align: justify; padding: 1px;'>
Notes:
</p>
<ul style='text-align: justify; padding: 10px;'>       
<li>This section provides the summary of the projects I have completed. For comprehensive details and access to the source code, please visit the provided link below the project title.</li>
<li>In this section, I primarily utilized Plotly for data visualization to enhance interactivity. However, in the Jupyter Notebook 
source code, I opted for Matplotlib and Seaborn since GitHub does not directly render Plotly charts.</li>
</ul>

""", unsafe_allow_html=True)

# --- RUN NAVIGATION ---
pg.run()

