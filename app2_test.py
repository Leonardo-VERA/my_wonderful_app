import streamlit as st
import plotly.express as px
import pandas as pd

# Cargar datos
url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv'
df = pd.read_csv(url)

st.title("Scatter Plot en Streamlit con Plotly Express")

# use plotly express to create a scatter plot
fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)

# show the plot
# fig.show()
st.plotly_chart(fig)
