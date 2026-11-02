
import streamlit as st
import pandas as pd

from database import get_participants
from dashboard_utils import count_groups, get_group_counts


st.set_page_config(
    page_title="Psychology Research Dashboard",
    page_icon="🧠",
    layout="wide"
)


st.title("🧠 Psychology Research Dashboard")
st.caption("Cognitive experiment research portal")


df = get_participants()

groups = count_groups(df)


# --------------------------------------------------
# STUDY OVERVIEW
# --------------------------------------------------

st.subheader("Study Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Participants", len(df))

with col2:
    st.metric("AI", groups["AI"])

with col3:
    st.metric("Non-AI", groups["Non-AI"])

with col4:
    st.metric("Control", groups["Control"])


# --------------------------------------------------
# GROUP DISTRIBUTION
# --------------------------------------------------

st.subheader("Participants by Group")

group_counts = get_group_counts(df)

st.bar_chart(
    group_counts,
    x="Group",
    y="Participants"
)


# --------------------------------------------------
# DEMOGRAPHIC OVERVIEW
# --------------------------------------------------

st.divider()
st.subheader("Demographic Overview")

if not df.empty:

    col1, col2, col3 = st.columns(3)

    with col1:
        if "age" in df.columns:
            ages = pd.to_numeric(df["age"], errors="coerce")
            average_age = ages.mean()

            st.metric(
                "Average Age",
                f"{average_age:.1f}" if pd.notna(average_age) else "N/A"
            )

    with col2:
        if "gender" in df.columns:
            gender_count = df["gender"].nunique()
            st.metric("Gender Categories", gender_count)

    with col3:
        if "university" in df.columns:
            university_count = df["university"].nunique()
            st.metric("Universities Represented", university_count)


    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Participants by Gender**")

        if "gender" in df.columns:
            gender_data = (
                df["gender"]
                .dropna()
                .value_counts()
                .rename_axis("Gender")
                .reset_index(name="Participants")
            )

            if not gender_data.empty:
                st.bar_chart(
                    gender_data,
                    x="Gender",
                    y="Participants"
                )

    with col2:
        st.markdown("**Participants by Academic Year**")

        if "academic_year" in df.columns:
            year_data = (
                df["academic_year"]
                .dropna()
                .value_counts()
                .rename_axis("Academic Year")
                .reset_index(name="Participants")
            )

            if not year_data.empty:
                st.bar_chart(
                    year_data,
                    x="Academic Year",
                    y="Participants"
                )

else:
    st.info("No participant data available yet.")
