import plotly.express as px
import streamlit as st
import pandas as pd

# example de dataset online 
url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv'

# load data in a df data structure
df = pd.read_csv(url)

st.title('Plotly Express in Streamlit')
# streamlit run app_test.py dans la terminal
# pip install watchdog to auto refresh the page

# make a scatter 3D plot using the dataset
fig = px.scatter_3d(df, x='gdpPercap', y='lifeExp', z='pop', color='continent')
fig.show()