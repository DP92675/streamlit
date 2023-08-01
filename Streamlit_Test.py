import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Creating a figure and axis
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plotting "Visits" as a vertical bar graph
ax1.bar(filtered_data['Month'], filtered_data['Visits'], color='b', label='Visits')
ax1.set_xlabel('Month')
ax1.set_ylabel('Visits', color='b')
ax1.tick_params(axis='y', colors='b')
ax1.legend(loc='upper left')

# Creating a second y-axis to plot "Visits (y/y)" with double line width
ax2 = ax1.twinx()
ax2.plot(filtered_data['Month'], filtered_data['Visits (y/y)'] * 100, color='orange', linestyle='dotted', label='Visits (y/y)', linewidth=2)
ax2.set_ylabel('Visits (y/y) (%)', color='orange')
ax2.tick_params(axis='y', colors='orange')
ax2.legend(loc='upper right')

# Defining a custom formatter function for the second y-axis as a percentage
def percent_formatter(x, pos):
    return '{:.0f}%'.format(x)

# Applying the custom formatter to the second y-axis
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(percent_formatter))

# Displaying the plot in the Streamlit app
st.pyplot(fig)
