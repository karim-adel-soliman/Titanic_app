import plotly.express as px

def plot_family_size_histogram(data):
    fig = px.histogram(data, x="family_size", nbins=11, labels={"family_size": "Family size (incl. the passenger)"},
                       title="How big were the families on board?")
    fig.update_layout(bargap=0.1, yaxis_title="Passengers")
    return fig

def plot_survival_pie_chart(data):
    outcome = data["survival"].value_counts().reset_index()
    fig = px.pie(outcome, names="survival", values="count", hole=0.5, color="survival",
                 color_discrete_map={"Died": "#D95D4A", "Survived": "#0F766E"}, title="Died vs survived")
    return fig