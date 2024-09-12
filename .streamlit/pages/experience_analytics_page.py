import streamlit as st
import pandas as pd

def app():
    st.title("Experience Analytics")

    # Load the dataset
    df = pd.read_csv(r'C:\Users\Beab\Desktop\Kifiya AIM\Investor-feasibility-analysis\.streamlit\data\engagement_experience_scores.csv')

    # Calculate Total Traffic (Bytes) as sum of 'Total UL (Bytes)' and 'Total DL (Bytes)'
    df['Total Traffic (Bytes)'] = df['Total UL (Bytes)'] + df['Total DL (Bytes)']

    # Define relevant columns including the newly calculated 'Total Traffic (Bytes)'
    relevant_columns = ['MSISDN/Number', 'Experience Score', 'Total Traffic (Bytes)']
    
    # Display the dataframe with the relevant columns
    st.dataframe(df[relevant_columns].head())

    # Display an area chart for Experience Score distribution
    st.subheader("Experience Score Distribution")
    st.area_chart(df['Experience Score'].sample(50))

    # Display a line chart for Experience vs Traffic
    st.subheader("Experience vs Traffic")
    st.line_chart(df[['Experience Score', 'Total Traffic (Bytes)']].sample(50))

    # Slicers for dynamic filtering
    experience_range = st.slider("Select Experience Score Range", min_value=float(df['Experience Score'].min()), max_value=float(df['Experience Score'].max()), value=(0.0, 100.0))
    filtered_data = df[(df['Experience Score'] >= experience_range[0]) & (df['Experience Score'] <= experience_range[1])]
    st.dataframe(filtered_data[relevant_columns].head())

    # Add a 'Back to Main' button to return to the main page
    if st.button('Back to Main'):
        st.session_state['current_page'] = 'Main'
