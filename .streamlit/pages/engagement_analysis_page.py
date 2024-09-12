import streamlit as st
import pandas as pd

def app():
    st.title("Engagement Analysis")

    # Load the dataset
    df = pd.read_csv(r'C:\Users\Beab\Desktop\Kifiya AIM\Investor-feasibility-analysis\.streamlit\data\engagement_experience_scores.csv')

    # Calculate Total Traffic (Bytes) as sum of 'Total UL (Bytes)' and 'Total DL (Bytes)'
    df['Total Traffic (Bytes)'] = df['Total UL (Bytes)'] + df['Total DL (Bytes)']

    # Define relevant columns including the newly calculated 'Total Traffic (Bytes)'
    relevant_columns = ['MSISDN/Number', 'Engagement Score', 'Total Traffic (Bytes)']
    
    # Display the dataframe with the relevant columns
    st.dataframe(df[relevant_columns].head())

    # Display a bar chart for Engagement Score distribution
    st.subheader("Engagement Score Distribution")
    st.bar_chart(df['Engagement Score'].sample(50))

    # Display a scatter chart for Traffic by Engagement Level
    st.subheader("Traffic by Engagement Level")
    st.scatter_chart(df[['Engagement Score', 'Total Traffic (Bytes)']].sample(50))

    # Slicers for dynamic filtering
    traffic_range = st.slider("Select Traffic Range", min_value=float(df['Total Traffic (Bytes)'].min()), max_value=float(df['Total Traffic (Bytes)'].max()), value=(0.0, 1000000.0))
    filtered_data = df[(df['Total Traffic (Bytes)'] >= traffic_range[0]) & (df['Total Traffic (Bytes)'] <= traffic_range[1])]
    st.dataframe(filtered_data[relevant_columns].head())

    # Add a 'Back to Main' button to return to the main page
    if st.button('Back to Main'):
        st.session_state['current_page'] = 'Main'
