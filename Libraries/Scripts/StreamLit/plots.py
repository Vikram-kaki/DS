import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(30, 3), index=range(1, 31), columns=['Vikram', 'Anil', 'Jaya'])

st.title("Interacting with Plots")

# Line Chart
st.subheader('Line Chart')
st.line_chart(df1)
# chart.x_axis.label("fj")

# Area Chart
st.subheader('Area Chart')
st.area_chart(df1)

# Bar Chart
st.subheader('Bar Chart')
st.bar_chart(df1)

# Plots using matplotlib and seaborn
st.header("Using Matplotlib and Seaborn")
st.subheader("Loading the dataframe")

df2 = pd.read_csv('../../File1.csv')
st.dataframe(df2.head())

# Bar plot

# Matplotlib
st.subheader('Distribution Plot with Matplotlib')
fig = plt.figure(figsize=(15, 5))
df2['Team'].value_counts().plot(kind='bar')
st.pyplot(fig)

# Seaborn
st.subheader('Distribution Plot with Seaborn')
fig = plt.figure(figsize=(15, 5))
sns.distplot(df2['Team'].value_counts())
st.pyplot(fig)