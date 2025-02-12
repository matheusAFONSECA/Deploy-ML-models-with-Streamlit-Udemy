import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("02_streamlit_fundamentals\data_display\data\sample.csv", dtype="int")

# Display data
st.dataframe(df)
st.write(df)

# Display table
st.table(df)

# Metrics
st.metric(label="Expenses", value=900, delta=20, delta_color="inverse")