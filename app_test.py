import streamlit as st
import plotly.express as px
import pandas as pd

# Cargar datos desde URL
url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv'
df = pd.read_csv(url)

# Título de la app
st.title('Plotly Express in Streamlit')

# Crear un gráfico interactivo en Streamlit
fig = px.scatter_3d(df, x='gdpPercap', y='lifeExp', z='pop', color='continent')

# Mostrar gráfico en Streamlit
st.plotly_chart(fig)  # Cambié fig.show() por st.plotly_chart(fig)
