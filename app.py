import streamlit as st
import pandas as pd
import numpy as np
import time

# Set page config
st.set_page_config(page_title="Streamlit Feature Showcase", layout="wide")

# Title and Header
st.title("🎈 Streamlit Feature Showcase")
st.header("An app that uses lots of Streamlit features!")

# Sidebar
st.sidebar.title("Sidebar Settings")
name = st.sidebar.text_input("Enter your name", "Guest")
age = st.sidebar.slider("Select your age", 10, 100, 25)

# Welcome message
st.markdown(f"👋 Hello, **{name}**! You are **{age}** years old.")

# Button
if st.button("Click me for a fun fact"):
    st.success("🌍 Did you know? Streamlit was acquired by Snowflake!")

# Checkbox
if st.checkbox("Show random data table"):
    df = pd.DataFrame(np.random.randn(10, 5), columns=[f'Col {i}' for i in range(5)])
    st.dataframe(df)

# Selectbox
chart_type = st.selectbox("Select a chart type", ["Line", "Bar", "Area"])

# Simulated data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# Show chart based on selection
st.subheader(f"{chart_type} Chart")
if chart_type == "Line":
    st.line_chart(chart_data)
elif chart_type == "Bar":
    st.bar_chart(chart_data)
elif chart_type == "Area":
    st.area_chart(chart_data)

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file to preview data")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    st.dataframe(data.head())

# Columns
st.subheader("Use of Columns")
col1, col2 = st.columns(2)

with col1:
    st.info("This is the left column")
    color = st.color_picker("Pick a color", "#00f900")
    st.write(f"You picked {color}")

with col2:
    st.info("This is the right column")
    date = st.date_input("Pick a date")
    st.write(f"📅 You selected: {date}")

# Progress bar
st.subheader("Progress bar example")
progress_text = "⏳ Operation in progress..."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)

st.success("✅ Done!")

# Caching example
@st.cache_data
def expensive_computation(x):
    time.sleep(2)
    return x ** 2

st.subheader("Cached Computation")
val = st.number_input("Enter a number", 0, 100)
result = expensive_computation(val)
st.write(f"Square of {val} is {result}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit.")

