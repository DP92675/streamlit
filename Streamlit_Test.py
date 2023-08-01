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

# Creating a Plotly figure with a vertical bar graph for "Visits"
fig = px.bar(filtered_data, x='Month', y='Visits', text='Visits', labels={'Visits': 'Visits'})

# Updating the bar width to 3 times the default size
fig.update_traces(width=3 * 86400000)  # 1 day in milliseconds

# Adding a line plot for "Visits (y/y)" with a dotted orange line
line_trace = go.Scatter(x=filtered_data['Month'], y=filtered_data['Visits (y/y)'] * 100, mode='lines', line=dict(dash='dot', color='orange'))
fig.add_trace(line_trace)

# Updating the y-axis to show percentages for "Visits (y/y)"
fig.update_layout(
    yaxis2=dict(
        title='Visits (y/y) (%)',
        overlaying='y',
        side='right',
        tickformat='%'
    )
)

# Displaying the plot in the Streamlit app
st.plotly_chart(fig)
