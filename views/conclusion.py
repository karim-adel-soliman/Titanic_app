import streamlit as st


st.markdown("# Conclusions")

st.markdown(
    """
    ## What the data suggests

    The Titanic passenger data shows that survival was not evenly distributed
    across the passengers. **Gender, passenger class, age, and family size**
    are important factors associated with the outcome.

    - Female passengers generally had a higher survival rate than male
      passengers.
    - First-class passengers generally had better survival outcomes than
      second- and third-class passengers.
    - Children and passengers with smaller family groups often show different
      survival patterns from other age and family-size groups.
    - Fare and passenger class are closely related, so they should not be
      interpreted as completely independent factors.

    ## Interpreting the dashboard

    Use the filters on the Overview page to compare specific passenger groups.
    The metrics and charts update with the selected class, gender, and age
    range, making it easier to see how the groups differ.

    > These results describe associations in the dataset; they do not prove
    > that one passenger characteristic directly caused survival.

    ## Limitations

    This analysis uses a historical passenger manifest and contains missing
    values, particularly for age and cabin-related information. The dataset
    also represents one event, so its patterns should not be generalized to
    every emergency or population.

    ## Final takeaway

    Survival on the Titanic was strongly associated with social and
    demographic factors. Exploring the data through multiple filters gives a
    clearer picture than relying on a single overall survival rate.
    """
)