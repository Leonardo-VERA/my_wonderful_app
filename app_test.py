import streamlit as st
import plotly.express as px
import pandas as pd

# Cargar datos
url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv'
df = pd.read_csv(url)

# Reducir el dataset (ejemplo: tomar solo 50 filas)
df = df.sample(50, random_state=42)

# Mostrar título
st.title('Plotly Express in Streamlit')

# Crear gráfico 3D con menos puntos
fig = px.scatter_3d(df, x='gdpPercap', y='lifeExp', z='pop', color='continent')

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)
