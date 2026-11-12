import streamlit as st
import plotly.express as px
from utils.data import load_data
from utils.config import COLORS, ORDERS
from utils.figures import plot_family_size_histogram, plot_survival_pie_chart


st.set_page_config(layout="wide")
df = load_data()

st.title("Titanic Survival Prediction App")
st.image("utils/titanic_pic.jpeg", caption="Titanic")


show_data = st.checkbox("Show raw data")
if show_data:
    st.subheader("Raw data")
    st.dataframe(df.head(5))

classes = st.multiselect("Class", options=df['class'].unique(), default=["First", "Second", "Third"])
genders = st.radio("Gender", options=["male", "female"], index=0)

data = df[(df["class"].isin(classes)) & (df["sex"].isin([genders]))]

c1, c2 = st.columns(2)
with c1:
    st.plotly_chart(plot_family_size_histogram(data))

with c2:
    st.plotly_chart(plot_survival_pie_chart(data))