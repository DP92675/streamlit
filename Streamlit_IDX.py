import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Adjusted title with smaller font size
st.markdown('<h2 style="font-size:20px;">Indonesian Stock Brokerage Benchmarking</h2>', unsafe_allow_html=True)

# Reading the data from the uploaded Excel file
file_path = 'IDX_Scrape_Streamlit.xlsx'
data = pd.read_excel(file_path)

# Converting the "Date" column to a datetime object
data['Date'] = pd.to_datetime(data['Date'])

# Dropdown to select the Metric
selected_metric = st.selectbox('Select Metric:', options=['Volume', 'Value', 'Frequency'], key='select_metric')

# Create two columns for the 'Select Brokerage' dropdowns
col1, col2 = st.columns(2)
selected_ticker1 = col1.selectbox('Select Brokerage 1:', options=data['FirmName'].unique(), key='select_brokerage1')
selected_ticker2 = col2.selectbox('Select Brokerage 2:', options=data['FirmName'].unique(), key='select_brokerage2')

# Determine the maximum y-axis and y/y-axis limits across both brokerages
max_y = max(data[data['FirmName'].isin([selected_ticker1, selected_ticker2])][selected_metric].max(), 0)
max_yoy = max(data[data['FirmName'].isin([selected_ticker1, selected_ticker2])][f"{selected_metric} (y/y)"].max(), 0)


def plot_chart(selected_ticker, selected_metric, max_y, max_yoy):
    # Filter the data based on the selected Ticker
    data_filtered_by_ticker = data[data['FirmName'] == selected_ticker]

    # Create a figure with subplots based on the selected metric
    fig = go.Figure()

    metric_yoy = f"{selected_metric} (y/y)"
    fig.add_trace(go.Bar(x=data_filtered_by_ticker['Date'], y=data_filtered_by_ticker[selected_metric], name=selected_metric, width=20 * 86400000, marker_color='#0F1B93'))
    fig.add_trace(go.Scatter(x=data_filtered_by_ticker['Date'], y=data_filtered_by_ticker[metric_yoy], name=metric_yoy, line=dict(dash='dot', color='#E67E22', width=4), yaxis='y2'))

    # Update layout to include a secondary y-axis for percentages and other adjustments
    fig.update_layout(
        yaxis=dict(title=f'<b>{selected_metric}</b>', range=[0, max_y]),
        yaxis2=dict(title=f'<b>{metric_yoy}</b>', overlaying='y', side='right', tickformat='.1%', showgrid=False, zeroline=False),
        xaxis=dict(title='<b>Date</b>'),
        barmode='overlay',
        template='plotly_white',
        legend=dict(y=1, x=1, xanchor='right', yanchor='top')
    )

    return fig

# Plotting the first chart
st.plotly_chart(plot_chart(selected_ticker1, selected_metric, max_y, max_yoy))

# Reduced gap between the two charts
st.markdown('<p style="line-height:0.1;"> </p>', unsafe_allow_html=True)  # Use minimal line-height to reduce vertical gap

# Plotting the second chart
st.plotly_chart(plot_chart(selected_ticker2, selected_metric, max_y, max_yoy))