import streamlit as st

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


st.subheader("Study Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Participants",
        len(df)
    )

with col2:
    st.metric(
        "AI",
        groups["AI"]
    )

with col3:
    st.metric(
        "Non-AI",
        groups["Non-AI"]
    )

with col4:
    st.metric(
        "Control",
        groups["Control"]
    )


st.subheader("Participants by Group")

group_counts = get_group_counts(df)

st.bar_chart(
    group_counts,
    x="Group",
    y="Participants"
)