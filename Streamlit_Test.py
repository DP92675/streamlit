import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Title of the Streamlit app
st.title('Visits Analysis')

# Reading the data from the uploaded Excel file
file_path = 'Streamlit_Test.xlsx'
data = pd.read_excel(file_path)

# Converting the "Month" column to a datetime object
data['Month'] = pd.to_datetime(data['Month'])

# Adding a slider to select the date range using index values
start_index, end_index = st.slider('Select a date range:', min_value=0, max_value=len(data) - 1, value=(0, len(data) - 1))

# Filtering the data based on the selected date range
filtered_data = data.iloc[start_index:end_index + 1]

# Create a figure with subplots
fig = go.Figure()

# Add a bar trace for "Visits" with a width of 5 days
fig.add_trace(go.Bar(x=filtered_data['Month'], y=filtered_data['Visits'], name='Visits', width=20 * 86400000, marker_color='#0F1B93'))  # 20 days in milliseconds

# Add a scatter trace for "Visits (y/y)" on a secondary y-axis, presented in percentages
fig.add_trace(go.Scatter(x=filtered_data['Month'], y=filtered_data['Visits (y/y)'], name='Visits (y/y)', line=dict(dash='dot', color='#E67E22', width=3), yaxis='y2'))

# Update layout to include a secondary y-axis for percentages, rounded to 1 decimal, and remove grid lines
fig.update_layout(
    yaxis=dict(title='Visits'),
    yaxis2=dict(title='Visits (y/y) (%)', overlaying='y', side='right', tickformat='.1%', showgrid=False),  # Remove grid lines
    xaxis=dict(title='Month'),
    barmode='overlay',
    template='plotly_white'
)

# Displaying the plot in the Streamlit app
st.plotly_chart(fig)
