import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="CORD-19 Explorer", layout="wide")
st.title("CORD-19 Data Explorer")

# Load data
try:
    df = pd.read_csv("cleaned_metadata.csv", low_memory=False)
    st.success("Data loaded successfully!")
except:
    st.error("Please run create_sample.py and data_cleaning.py first")
    st.stop()

# Basic analysis
st.header("Basic Analysis")

# Year distribution
year_counts = df['publish_year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title('Publications by Year')
st.pyplot(fig)

# Journal distribution
journal_counts = df['journal'].value_counts().head(10)
st.subheader("Top 10 Journals")
st.bar_chart(journal_counts)

# Data sample
st.subheader("Data Sample")
st.dataframe(df[['title', 'journal', 'publish_year', 'authors']].head(10))

# Statistics
st.subheader("Statistics")
col1, col2 = st.columns(2)
col1.metric("Total Publications", len(df))
col2.metric("Year Range", f"{df['publish_year'].min()} - {df['publish_year'].max()}")