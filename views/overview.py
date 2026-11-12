import streamlit as st
import plotly.express as px
from utils.data import load_data
from utils.config import COLORS, ORDERS
from utils.figures import plot_family_size_histogram, plot_survival_pie_chart, plot_heatmap


st.set_page_config(layout="wide")
data = st.session_state.data
show_data = st.session_state.show_data
df = st.session_state.df

# center the title and image
st.markdown("<h1 style='text-align: center;'>Titanic Survival Prediction App</h1>", unsafe_allow_html=True)

# Use three columns to center the local image in the middle column
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("utils/titanic_pic.jpeg", width=500)

if show_data:
    st.subheader("Raw data")
    st.dataframe(df.head(5))
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Total passengers", data.shape[0], border=True)

with c2:
    st.metric("Survival rate", f"{data['survived'].mean() * 100:.2f}%", border=True)

with c3:
    st.metric("Median age", f"{data['age'].median():.2f}", border=True)

with c4:
    st.metric("Median fare", f"${data['fare'].median():.2f}", border=True)


tab1, tab2 = st.tabs(["Family size & outcome","Heatmap"])
with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(plot_family_size_histogram(data))

    with c2:
        st.plotly_chart(plot_survival_pie_chart(data))

with tab2:
    st.plotly_chart(plot_heatmap(data))
