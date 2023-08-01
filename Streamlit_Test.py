import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the Streamlit app
st.title('Visits Analysis')

# Reading the data from the Excel file
file_path = 'Streamlit_Test.xlsx'
data = pd.read_excel(file_path)
print(data)
print('1---------------------------')
# Converting the "Month" column to a datetime object
data['Month'] = pd.to_datetime(data['Month'])

# Adding a slider to select the date range using index values
start_index, end_index = st.slider('Select a date range:', min_value=0, max_value=len(data) - 1, value=(0, len(data) - 1))

# Filtering the data based on the selected date range
filtered_data = data.iloc[start_index:end_index + 1]

# Creating a figure and axis
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plotting "Visits" on the first y-axis
ax1.plot(filtered_data['Month'], filtered_data['Visits'], color='b', label='Visits')
ax1.set_xlabel('Month')
ax1.set_ylabel('Visits', color='b')
ax1.tick_params(axis='y', colors='b')
ax1.legend(loc='upper left')

# Creating a second y-axis to plot "Visits (y/y)"
ax2 = ax1.twinx()
ax2.plot(filtered_data['Month'], filtered_data['Visits (y/y)'], color='r', label='Visits (y/y)')
ax2.set_ylabel('Visits (y/y)', color='r')
ax2.tick_params(axis='y', colors='r')
ax2.legend(loc='upper right')

# Displaying the plot in the Streamlit app
st.pyplot(fig)
