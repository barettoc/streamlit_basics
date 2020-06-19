import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.write("DISCLAIMER: Sample Data Not Real Data")
st.write("Here's our first attempt at using data to create a table:")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

if st.checkbox('Show REAL New'):
  chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

  st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(100,2) / [10, 50] + [39.115662, -77.563599],
    columns=['lat', 'lon'])

st.map(map_data)

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option
