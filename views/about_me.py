import streamlit as st

# --- HERO SECTION ---
col1, col2 = st.columns([1.6, 3], gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/pp1.png", width=260)
with col2:
    st.title("Afridoyo Siringo-ringo", anchor=False)
    st.write(
        "Data Analyst, assisting enterprises by supporting data-driven decision-making.",
        unsafe_allow_html=True
    )
    col2_1, col2_2, col2_3 = st.columns(3)
    with col2_1:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/afridoyosiringoringo/)", unsafe_allow_html=True)
    with col2_2:
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/afrisiringo)", unsafe_allow_html=True)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 1 Year experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Technical Skills", anchor=False)
st.write(
    """
    - SQL (MySQL, Microsoft SQL Server)
    - Python (NumPy, Pandas, Matplotlib, DuckDB, Scikit-Learn, Statsmodels)
    - Databases: MySQL, SQL Server
    - Microsoft Excel
    - BigQuery
    - Tableau
    - Microsoft Power BI
    """
)