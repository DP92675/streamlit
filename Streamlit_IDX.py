import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Title of the Streamlit app
st.title('Indonesian Stock Brokerage Benchmarking')

# Reading the data from the uploaded Excel file
file_path = 'IDX_Scrape_Streamlit.xlsx'
data = pd.read_excel(file_path)

# Converting the "Date" column to a datetime object
data['Date'] = pd.to_datetime(data['Date'])

# Dropdown to select the Ticker
selected_ticker = st.selectbox('Select Brokerage:', options=data['FirmName'].unique())

# Dropdown to select the Ticker and Metric
col1, col2 = st.columns(2)  # Create two columns to avoid cluttering

# Place the dropdowns in separate columns
selected_ticker = col1.selectbox('Select Brokerage:', options=data['FirmName'].unique())
selected_metric = col2.selectbox('Select Metric:', options=['Volume', 'Value', 'Frequency'])

# Filter the data based on the selected Ticker
data_filtered_by_ticker = data[data['FirmName'] == selected_ticker]

# Adding a slider to select the date range using index values
start_index, end_index = st.slider('Select a date range:', min_value=0, max_value=len(data_filtered_by_ticker) - 1, value=(0, len(data_filtered_by_ticker) - 1))

# Filtering the data based on the selected date range
filtered_data = data_filtered_by_ticker.iloc[start_index:end_index + 1]

# Create a figure with subplots
fig = go.Figure()

# Determine the metric and y/y metric to be plotted based on the selected metric
metric_yoy = f"{selected_metric} (y/y)"
fig.add_trace(go.Bar(x=filtered_data['Date'], y=filtered_data[selected_metric], name=selected_metric, width=20 * 86400000, marker_color='#0F1B93'))
fig.add_trace(go.Scatter(x=filtered_data['Date'], y=filtered_data[metric_yoy], name=metric_yoy, line=dict(dash='dot', color='#E67E22', width=4), yaxis='y2'))


# Add a scatter trace for "Visits (y/y)" on a secondary y-axis, presented in percentages
fig.add_trace(go.Scatter(x=filtered_data['Date'], y=filtered_data['Volume (y/y)'], name='Volume (y/y)', line=dict(dash='dot', color='#E67E22', width=4), yaxis='y2'))

# Update layout to include a secondary y-axis for percentages, rounded to 1 decimal, and remove grid lines
fig.update_layout(
    yaxis=dict(title='<b>Volume</b>'),
    yaxis2=dict(title='<b>Volume (y/y)</b>', overlaying='y', side='right', tickformat='.1%', showgrid=False, zeroline=False),  # Remove grid lines
    xaxis=dict(title='<b>Date</b>'),
    barmode='overlay',
    template='plotly_white',
    legend=dict(y=1, x=1, xanchor='right', yanchor='top')
)

# Displaying the plot in the Streamlit app
st.plotly_chart(fig)
