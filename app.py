import streamlit as st
import plotly.express as px
from utils.data import load_data
from utils.config import COLORS, ORDERS


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
    fig = px.histogram(data, x="family_size", nbins=11, labels={"family_size": "Family size (incl. the passenger)"},
                   title="How big were the families on board?")
    fig.update_layout(bargap=0.1, yaxis_title="Passengers")
    st.plotly_chart(fig, use_container_width=True)

with c2:
    outcome = data["survival"].value_counts().reset_index()

    fig2 = px.pie(outcome, names="survival", values="count", hole=0.5, color="survival",
                color_discrete_map=COLORS, title="Died vs survived")
    st.plotly_chart(fig2, use_container_width=True)