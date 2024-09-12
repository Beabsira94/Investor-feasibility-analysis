import streamlit as st
from multiapp import MultiApp
from pages import overview_page, engagement_analysis_page, experience_analytics_page
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

# Load the dataset
df = pd.read_csv(r'C:\Users\Beab\Desktop\Kifiya AIM\Investor-feasibility-analysis\.streamlit\data\engagement_experience_scores.csv')

# Calculate Total Traffic (Bytes) as sum of 'Total UL (Bytes)' and 'Total DL (Bytes)'
df['Total Traffic (Bytes)'] = df['Total UL (Bytes)'] + df['Total DL (Bytes)']

# Create the app instance
app = MultiApp()

# Add color styles for buttons and text
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50; 
        color: white;
        font-size: 16px;
        margin: 10px 0;
    }
    .stSidebar .css-1d391kg {
        background-color: #F4F4F4;
        border-radius: 5px;
    }
    .stSidebar .css-1d391kg .css-18e3th9 {
        background-color: #2C3E50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main app page with descriptions only
def main():
    st.title('Main Dashboard')
    st.write("Welcome to the Interactive Dashboard!")
    
    st.markdown("""
        - **Overview Analysis**: Provides general insights about user metrics.
        - **Engagement Analysis**: Explores user engagement patterns in detail.
        - **Experience Analytics**: Analyzes user experience across various metrics.
    """)
    
    st.write("Use the navigation panel on the left to switch between sections.")

# Registering the pages
app.add_app("Main", main)
app.add_app("Overview Analysis", overview_page.app)
app.add_app("Engagement Analysis", engagement_analysis_page.app)
app.add_app("Experience Analytics", experience_analytics_page.app)

# Running the app
app.run()
