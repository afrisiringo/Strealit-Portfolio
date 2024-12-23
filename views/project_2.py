import streamlit as st

# Data manipulation
import pandas as pd
import numpy as np

# Data viz
import seaborn as sns

# --- Title ---
st.title("E-commerce Strategy: Invest in App or Website for Max ROI?")


url = 'https://github.com/afrisiringo/Website-vs-App/blob/main/analysis.ipynb'

st.markdown(f"<i>To access the full project details and source code, please click this <a href='{url}'>link</a>.</i>", unsafe_allow_html=True)

st.markdown("---")

# --- BACKGROUND ---

st.markdown("""
### Background
<p style='text-align: justify; padding: 1px;'>
X is an Ecommerce company that sells clothing online but they also have in-store style and clothing advice sessions. Customers come in to the store, have sessions/meetings with a personal stylist, 
then they can go home and order either on a mobile app or website for the clothes they want.
<br><br>
The company is trying to decide whether to focus their efforts on their mobile app experience or their website.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# --- DATASET ---

st.markdown("""
### Dataset
<p style='text-align: justify; padding: 1px;'>
The data used is information about E-commerce X's customer accounts.
</p>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv('./assets/Ecommerce Customers')

customers = load_data()

# Menampilkan DataFrame di Streamlit
st.dataframe(customers)

st.markdown("---")

st.markdown("""
### Relationships between the numerical features
<p style='text-align: justify; padding: 1px;'>
The interrelationships among numerical variables were examined by utilizing Seaborn's pairplot function.
</p>
""", unsafe_allow_html=True)

pairplot = sns.pairplot(customers)
st.pyplot(pairplot.fig)

st.markdown("""
<p style='text-align: justify; padding: 1px;'>
From this visual we can see several points of analysis:
</p>
<ul style='text-align: justify; padding: 10px;'>       
<li>There is a positive correlation between <b>Time on App</b> and <b>Yearly Amount Spent</b>, indicating that the more time customers spend in the app, the more they spend. This could be a reason to improve 
the user experience in the app.</li>
<li>The relationship between <b>Time on Website</b> and <b>Yearly Amount Spent</b> appears weaker. This could indicate that websites may not be as effective as apps in driving sales, or that there is room 
for improvement on websites.</li>
<li>There is a strong linear relationship between <b>Length of Membership</b> and <b>Yearly Amount Spent</b>. This shows that the longer a customer is a member, the more money they spend each year. This 
emphasizes the importance of retaining existing customers.</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("""
### Regression analysis
<p style='text-align: justify; padding: 1px;'>
To reinforce these findings and provide more targeted recommendations, regression analysis was conducted. A linear regression model was developed to predict <b>Yearly Amount Spent</b>. Subsequently, 
the coefficients of the model was analyzed to identify which features most significantly influence changes in <b>Yearly Amount Spent</b>.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: justify; padding: 1px;'>
After building the model, an evaluation was conducted to assess its performance. The results are as follows:
</p>
<ul style='text-align: justify; padding: 10px;'>       
<li>Mean Absolute Error (MAE): 7.22</li>
<li>Root Mean Square Error (RMSE): 8.93</li>
<li>Mean Absolute Percentage Error (MAPE): 1.45%</li>
<li>R-squared (R2): 98.90%</li>
</ul>
<p style='text-align: justify; padding: 1px;'>
The model has low error metrics and high R2, this indicates that the model is very effective in predicting annual spending based on the features provided.
</p>
<p style='text-align: justify; padding: 1px;'>
The following is a comparison of the coefficients of the features model:
</p>
""", unsafe_allow_html=True)

# Create a DataFrame with the coefficients
data = {
    "Coefficient": [25.981550, 38.590159, 0.190405, 61.279097]
}
index = ["Avg. Session Length", "Time on App", "Time on Website", "Length of Membership"]
df = pd.DataFrame(data, index=index)

# Display the DataFrame in Streamlit
st.dataframe(df)

st.markdown("""
<p style='text-align: justify; padding: 1px;'>
The interpretation of this value is as follows:
</p>    
<ul style='text-align: justify; padding: 10px;'>       
<li>Every one unit increase in Time on App correlates to an increase of approximately 38.59 units in annual spending, demonstrating the significant impact of apps on sales.</li>
<li>The coefficient for Time on Website is only 0.19, indicating that time spent on the website does not significantly affect customers' annual spending compared to other factors in the model.</li>
<li>Each one-year increase in membership correlates with an increase of approximately 61.27 units in annual spending, confirming the importance of customer loyalty.</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("""
### Conclusion
<p style='text-align: justify; padding: 1px;'>
The data shows that apps have a greater impact on annual spending growth than websites. This could be a strong argument for further development focus on the mobile app experience. Meanwhile, 
the importance of membership length in increasing spending suggests the need for strategies aimed at increasing customer retention.
</p>
""", unsafe_allow_html=True)