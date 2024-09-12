import streamlit as st
import pandas as pd

def app():
    st.title("Overview Analysis")
    
    # Load the dataset
    df = pd.read_csv(r'C:\Users\Beab\Desktop\Kifiya AIM\Investor-feasibility-analysis\.streamlit\data\engagement_experience_scores.csv')
    df['Total Traffic (Bytes)'] = df['Total UL (Bytes)'] + df['Total DL (Bytes)']
    
    relevant_columns = ['MSISDN/Number', 'Engagement Score', 'Experience Score', 'Total Traffic (Bytes)']
    st.dataframe(df[relevant_columns].head())
    
    st.subheader("Engagement vs Experience")
    st.line_chart(df[['Engagement Score', 'Experience Score']].sample(50))

    st.subheader("Total Traffic Distribution")
    st.bar_chart(df['Total Traffic (Bytes)'].sample(50))

    # Add slicers for interactivity
    engagement_range = st.slider("Select Engagement Score Range", min_value=float(df['Engagement Score'].min()), max_value=float(df['Engagement Score'].max()), value=(0.0, 100.0))
    filtered_data = df[(df['Engagement Score'] >= engagement_range[0]) & (df['Engagement Score'] <= engagement_range[1])]
    st.dataframe(filtered_data[relevant_columns].head())
    # Add a 'Back to Main' button to return to the main page
   