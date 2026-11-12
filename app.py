import streamlit as st
import plotly.express as px
from utils.data import load_data
from utils.config import COLORS, ORDERS
from utils.figures import plot_family_size_histogram, plot_survival_pie_chart, plot_heatmap


st.set_page_config(layout="wide")
df = load_data()

with st.sidebar:
    st.header("Filters")
    show_data = st.checkbox("Show raw data")
    classes = st.multiselect("Class", options=df['class'].unique(), default=["First", "Second", "Third"])
    genders = st.radio("Gender", options=["male", "female", "All"], index=0)
    age_range = st.slider("Age range", min_value=int(df['age'].min()), max_value=int(df['age'].max()),
                          value=(int(df['age'].min()), int(df['age'].max())))

    st.write("Made by [Karim Adel](https://github.com/karim-adel-soliman)")

if genders == "All":
    genders = ["male", "female"]
else:
    genders = [genders]

data = df[(df["class"].isin(classes)) & (df["sex"].isin(genders) & (df["age"].between(age_range[0], age_range[1])))]
st.session_state.data = data
st.session_state.show_data = show_data
st.session_state.df = df


pages = [
    st.Page("views/overview.py", title="Overview", default=True),
    st.Page("views/conclusion.py", title="Conclusion"),
]
page = st.navigation(pages, position="top")
page.run()